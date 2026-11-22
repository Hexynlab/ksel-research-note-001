"""Unit tests for the RN-008 structural evaluator."""
import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("evaluate.py")
SPEC = importlib.util.spec_from_file_location("ksel_evaluate", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)
DATASET_PATH = MODULE_PATH.parents[1] / "data" / "dev" / "ksel-synthetic-dev-v0.2.jsonl"


class EvaluatorTests(unittest.TestCase):
    def test_public_development_dataset_integrity(self):
        rows = MODULE.read_jsonl(DATASET_PATH)
        self.assertEqual(len(rows), 15)
        case_ids = [row["case_id"] for row in rows]
        self.assertEqual(len(case_ids), len(set(case_ids)))
        by_id = {row["case_id"]: row for row in rows}
        self.assertEqual(by_id["KSEL-DEV-013"]["gold"]["dependent_pairs"], [])
        self.assertEqual(by_id["KSEL-DEV-013"]["gold"]["independent_pairs"], [])
        self.assertEqual(
            {tuple(pair) for pair in by_id["KSEL-DEV-014"]["gold"]["dependent_pairs"]},
            {("E1", "E2"), ("E2", "E3"), ("E1", "E3")},
        )
        self.assertIn("single derivation chain", by_id["KSEL-DEV-014"]["claims"][0]["text"])
        self.assertEqual(by_id["KSEL-DEV-014"]["gold"]["expected_decision_status"], "supported")
        self.assertEqual(by_id["KSEL-DEV-015"]["gold"]["dependent_pairs"], [["E1", "E2"]])
        self.assertEqual(by_id["KSEL-DEV-015"]["gold"]["provenance_conflicts"], [["E1", "E2"]])
        for row in rows:
            gold = row["gold"]
            evidence_ids = {item["evidence_id"] for item in row["evidence"]}
            self.assertTrue(set(gold["valid_evidence_ids"]).issubset(evidence_ids))
            self.assertTrue(set(gold["invalid_evidence_ids"]).issubset(evidence_ids))
            self.assertFalse(set(gold["valid_evidence_ids"]) & set(gold["invalid_evidence_ids"]))
            for claim_id, evidence_id in gold["required_links"]:
                self.assertIn(claim_id, {claim["claim_id"] for claim in row["claims"]})
                self.assertIn(evidence_id, evidence_ids)
            self.assertIn(gold["expected_decision_status"], {"supported", "uncertain", "unsupported", "review_required"})

    def setUp(self):
        self.dataset = [{
            "case_id": "C-1",
            "evidence": [
                {"evidence_id": "E-1"}, {"evidence_id": "E-2"},
                {"evidence_id": "E-3"}, {"evidence_id": "E-4"},
            ],
            "gold": {
                "required_links": [["CL-1", "E-1"]],
                "valid_evidence_ids": ["E-1"],
                "invalid_evidence_ids": ["E-2"],
                "stale_evidence_ids": ["E-2"],
                "dependent_pairs": [["E-3", "E-4"]],
                "independent_pairs": [["E-1", "E-2"]],
                "contradiction_pairs": [["E-1", "E-2"]],
                "review_required": True,
                "expected_decision_status": "review_required",
            },
        }]

    def test_perfect_prediction(self):
        prediction = [{
            "case_id": "C-1",
            "traceability_links": [{"claim_id": "CL-1", "evidence_id": "E-1"}],
            "accepted_evidence_ids": ["E-1"],
            "flagged_evidence_ids": ["E-2"],
            "independent_pairs": [{"evidence_a": "E-1", "evidence_b": "E-2"}],
            "dependent_pairs": [{"evidence_a": "E-3", "evidence_b": "E-4"}],
            "contradiction_pairs": [{"evidence_a": "E-1", "evidence_b": "E-2"}],
            "review_completed": True,
            "authorization_valid": True,
            "decision_status": "review_required",
        }]
        result = MODULE.evaluate(self.dataset, prediction)
        self.assertEqual(result["metrics"]["traceability"]["f1"], 1.0)
        self.assertEqual(result["metrics"]["invalid_evidence_detection"]["f1"], 1.0)
        self.assertEqual(result["metrics"]["valid_evidence_retention"], 1.0)
        self.assertEqual(result["metrics"]["false_acceptance_rate"], 0.0)
        self.assertEqual(result["metrics"]["stale_evidence_detection_recall"], 1.0)
        self.assertEqual(result["metrics"]["dependent_pair_detection"]["f1"], 1.0)
        self.assertEqual(result["metrics"]["independent_pair_detection"]["f1"], 1.0)
        self.assertEqual(result["metrics"]["false_independence_rate"], 0.0)
        self.assertEqual(result["metrics"]["false_dependence_rate"], 0.0)
        self.assertEqual(result["metrics"]["contradiction_preservation"]["f1"], 1.0)
        self.assertEqual(result["metrics"]["review_and_authorization_compliance"], 1.0)
        self.assertEqual(result["metrics"]["decision_status_accuracy"], 1.0)

    def test_abstention_does_not_score_as_source_dependence_detection(self):
        prediction = [{
            "case_id": "C-1",
            "traceability_links": [{"claim_id": "CL-1", "evidence_id": "E-1"}],
            "accepted_evidence_ids": ["E-1"],
            "flagged_evidence_ids": ["E-2"],
            "independent_pairs": [],
            "dependent_pairs": [],
            "contradiction_pairs": [],
            "review_completed": True,
            "authorization_valid": True,
            "decision_status": "review_required",
        }]
        result = MODULE.evaluate(self.dataset, prediction)
        self.assertEqual(result["metrics"]["dependent_pair_detection"]["recall"], 0.0)
        self.assertEqual(result["metrics"]["independent_pair_detection"]["recall"], 0.0)

    def test_unresolved_prediction_is_reported_and_not_counted_as_independent(self):
        prediction = [{
            "case_id": "C-1", "dependent_pairs": [], "independent_pairs": [],
            "unresolved_pairs": [{"evidence_a": "E-3", "evidence_b": "E-4"}],
        }]
        result = MODULE.evaluate(self.dataset, prediction)
        self.assertEqual(result["metrics"]["false_independence_rate"], 0.0)
        self.assertEqual(result["metrics"]["dependent_pair_detection"]["recall"], 0.0)
        self.assertEqual(result["metrics"]["unresolved_prediction_rate"], 1.0)
        self.assertEqual(result["metrics"]["source_dependence_classification_coverage"], 1.0)

    def test_ambiguous_and_conflicting_gold_pairs_are_not_binary_scored(self):
        dataset = [{
            **self.dataset[0],
            "gold": {**self.dataset[0]["gold"], "dependent_pairs": [], "independent_pairs": [],
                     "ambiguous_pairs": [["E-1", "E-3"]], "conflicting_pairs": [["E-2", "E-4"]]}
        }]
        prediction = [{"case_id": "C-1", "dependent_pairs": [], "independent_pairs": [],
                       "unresolved_pairs": [{"evidence_a": "E-1", "evidence_b": "E-3"},
                                            {"evidence_a": "E-2", "evidence_b": "E-4"}]}]
        result = MODULE.evaluate(dataset, prediction)
        self.assertIsNone(result["metrics"]["false_independence_rate"])
        self.assertEqual(result["metrics"]["unresolved_recall_on_ambiguous_or_conflicting"], 1.0)
        self.assertEqual(result["metrics"]["confident_classification_rate_on_ambiguous_or_conflicting"], 0.0)

    def test_pair_cannot_be_both_resolved_and_unresolved(self):
        prediction = [{"case_id": "C-1", "dependent_pairs": [{"evidence_a": "E-3", "evidence_b": "E-4"}],
                       "unresolved_pairs": [{"evidence_a": "E-4", "evidence_b": "E-3"}]}]
        with self.assertRaisesRegex(ValueError, "multiple source-dependence classifications"):
            MODULE.evaluate(self.dataset, prediction)

    def test_unlabelled_source_dependence_pair_is_rejected(self):
        prediction = [{
            "case_id": "C-1",
            "independent_pairs": [{"evidence_a": "E-1", "evidence_b": "E-3"}],
            "dependent_pairs": [],
        }]
        with self.assertRaisesRegex(ValueError, "unlabelled evidence pair"):
            MODULE.evaluate(self.dataset, prediction)

    def test_pair_cannot_be_both_dependent_and_independent(self):
        prediction = [{
            "case_id": "C-1",
            "independent_pairs": [{"evidence_a": "E-3", "evidence_b": "E-4"}],
            "dependent_pairs": [{"evidence_a": "E-4", "evidence_b": "E-3"}],
        }]
        with self.assertRaisesRegex(ValueError, "both dependent and independent"):
            MODULE.evaluate(self.dataset, prediction)

    def test_duplicate_pairs_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "Duplicate pair"):
            MODULE.pair_set([["E-1", "E-2"], ["E-2", "E-1"]])

    def test_missing_prediction_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "missing cases"):
            MODULE.evaluate(self.dataset, [])

    def test_unknown_prediction_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "unknown case IDs"):
            MODULE.evaluate(self.dataset, [{"case_id": "UNKNOWN"}])

    def test_duplicate_prediction_is_rejected(self):
        row = {"case_id": "C-1"}
        with self.assertRaisesRegex(ValueError, "duplicate case_id"):
            MODULE.evaluate(self.dataset, [row, row])

    def test_pair_order_is_irrelevant(self):
        result = MODULE.pair_set([{"evidence_a": "E-4", "evidence_b": "E-3"}], "evidence_a", "evidence_b")
        self.assertEqual(result, {("E-3", "E-4")})


if __name__ == "__main__":
    unittest.main()

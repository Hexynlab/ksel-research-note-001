"""Contract tests for the public RN-008 prediction JSON Schema."""
import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "benchmark" / "schemas" / "prediction.schema.json"
EXAMPLE_PATH = ROOT / "benchmark" / "examples" / "predictions.example.jsonl"


class PredictionSchemaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(cls.schema)
        cls.validator = Draft202012Validator(cls.schema)
        cls.examples = [
            json.loads(line)
            for line in EXAMPLE_PATH.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

    def test_schema_is_valid_draft_2020_12(self):
        Draft202012Validator.check_schema(self.schema)

    def test_public_example_matches_prediction_contract(self):
        self.assertTrue(self.examples, "Expected at least one prediction example")
        for prediction in self.examples:
            with self.subTest(case_id=prediction.get("case_id")):
                self.validator.validate(prediction)

    def test_missing_required_property_is_rejected(self):
        prediction = dict(self.examples[0])
        prediction.pop("decision_status")
        self.assertTrue(list(self.validator.iter_errors(prediction)))

    def test_unknown_top_level_property_is_rejected(self):
        prediction = dict(self.examples[0], unreviewed_extra_field=True)
        self.assertTrue(list(self.validator.iter_errors(prediction)))

    def test_invalid_decision_status_is_rejected(self):
        prediction = dict(self.examples[0], decision_status="probably")
        self.assertTrue(list(self.validator.iter_errors(prediction)))

    def test_non_boolean_review_flag_is_rejected(self):
        prediction = dict(self.examples[0], review_completed="yes")
        self.assertTrue(list(self.validator.iter_errors(prediction)))

    def test_malformed_pair_is_rejected(self):
        prediction = dict(self.examples[0])
        prediction["independent_pairs"] = [{"evidence_a": "E-1", "unexpected": "E-2"}]
        self.assertTrue(list(self.validator.iter_errors(prediction)))


if __name__ == "__main__":
    unittest.main()

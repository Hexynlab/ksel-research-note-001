"""Black-box conformance tests for the KSEL Profile A v0.1.0 reference API.

These tests are deliberately separate from the implementation's unit tests.
They exercise only documented public functions and fixture records. They are
not an independent third-party replication or evidence of KSEL effectiveness.
"""
import json
import unittest
from pathlib import Path

from ksel_profile_a import (
    HashChainAuditLedger,
    KSELTransitionError,
    KSELValidationError,
    transition_claim,
    validate_records,
)

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "examples" / "profile-a-examplelib.jsonl"


def fixture_records():
    return [json.loads(line) for line in FIXTURE.read_text(encoding="utf-8").splitlines() if line.strip()]


class ProfileAConformanceTests(unittest.TestCase):
    def setUp(self):
        self.records = fixture_records()
        self.index = validate_records(self.records)
        self.claim = self.index["CLM-EXAMPLELIB-01"]

    def test_reference_fixture_is_accepted_as_a_complete_record_set(self):
        self.assertEqual(set(self.index), {r["id"] for r in self.records})

    def test_schema_invalid_nested_record_is_reported_as_validation_error(self):
        records = [dict(r) for r in self.records]
        claim = next(r for r in records if r["record_type"] == "claim")
        claim["evidence_links"] = None
        with self.assertRaises(KSELValidationError):
            validate_records(records)

    def test_non_mapping_record_is_reported_as_validation_error(self):
        with self.assertRaises(KSELValidationError):
            validate_records(self.records + ["not-a-record"])

    def test_dangling_source_lineage_is_rejected(self):
        records = [dict(r) for r in self.records]
        source = next(r for r in records if r["record_type"] == "source")
        source["derived_from"] = ["SRC-NOT-PRESENT"]
        with self.assertRaises(KSELValidationError):
            validate_records(records)

    def test_uncertainty_reference_to_missing_record_is_rejected(self):
        records = [dict(r) for r in self.records]
        uncertainty = next(r for r in records if r["record_type"] == "uncertainty")
        uncertainty["affected_record_ids"] = ["REC-NOT-PRESENT"]
        with self.assertRaises(KSELValidationError):
            validate_records(records)

    def test_review_snapshot_with_stale_evidence_version_is_rejected(self):
        records = [dict(r) for r in self.records]
        review = next(r for r in records if r["record_type"] == "review")
        review["evidence_snapshot"][0]["version"] += 1
        with self.assertRaises(KSELValidationError):
            validate_records(records)

    def test_empty_custom_role_policy_denies_every_transition(self):
        claim = dict(self.claim, review_state="draft")
        with self.assertRaises(KSELTransitionError):
            transition_claim(
                claim, "evidence_linked", actor="analyst-1",
                actor_role="analyst", required_roles={}
            )

    def test_custom_role_policy_is_used_when_explicitly_supplied(self):
        claim = dict(self.claim, review_state="draft")
        result = transition_claim(
            claim, "evidence_linked", actor="owner-1",
            actor_role="owner", required_roles={"evidence_linked": {"owner"}}
        )
        self.assertEqual(result["review_state"], "evidence_linked")

    def test_transition_rejects_non_string_actor_identity_cleanly(self):
        claim = dict(self.claim, review_state="draft")
        with self.assertRaises(KSELTransitionError):
            transition_claim(claim, "evidence_linked", actor=17, actor_role="analyst")

    def test_audit_ledger_does_not_retain_caller_mutations(self):
        ledger = HashChainAuditLedger()
        event = {"id": "AUD-CONF-1", "event_type": "created", "metadata": {"x": 1}}
        ledger.append(event)
        event["metadata"]["x"] = 99
        self.assertEqual(ledger.entries[0]["event"]["metadata"]["x"], 1)
        self.assertTrue(ledger.verify())

    def test_audit_ledger_does_not_expose_mutable_internal_entries(self):
        ledger = HashChainAuditLedger()
        ledger.append({"id": "AUD-CONF-2", "event_type": "created"})
        exposed = ledger.entries
        exposed[0]["event"]["event_type"] = "rewritten"
        self.assertTrue(ledger.verify())

    def test_audit_replay_requires_a_contiguous_allowed_transition_sequence(self):
        ledger = HashChainAuditLedger()
        ledger.append({
            "id": "AUD-CONF-3", "event_type": "state_transition",
            "target_id": "CLM-X", "prior_state": "draft",
            "resulting_state": "evidence_linked",
        })
        ledger.append({
            "id": "AUD-CONF-4", "event_type": "state_transition",
            "target_id": "CLM-X", "prior_state": "draft",
            "resulting_state": "review_required",
        })
        with self.assertRaises(KSELValidationError):
            ledger.reconstruct_claim_states({"CLM-X": "draft"})


if __name__ == "__main__":
    unittest.main()

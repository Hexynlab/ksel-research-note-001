"""Adversarial and behavioural tests for the KSEL Profile A reference engine."""
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
FIXTURES = ROOT / "examples" / "profile-a-examplelib.jsonl"


def load_records():
    return [json.loads(line) for line in FIXTURES.read_text().splitlines() if line.strip()]


class ProfileAEngineTests(unittest.TestCase):
    def setUp(self):
        self.records = load_records()
        self.index = validate_records(self.records)
        self.claim = dict(self.index["CLM-EXAMPLELIB-01"])

    def test_fixture_cross_references_validate(self):
        self.assertEqual(len(self.index), 6)

    def test_dangling_evidence_reference_is_rejected(self):
        records = [dict(r) for r in self.records]
        claim = next(r for r in records if r["record_type"] == "claim")
        claim["evidence_links"][0]["evidence_id"] = "EVD-MISSING"
        with self.assertRaisesRegex(KSELValidationError, "missing id"):
            validate_records(records)

    def test_wrong_reference_type_is_rejected(self):
        records = [dict(r) for r in self.records]
        evidence = next(r for r in records if r["record_type"] == "evidence")
        evidence["source_id"] = "CLM-EXAMPLELIB-01"
        with self.assertRaisesRegex(KSELValidationError, "expects source"):
            validate_records(records)

    def test_duplicate_ids_are_rejected(self):
        records = self.records + [dict(self.records[0])]
        with self.assertRaisesRegex(KSELValidationError, "duplicate record id"):
            validate_records(records)

    def test_review_target_version_mismatch_is_rejected(self):
        records = [dict(r) for r in self.records]
        review = next(r for r in records if r["record_type"] == "review")
        review["target_version"] = 99
        with self.assertRaisesRegex(KSELValidationError, "target_version"):
            validate_records(records)

    def test_valid_transition_returns_new_version_without_mutating_input(self):
        claim = dict(self.claim, review_state="draft")
        result = transition_claim(
            claim, "evidence_linked", actor="analyst-1", actor_role="analyst"
        )
        self.assertEqual(result["review_state"], "evidence_linked")
        self.assertEqual(result["record_version"], 2)
        self.assertEqual(claim["record_version"], 1)

    def test_invalid_transition_is_rejected(self):
        with self.assertRaises(KSELTransitionError):
            transition_claim(
                self.claim, "approved", actor="reviewer-placeholder",
                actor_role="approver", review=None
            )

    def test_approval_requires_matching_review_and_role(self):
        claim = dict(self.claim, review_state="review_required")
        review = next(r for r in self.records if r["record_type"] == "review")
        approval = dict(review, decision="approve")
        with self.assertRaises(KSELTransitionError):
            transition_claim(
                claim, "approved", actor="reviewer-placeholder",
                actor_role="reviewer", review=approval
            )
        result = transition_claim(
            claim, "approved", actor="reviewer-placeholder",
            actor_role="approver", review=approval
        )
        self.assertEqual(result["review_state"], "approved")

    def test_audit_chain_detects_event_tampering(self):
        ledger = HashChainAuditLedger()
        ledger.append({"id": "AUD-1", "event_type": "created"})
        ledger.append({"id": "AUD-2", "event_type": "reviewed"})
        self.assertTrue(ledger.verify())
        ledger._entries[0]["event"]["event_type"] = "deleted"
        self.assertFalse(ledger.verify())

    def test_audit_replay_reconstructs_claim_state(self):
        ledger = HashChainAuditLedger()
        ledger.append({
            "id": "AUD-1", "event_type": "state_transition",
            "target_id": "CLM-1", "prior_state": "draft",
            "resulting_state": "evidence_linked",
        })
        ledger.append({
            "id": "AUD-2", "event_type": "state_transition",
            "target_id": "CLM-1", "prior_state": "evidence_linked",
            "resulting_state": "review_required",
        })
        self.assertEqual(
            ledger.reconstruct_claim_states({"CLM-1": "draft"})["CLM-1"],
            "review_required",
        )

    def test_audit_replay_rejects_broken_state_sequence(self):
        ledger = HashChainAuditLedger()
        ledger.append({
            "id": "AUD-1", "event_type": "state_transition",
            "target_id": "CLM-1", "prior_state": "draft",
            "resulting_state": "approved",
        })
        with self.assertRaisesRegex(KSELValidationError, "expected prior state"):
            ledger.reconstruct_claim_states({"CLM-1": "review_required"})


if __name__ == "__main__":
    unittest.main()

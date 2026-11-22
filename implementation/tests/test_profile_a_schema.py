"""Contract tests for the KSEL Profile A JSON Schema bundle."""
import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "implementation" / "schemas" / "profile-a.schema.json"
FIXTURE_PATH = ROOT / "implementation" / "examples" / "profile-a-examplelib.jsonl"


class ProfileAContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(cls.schema)
        cls.validator = Draft202012Validator(cls.schema, format_checker=FormatChecker())
        cls.records = [
            json.loads(line)
            for line in FIXTURE_PATH.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

    def test_all_six_record_types_are_represented(self):
        self.assertEqual(
            {r["record_type"] for r in self.records},
            {"source", "evidence", "claim", "uncertainty", "review", "audit_event"},
        )

    def test_example_records_validate(self):
        for record in self.records:
            with self.subTest(record_id=record.get("id")):
                self.validator.validate(record)

    def test_unknown_properties_are_rejected(self):
        record = dict(self.records[0], unreviewed_extra_field="not allowed")
        self.assertTrue(list(self.validator.iter_errors(record)))

    def test_wrong_schema_version_is_rejected(self):
        record = dict(self.records[0], schema_version="9.9.9")
        self.assertTrue(list(self.validator.iter_errors(record)))

    def test_malformed_timestamp_is_rejected(self):
        record = dict(self.records[0], created_at="not-a-date")
        self.assertTrue(list(self.validator.iter_errors(record)))

    def test_claim_cannot_omit_review_state(self):
        record = dict(self.records[2])
        record.pop("review_state")
        self.assertTrue(list(self.validator.iter_errors(record)))


if __name__ == "__main__":
    unittest.main()

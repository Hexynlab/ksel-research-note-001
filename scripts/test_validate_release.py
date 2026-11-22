"""Unit tests for KSEL release metadata validation."""

import tempfile
import unittest
from pathlib import Path

from validate_release import validate_release


class ReleaseValidationTests(unittest.TestCase):
    def make_root(self, version="1.2.3", changelog=None):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / "VERSION").write_text(version + "\n", encoding="utf-8")
        (root / "CHANGELOG.md").write_text(
            changelog if changelog is not None else f"# Changelog\n\n## [{version}] - 2026-11-22\n\n- Initial release.\n",
            encoding="utf-8",
        )
        for relative in (
            "governance/RELEASE-GOVERNANCE.md",
            "governance/RELEASE-CHECKLIST.md",
            "governance/RESEARCH-INTEGRITY.md",
            "governance/REPRODUCIBILITY-STANDARD.md",
            "governance/PUBLICATION-AND-REVIEW-POLICY.md",
            "governance/PUBLIC-DISCLOSURE-POLICY.md",
            "CITATION.cff",
            "README.md",
        ):
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("fixture\n", encoding="utf-8")
        return root

    def test_accepts_matching_version_tag_and_changelog(self):
        root = self.make_root()
        self.assertEqual(validate_release(root, "v1.2.3"), [])

    def test_rejects_tag_version_mismatch(self):
        root = self.make_root()
        self.assertTrue(any("does not match VERSION" in e for e in validate_release(root, "v1.2.4")))

    def test_rejects_invalid_semver(self):
        root = self.make_root(version="01.2.3")
        self.assertTrue(any("valid SemVer" in e for e in validate_release(root, "v01.2.3")))

    def test_rejects_missing_changelog_entry(self):
        root = self.make_root(changelog="# Changelog\n\n## [0.0.1]\n")
        self.assertTrue(any("no section" in e for e in validate_release(root, "v1.2.3")))

    def test_rejects_missing_governance_file(self):
        root = self.make_root()
        (root / "governance/RELEASE-CHECKLIST.md").unlink()
        self.assertTrue(any("RELEASE-CHECKLIST.md" in e for e in validate_release(root, "v1.2.3")))


if __name__ == "__main__":
    unittest.main()

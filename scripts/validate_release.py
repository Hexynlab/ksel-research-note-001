#!/usr/bin/env python3
"""Validate KSEL repository release metadata using only the Python standard library."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SEMVER = re.compile(
    r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)"
    r"(?:-([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?$"
)


def validate_release(root: Path, tag: str) -> list[str]:
    errors: list[str] = []
    version_path = root / "VERSION"
    changelog_path = root / "CHANGELOG.md"

    if not version_path.is_file():
        return ["VERSION file is missing"]
    if not changelog_path.is_file():
        return ["CHANGELOG.md file is missing"]

    version = version_path.read_text(encoding="utf-8").strip()
    if not SEMVER.fullmatch(version):
        errors.append(f"VERSION must contain a valid SemVer value; found: {version!r}")

    expected_tag = f"v{version}"
    if tag != expected_tag:
        errors.append(f"Tag {tag!r} does not match VERSION; expected {expected_tag!r}")

    changelog = changelog_path.read_text(encoding="utf-8")
    if version and f"## [{version}]" not in changelog:
        errors.append(f"CHANGELOG.md has no section for [{version}]")

    required_files = (
        "governance/RELEASE-GOVERNANCE.md",
        "governance/RELEASE-CHECKLIST.md",
        "governance/RESEARCH-INTEGRITY.md",
        "governance/REPRODUCIBILITY-STANDARD.md",
        "governance/PUBLICATION-AND-REVIEW-POLICY.md",
        "governance/PUBLIC-DISCLOSURE-POLICY.md",
        "CITATION.cff",
        "README.md",
    )
    for relative_path in required_files:
        if not (root / relative_path).is_file():
            errors.append(f"Required release-governance file is missing: {relative_path}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tag", required=True, help="Release tag, e.g. v0.1.0")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    errors = validate_release(args.root.resolve(), args.tag)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Release metadata valid for {args.tag}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

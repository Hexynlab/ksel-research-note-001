# KSEL Repository Changelog

This changelog records material changes to the public KSEL repository release series. Individual research notes and experimental artefacts may also maintain their own version histories.

## [0.1.1] - 2026-11-22

### Changed
- Replaced legacy repository URLs in the research-note citation metadata with the canonical Hexynlab repository URL.
- Added selected related-work references and consistent suggested citations to RN-001 through RN-008.
- Replaced broad extension-based licence descriptions with an explicit path-level licence map.
- Clarified that NOTICE identifies H3XYN LAB as the publishing source and does not claim third-party material.
- Pinned GitHub Actions dependencies to full commit SHAs.
- Integrated full-history Gitleaks scanning into the required `schema-tests` job so a failed PR secret scan blocks the existing required status check.
- Kept the scheduled/manual secret scan for periodic repository-history checks.

### Release integrity
- The previously published `v0.1.0` tag and release remain unchanged.
- This patch release records repository documentation and workflow hardening; it does not change KSEL's research claims or report new empirical findings.

## [0.1.0] - 2026-11-22

### Added
- Initial versioned repository release record for the public KSEL Research Notes 001–008.
- Research integrity, publication and review, public disclosure, and reproducibility governance policies.
- RN-008 synthetic development fixture, prediction schema, deterministic evaluator and benchmark protocol.
- Profile A schema and reference-engine implementation with automated tests.
- Required `schema-tests` CI workflow and protected-`main` merge gate.

### Status and limitations
- RN-001 through RN-007 are preliminary research frameworks.
- RN-008 is a proposed experimental protocol with a small public synthetic development fixture.
- No empirical validation, benchmark superiority, certification or independent replication is claimed.
- This entry establishes a repository snapshot record; it does not retroactively imply that a formal release workflow existed on this date.

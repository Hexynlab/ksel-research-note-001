# HEXYN LAB — KSEL Release Governance

**Policy version:** 1.0  
**Applies to:** KSEL research-note series, public schemas, benchmark artefacts, evaluation code and supporting documentation in this repository  
**Status:** Public governance policy  
**Effective date:** 22 November 2026  
**Authority:** HEXYN LAB

## 1. Purpose

This policy establishes a repeatable, evidence-preserving process for preparing, validating, publishing and correcting KSEL releases. It complements the Research Integrity Policy, Publication and Review Policy, Reproducibility Standard and Public Disclosure Policy. It does not replace them.

A release is a versioned snapshot of repository content. A Git tag or GitHub release records publication; neither is evidence that the research has been empirically validated, independently replicated, certified or endorsed.

## 2. Release principles

Every release must be:

- **Identifiable:** carry a unique semantic version and publication date.
- **Traceable:** identify the exact source commit and corresponding tag.
- **Reviewable:** pass the repository's required pull-request and status-check controls.
- **Reproducible where applicable:** include the methods, dependencies, data provenance and execution instructions required by the Reproducibility Standard.
- **Integrity-preserving:** retain prior releases and document material corrections rather than silently rewriting the research record.
- **Accurately represented:** distinguish proposals, protocols, implementation tests, empirical results, independent replication and formal peer review.
- **Disclosure-reviewed:** exclude secrets, personal or restricted data, unsafe operational details and material lacking publication rights.

## 3. Versioning

KSEL repository releases use Semantic Versioning: `MAJOR.MINOR.PATCH`, represented by Git tags `vMAJOR.MINOR.PATCH`.

- **MAJOR:** incompatible changes to published contracts, research architecture, or material changes to the meaning or scope of the release series.
- **MINOR:** backward-compatible substantive additions, such as a new research note, schema capability or benchmark component.
- **PATCH:** corrections, clarifications, documentation improvements or non-breaking fixes that do not materially change research conclusions or public contracts.

Use a prerelease identifier (for example, `v1.1.0-rc.1`) for release candidates. Prereleases must be labelled as such and must not be presented as stable releases.

The root `VERSION` file records the current release version without a leading `v`. The root `CHANGELOG.md` records the changes associated with each version. The tag, VERSION value and changelog entry must agree.

Versioning is a repository snapshot convention. Individual research notes and experimental artefacts may retain their own independent versions and maturity labels.

## 4. Release authority and review

1. Changes intended for `main` must enter through a pull request.
2. The active `KSEL Main Protection` ruleset and required `schema-tests` status check remain mandatory.
3. A release candidate must be reviewed for scope, claims, attribution, licensing, privacy, security and reproducibility.
4. The release owner must complete and retain the release checklist in the pull request or release record.
5. A release tag must point to a commit already reachable from `main`.
6. The release workflow must pass before a GitHub Release is published.
7. Release approval must not be inferred from a passing automated test. Tests establish only the properties they actually exercise.

HEXYN LAB currently operates this repository as an independent research programme. This policy does not imply an external review board, independent governance body or formal peer-review process.

## 5. Automated release validation

The release workflow validates the tag and repository version, checks for the corresponding changelog entry, confirms the tagged commit is on `main`, and runs the public validation suites before creating a GitHub Release.

The required `schema-tests` check remains the merge gate for changes entering `main`. Release validation is an additional publication gate; it does not replace branch protection.

A successful workflow means that the configured release checks passed for that commit. It does not establish empirical validity, security certification or scientific consensus.

## 6. Release contents and record

Each stable release should identify:

- Release version and date.
- Source commit and Git tag.
- Summary of additions, changes, fixes and known limitations.
- Research-note and artefact versions included.
- Validation workflow outcome.
- Material changes to schemas, datasets, metrics or evaluation procedures.
- Corrections, withdrawals or superseded material.
- Relevant research maturity and review status.

GitHub-generated release notes may supplement the changelog but must not replace the repository's maintained changelog.

## 7. Tag and release integrity

Published release tags are historical identifiers and must not be moved or reused. If a release contains a material defect, publish a new patch or subsequent version and clearly identify the affected release.

Where repository administration supports it, protect the `v*` tag namespace against deletion and force updates. This policy does not claim that GitHub tags are cryptographically immutable by default.

For higher-assurance provenance, signed tags and signed commits may be adopted after key custody, verification and recovery procedures are documented. Do not claim signatures are verified unless the release process actually verifies them.

## 8. Corrections, withdrawals and supersession

- Never silently rewrite a published research conclusion.
- Correct errors in a new commit and, where needed, a new patch release.
- Add a changelog entry describing the issue, correction and effect on conclusions.
- Mark superseded documents clearly while retaining historical context.
- If a release must be withdrawn, retain an appropriate notice and explain the reason without exposing restricted information.
- Preserve the relationship between the affected release, correction and replacement.

## 9. Security and disclosure

Before release, inspect the proposed snapshot for credentials, tokens, private keys, personal or re-identifiable data, restricted third-party information, unpatched vulnerability details and other material covered by the Public Disclosure Policy.

If a disclosure concern is found, pause the release and address the specific artefact. Do not conceal a restriction that materially limits reproducibility; document the limitation at a safe level.

## 10. Research maturity and claims

Release labels describe repository publication state, not scientific maturity. A released schema, test suite or benchmark implementation is not by itself evidence that KSEL is effective.

The current RN-008 synthetic development fixture remains a small, public, fictional development set and is not a blind benchmark or empirical validation. Any future empirical claim must meet the Research Integrity Policy and Reproducibility Standard.

## 11. Exceptions and policy changes

Exceptions must be documented with rationale, scope, risk, approving authority and expiry or reassessment date. An exception must not waive legal, privacy, safety or third-party rights obligations.

Changes to this policy must be made through the protected pull-request process and recorded in the changelog when they materially affect release practice.

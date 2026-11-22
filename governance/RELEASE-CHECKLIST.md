# KSEL Release Checklist

Use this checklist for every release candidate. Record the completed checklist in the release pull request or link it from the release record.

## A. Scope and version

- [ ] Release scope and intended audience are stated.
- [ ] Version increment follows `governance/RELEASE-GOVERNANCE.md`.
- [ ] Root `VERSION`, Git tag and changelog heading agree.
- [ ] Research-note and artefact versions are identified separately where applicable.
- [ ] Draft, preliminary, protocol, evaluated, corrected or superseded status is accurate.

## B. Research integrity

- [ ] Claims are proportionate to available evidence.
- [ ] Proposals, hypotheses, implementation tests and empirical results are clearly distinguished.
- [ ] Sources, datasets, software, methods and third-party materials are attributed.
- [ ] Positive, negative, null and inconclusive results are not selectively omitted.
- [ ] Conflicts of interest, funding and material support are disclosed where applicable.
- [ ] Review and replication status is described accurately; no implied endorsement.

## C. Reproducibility and technical validation

- [ ] Required `schema-tests` check passes on the release commit.
- [ ] RN-008 benchmark and evaluator tests pass.
- [ ] Schema and example fixtures validate.
- [ ] Dependencies and execution instructions are current.
- [ ] Dataset provenance, synthetic/real status, limitations and leakage risks are documented.
- [ ] Material experiment configurations, seeds, metrics and deviations are recorded where applicable.
- [ ] Known failures, limitations and environment constraints are documented.

## D. Security, privacy and rights

- [ ] No credentials, tokens, private keys or accidental secrets are included.
- [ ] No personal, sensitive or re-identifiable data is disclosed without a lawful and ethical basis.
- [ ] Third-party licences, permissions and attribution have been checked.
- [ ] Security-sensitive material has received disclosure review.
- [ ] Repository visibility is not represented as a reuse licence.

## E. Publication record

- [ ] Root `CHANGELOG.md` has a concise, accurate entry.
- [ ] `README.md` reflects the current publication set and research status.
- [ ] `CITATION.cff` is accurate for the release.
- [ ] Relevant policies and companion artefacts are linked.
- [ ] Corrections and superseded material are cross-referenced.
- [ ] Release notes identify known limitations and do not overstate validation.

## F. Publication

- [ ] All changes are merged to protected `main` through pull requests.
- [ ] Release tag points to a commit reachable from `main`.
- [ ] Automated release validation passes.
- [ ] GitHub Release is created from the verified tag.
- [ ] Release URL, tag, commit and workflow run are recorded.
- [ ] Any post-release correction is handled as a new version, not a moved tag.

**Release decision:** ☐ Approved ☐ Deferred ☐ Rejected  
**Release version:**  
**Tag / commit:**  
**Checklist owner:**  
**Review date:**  
**Exceptions or unresolved issues:**

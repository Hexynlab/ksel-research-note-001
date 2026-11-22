# KSEL licensing

**Publishing-source attribution: HEXYN LAB.**

KSEL is intended for commercial and non-commercial reuse, subject to the applicable licence terms. This guide defines the file-level scope so that the two licences are not confused or applied to third-party material.

## Exact licence map

### Apache License 2.0 — software and machine-readable implementation

The Apache 2.0 grant in [LICENSE](LICENSE) applies to these repository paths:

- `.github/workflows/*.yml` — CI and release workflow definitions.
- `implementation/ksel_profile_a.py`.
- `implementation/tests/*.py`.
- `implementation/schemas/*.json`.
- `implementation/requirements-dev.txt`.
- `benchmark/evaluation/*.py`.
- `benchmark/schemas/*.json`.
- `scripts/*.py`.

### Creative Commons Attribution 4.0 International — research prose and published examples

The CC BY 4.0 grant in [LICENSE-DOCS](LICENSE-DOCS) applies to original HEXYN LAB material in these paths:

- `research/*.md`.
- `governance/*.md`.
- `implementation/*.md`.
- `benchmark/*.md`.
- Root documentation: `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `RESEARCH-ROADMAP.md`.
- `CITATION.cff` to the extent its original metadata is copyrightable.
- `benchmark/data/**`, `benchmark/examples/**`, and `implementation/examples/**`, subject to the third-party exclusions below.

### Notices and release metadata

- `LICENSE` and `LICENSE-DOCS` reproduce the respective standard licence texts and scope notices; those legal texts are not relicensed as original HEXYN LAB content.
- `NOTICE` is an attribution notice, not a separate licence grant.
- `LICENSING.md` is a scope guide under CC BY 4.0 to the extent copyright subsists in its original prose.
- `VERSION` contains release metadata and is not separately offered as a creative work under either grant.
- Any path not expressly listed above is not automatically covered by either licence. Check for a file-specific notice or obtain permission before reuse.

## Attribution

For CC BY 4.0 material, provide appropriate credit to **HEXYN LAB**, link to the licence, indicate whether changes were made, and do not imply endorsement. For Apache-licensed software, provide a copy of the licence, retain applicable copyright, patent, trademark and attribution notices, reproduce relevant NOTICE content, and mark modified files as required by Apache 2.0.

Suggested attribution:

> KSEL research and/or implementation by HEXYN LAB. Original source: https://github.com/Hexynlab/ksel-research-note-001. Licensed under the applicable licence stated in LICENSING.md. Changes: [describe changes or state none].

Attribution identifies the publishing source; it does not grant permission to use HEXYN LAB names or marks to imply sponsorship, endorsement, or official affiliation.

## Third-party material and exclusions

The grants apply only to original material for which the relevant rights holder has authority to grant the stated permissions. They do not relicense:

- Third-party quotations, figures, tables, images, datasets, code, or other embedded material.
- External standards, specifications, and linked resources.
- Software dependencies and their licences.
- Trademarks, logos, names, or other rights not expressly granted.
- Material identified by a file-specific third-party notice.

A citation or link is not itself permission to reproduce or adapt the cited work. Preserve third-party notices and comply with the rights holder's terms. Public availability does not establish reuse permission.

## Contributions

By intentionally submitting a contribution for inclusion, you confirm that you have the rights needed to submit it and agree that, if accepted, it may be distributed under the licence applicable to its file type above, unless different terms are disclosed and approved before inclusion. You retain ownership of your contribution. Do not submit confidential or third-party material without necessary rights and permissions. For AI-assisted contributions, the submitter remains responsible for reviewing the output, checking applicable tool terms, and screening for third-party material or other restrictions.

## Important

This is a plain-language scope guide, not legal advice or a determination of copyright ownership. The full licence terms are in [LICENSE](LICENSE) and [LICENSE-DOCS](LICENSE-DOCS). HEXYN LAB should apply these grants only to material for which it has the necessary rights. Seek qualified advice for ownership, patents, trademarks, and third-party rights.

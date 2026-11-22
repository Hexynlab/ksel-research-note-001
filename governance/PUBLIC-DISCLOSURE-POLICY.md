# HEXYN LAB — Public Disclosure Policy

**Status:** Public policy, version 1.0  
**Effective date:** 22 November 2026

## 1. Purpose

HEXYN LAB supports open scrutiny of research while recognising that not every artefact should be public. Disclosure decisions should protect people, systems, legitimate rights and research integrity without using secrecy to avoid scientific criticism.

## 2. Generally suitable for public release

Subject to attribution and rights checks, public materials may include:

- Research questions, hypotheses and conceptual models.
- High-level architecture diagrams and non-sensitive interfaces.
- Research methods, evaluation protocols and benchmark definitions.
- Aggregated or synthetic test data with documented limitations.
- Results, uncertainty, negative findings and limitations.
- Public issue trackers, correction records and review responses.
- Non-sensitive schemas, terminology and reproducibility instructions.
- Research roadmaps and publication governance policies.

## 3. Materials requiring restriction or review

Do not publish by default:

- Credentials, tokens, private keys, passwords or access links.
- Personal, sensitive or re-identifiable data.
- Confidential third-party information or unpublished partner material.
- Private datasets without appropriate rights and consent.
- Operational security details that materially enable exploitation.
- Unpatched vulnerability details before responsible disclosure is complete.
- Internal infrastructure configuration that exposes attack paths.
- Proprietary implementation details where disclosure would undermine legitimate IP strategy.
- Materials restricted by contract, law, licence or research ethics requirements.

## 4. Public research versus implementation

A research publication may explain a problem, proposed architecture, threat model, evaluation method and high-level design rationale without disclosing every implementation detail.

The boundary must not be used to make unsupported claims. If implementation is withheld, state that the implementation is not public and avoid implying that readers can independently inspect it.

## 5. Privacy and data minimisation

Prefer synthetic, public-domain, openly licensed or appropriately anonymised data. Assess re-identification risk rather than assuming that removing names is sufficient. Publish data dictionaries and generation procedures where safe, but do not release underlying restricted records.

## 6. Security disclosure

Security findings should be assessed for severity, affected versions, exploitability and remediation status. Coordinate responsible disclosure with affected parties where appropriate. Avoid publishing secrets or turnkey exploit instructions that create unnecessary harm.

## 7. Intellectual property and licensing

Before release, verify ownership and third-party rights. Public availability is not the same as an open-source or open-content licence. A repository licence should be selected deliberately; do not assume that readers have permission to reuse, modify or redistribute material merely because it is visible.

Patent-sensitive or commercially sensitive implementation details should receive appropriate advice before publication. This policy is not legal advice.

## 8. Review and exceptions

When uncertain, delay the specific risky artefact, not the entire research programme. Record the reason for restriction at an appropriate level of detail and reassess when the risk changes.

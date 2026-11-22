# KSEL Research Programme Roadmap

**Institution:** H3XYN LAB  
**Programme:** KSEL — Knowledge, Source, Evidence Layer  
**Status:** Public research roadmap; subject to revision  
**Last updated:** 22 November 2026

## 1. Purpose

KSEL investigates how intelligent systems can make evidence traceable, uncertainty inspectable, knowledge revision governable, and consequential decisions auditable.

The programme is organised as a sequence of connected research questions. Publication of a framework does not establish that it has been implemented, validated, or shown to improve system performance.

## 2. Published research notes

| Note | Research area | Contribution |
|---|---|---|
| RN-001 | Evidence governance | Evidence-to-claim relationships, uncertainty, contradiction handling, review and audit controls |
| RN-002 | Evidence selection | Cost-aware evidence acquisition, Value of Information, review tiers and stopping conditions |
| RN-003 | Integrity and resilience | Provenance, authenticity, source dependence, adversarial resilience and incident reassessment |
| RN-004 | Evidence representation | Versioned evidence graphs, cross-source reasoning, temporal semantics and dependency analysis |
| RN-005 | Decision intelligence | Objectives, constraints, causal assumptions, alternatives, recommendations and authorization |
| RN-006 | Temporal validation | Evidence evolution, freshness, version continuity, revalidation and historical reconstruction |
| RN-007 | Adaptive knowledge | Governed belief revision, controlled memory, feedback-loop safeguards, model-change evaluation and rollback |

These notes form a proposed research architecture. They should be read as connected but independently challengeable contributions.

## 3. Next research priorities

### Priority A — Empirical evaluation (RN-008)

Develop a reproducible evaluation programme to test whether selected KSEL mechanisms improve measurable outcomes relative to clearly specified baselines. The work must measure both benefits and costs, including false updates, missed updates, review burden, latency and operational complexity.

### Priority B — Reference architecture and terminology

Consolidate cross-note concepts into a versioned reference model, glossary, lifecycle diagrams and traceability map. Resolve inconsistent terminology and identify unresolved design choices without implying implementation completeness.

### Priority C — Prototype and conformance research

If a prototype is developed, publish its scope, version, interfaces, test fixtures, known limitations and mapping to the research claims. Any conformance checklist must be described as a research aid, not certification.

### Priority D — Independent replication

Invite external researchers to challenge assumptions, reproduce selected experiments, propose alternative baselines and publish divergent or negative findings.

## 4. Research questions across the programme

1. Can evidence provenance and claim relationships be reconstructed reliably?
2. Can source dependence and duplicated reporting be distinguished from independent corroboration?
3. Can uncertainty and contradiction be represented without false precision?
4. Can evidence acquisition be prioritised without compromising mandatory safety, privacy or review constraints?
5. Can changes in evidence be propagated to affected claims and decisions?
6. Can knowledge revision be separated from model, policy and authority changes?
7. Do these controls improve outcomes enough to justify their cost and complexity?

## 5. Evidence and maturity labels

Use explicit labels in publications and project records:

- **Proposed:** a concept, architecture, method or hypothesis not yet tested.
- **Specified:** a sufficiently detailed design or protocol exists for scrutiny.
- **Implemented:** an identified version of a mechanism exists; this alone does not demonstrate effectiveness.
- **Evaluated:** a documented evaluation has been conducted and its methods and results are available.
- **Independently replicated:** an independent party has reproduced a defined result under documented conditions.
- **Superseded:** a later version replaces the item while its history remains accessible.

Do not promote a work to a higher maturity level without supporting artefacts.

## 6. Publication principles

- State research questions and limitations plainly.
- Distinguish evidence, interpretation, hypothesis and recommendation.
- Predefine evaluation methods where practical.
- Report negative, null and inconclusive results.
- Preserve version history and correction records.
- Avoid claims of certification, superiority or general effectiveness without adequate evidence.
- Protect personal data, confidential information, security-sensitive details and third-party rights.

## 7. Roadmap governance

This roadmap is a planning document, not a commitment that every listed activity is funded, scheduled or completed. Priorities may change as evidence, independent feedback and feasibility assessments develop. Changes should be recorded in the repository history.

## 8. Current status

As of 22 November 2026, RN-001 through RN-007 are published as preliminary research frameworks. RN-008 is a proposed empirical evaluation protocol. No empirical validation or independent replication is claimed by this roadmap.

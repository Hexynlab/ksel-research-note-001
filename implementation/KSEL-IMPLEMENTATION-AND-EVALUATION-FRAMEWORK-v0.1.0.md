# KSEL Implementation and Evaluation Framework

**Document identifier:** KSEL-IEF-001  
**Version:** 0.1.0  
**Institution:** H3XYN LAB  
**Programme:** KSEL — Knowledge, Source, Evidence Layer  
**Publication type:** Implementation companion / research specification  
**Status:** Proposed specification; not a standard, certification scheme, or validated implementation  
**Date:** 22 November 2026  
**Related publications:** KSEL RN-001 through RN-008  
**Related artefacts:** `benchmark/` RN-008 experimental starter kit

---

## Abstract

The KSEL research-note series proposes mechanisms for evidence traceability, multidimensional uncertainty, provenance and integrity assessment, evidence-graph representation, decision governance, temporal validation, and controlled knowledge revision. This companion translates selected concepts into an incremental implementation model without asserting that the complete architecture has been implemented or empirically validated.

It defines three additive implementation profiles, a shared lifecycle, a worked synthetic example carried across the research-note themes, component-boundary guidance for common agent and retrieval systems, minimum record expectations, and implementation-to-evaluation traceability. It also identifies which capabilities are required for a first useful implementation and which remain extensions for later research.

This document is a bridge between the research proposals and future prototypes. It does not amend or supersede the research notes, define a universal compliance regime, or establish conformance certification.

## 1. Purpose and status

KSEL is proposed as a governance layer that makes material evidence, claims, uncertainty, review, and decision history inspectable. It is intended to work with existing models, retrieval systems, tools, databases, and human workflows rather than replace them.

This companion has five purposes:

1. Make the architecture implementable in stages.
2. Demonstrate how the same case moves through multiple KSEL capabilities.
3. Clarify the boundary between KSEL records and common agent/RAG components.
4. Provide a practical starting point for a reference implementation.
5. Connect implementation claims to the existing RN-008 evaluation programme.

### 1.1 Maturity language

The following labels describe the status of artefacts, not the quality of a system:

- **Proposed:** a concept or mechanism has been described but is not yet sufficiently specified or implemented.
- **Specified:** a versioned design, schema, interface, or procedure exists for scrutiny.
- **Implemented:** an identified software version performs the specified operation; this does not establish effectiveness.
- **Evaluated:** a documented evaluation has been conducted under stated conditions.
- **Independently replicated:** an independent party has reproduced a defined result under documented conditions.
- **Superseded:** a later version replaces the artefact while its history remains accessible.

A repository document, schema, test fixture, or passing unit test must not be represented as evidence that the complete KSEL architecture is implemented or effective.

## 2. Incremental implementation profiles

The profiles below are cumulative research implementation scopes. They are not separate standards, product tiers, or certifications. An implementation may adopt a profile only when it can demonstrate the required records and behaviours for the stated scope.

### 2.1 Profile A — Core evidence governance

**Purpose:** establish a minimum useful evidence-governance workflow for material claims.

Required capabilities:

- Stable identifiers for sources, evidence items, claims, and review records.
- Explicit claim-to-evidence relationships with relationship type and rationale.
- Separation of source-derived observations, claims, inferences, and recommendations.
- An uncertainty register with dimension, rationale, affected object, and resolution condition.
- Explicit review states and protected transitions.
- Append-oriented audit events for material creation, assessment, review, release, and revision.
- Visible handling of missing provenance, unresolved contradictions, and unmet review requirements.

Profile A should not require a graph database, automated VOI estimator, model fine-tuning, or autonomous memory updates. A relational database or structured files may be sufficient if referential integrity, version history, and audit requirements are preserved.

**Minimum exit evidence:** a reviewer can select a released claim and reconstruct its linked evidence, known uncertainty, review state, and material state changes.

### 2.2 Profile B — Evidence acquisition and adaptive review

**Purpose:** add explicit governance over whether further evidence should be acquired and how review effort should be allocated.

Includes all Profile A capabilities, plus:

- Candidate evidence-action records.
- A stated decision question and the uncertainty or evidence gap an action is intended to reduce.
- Expected information value, acquisition cost, review cost, delay cost, and operational constraints where estimable.
- Qualitative prioritisation when defensible numerical estimates are unavailable.
- Review tiers tied to consequence, reversibility, uncertainty, and mandatory controls.
- Explicit stopping, escalation, and reassessment conditions.
- A record of why an evidence action was selected, deferred, or rejected.

Profile B must not turn mandatory safety, privacy, security, legal, or human-review requirements into optional costs. A favourable VOI assessment cannot override a hard constraint.

**Minimum exit evidence:** a reviewer can reconstruct why a proposed evidence action was or was not taken, what assumptions informed its priority, and which constraints governed the decision.

### 2.3 Profile C — Versioned evidence and temporal governance

**Purpose:** represent cross-object dependencies and changes over time so that the impact of revised or superseded evidence can be reconstructed.

Includes Profile A and B capabilities, plus:

- Typed relationships between sources, evidence, observations, claims, transformations, assessments, reviews, and decisions.
- Version identifiers for mutable records and explicit supersession links.
- Distinction between event time, observation time, publication time, ingestion time, assessment time, valid time, and record time where applicable.
- Source-lineage and dependency representation.
- Queryable impact paths from changed evidence to affected claims, assessments, and decisions.
- Historical reconstruction that does not overwrite prior states.
- Retention, archival, and privacy-aware pruning rules.

Profile C does not mandate a particular graph database. A relational representation, graph store, or hybrid architecture may be used if the required typed relationships, version semantics, and impact queries are preserved.

**Minimum exit evidence:** a reviewer can identify which claims and decisions depend on a superseded or materially changed evidence item, reconstruct their prior state, and determine which require reassessment.

### 2.4 Cross-cutting extensions

The following RN-003, RN-005, and RN-007 mechanisms should be integrated according to system risk and use case. They are not silently assumed to be fully delivered merely by adopting Profile C.

| Research area | Capability | Implementation consideration |
|---|---|---|
| RN-003 | Integrity and adversarial resilience | Separate content integrity, authenticity, provenance continuity, context, independence, and reliability assessments |
| RN-005 | Decision intelligence | Link objectives, constraints, alternatives, causal assumptions, recommendations, and authorization records |
| RN-007 | Adaptive knowledge | Govern memory admission, belief revision, feedback-loop controls, downstream impact, and rollback |

An implementation must declare which extensions are active and which are out of scope.

## 3. Shared KSEL lifecycle

A practical implementation can organise work around the following lifecycle:

1. **Acquire:** obtain source material using a documented channel.
2. **Register:** assign source and evidence identifiers; preserve origin and acquisition metadata.
3. **Normalize:** extract relevant material while retaining the source reference and transformation record.
4. **Assess:** record integrity, relevance, independence, temporal applicability, and limitations.
5. **Claim:** create atomic, reviewable claims and distinguish them from observations and recommendations.
6. **Link:** record support, qualification, contradiction, contextualisation, or examined-but-unrelated relationships.
7. **Record uncertainty:** identify unresolved dimensions and affected claims or decisions.
8. **Prioritise:** where in scope, evaluate evidence actions and review requirements.
9. **Review:** apply required checks, record reviewer/process identity, and protect controlled state transitions.
10. **Release or defer:** issue a qualified output, escalate, defer, or reject according to explicit criteria.
11. **Monitor:** detect relevant source, policy, model, or context changes.
12. **Reassess:** create new versions and impact records without erasing prior decisions.

Not every deployment requires a separate service for each step. The implementation must preserve the logical responsibilities and auditable transitions.

## 4. Worked synthetic example: a software-security finding

### 4.1 Scenario and limitations

The following case is fictional and is included only to demonstrate record relationships. It does not describe a real vulnerability, product, vendor, or security advisory.

A software team receives a report that a fictional library, **ExampleLib**, may contain a vulnerability affecting a particular version range. Three documents appear to corroborate the report. During review, the team discovers that two documents reproduce the same upstream advisory. A later maintainer notice narrows the affected version range. The team must decide whether to block a release, request more evidence, or proceed with a qualified assessment.

This example illustrates evidence governance; it does not provide operational exploit instructions.

### 4.2 Initial source and evidence records

| ID | Type | Description | Initial assessment |
|---|---|---|---|
| SRC-01 | Source | Fictional upstream advisory | Origin identified; content not yet independently verified |
| SRC-02 | Source | Fictional security-news summary | Derived from SRC-01 |
| SRC-03 | Source | Fictional community repost | Also derived from SRC-01 |
| SRC-04 | Source | Fictional maintainer update | Later publication; origin identified |
| EVD-01 | Evidence | Advisory excerpt describing affected versions | Relevant; integrity and applicability require review |
| EVD-02 | Evidence | News summary repeating the advisory | Relevant as a report; not independent corroboration |
| EVD-03 | Evidence | Community repost repeating the advisory | Relevant as a report; not independent corroboration |
| EVD-04 | Evidence | Maintainer update narrowing the affected range | Potentially authoritative update; requires version and context check |

The source records must preserve the known lineage. Three documents do not constitute three independent confirmations when two derive from the same upstream statement.

### 4.3 Claim and relationship records

| Claim ID | Claim | Evidence relationship |
|---|---|---|
| CLM-01 | A vulnerability has been reported in ExampleLib | EVD-01 supports; EVD-02 and EVD-03 contextualise but do not independently corroborate |
| CLM-02 | The deployed version is within the affected range | EVD-01 initially supports; EVD-04 qualifies or may contradict depending on the deployed version |
| CLM-03 | The release should be blocked pending verification | This is a decision recommendation, not a source observation; it requires explicit objectives, constraints, and authorization |

Each relationship should include a rationale and the relevant passage or structured field. The system must not turn the recommendation in CLM-03 into an observed fact.

### 4.4 Uncertainty register

| Uncertainty ID | Dimension | Affected object | Rationale | Resolution condition |
|---|---|---|---|---|
| UNC-01 | Source | EVD-01 | Authenticity not yet verified | Verify origin and integrity |
| UNC-02 | Independence | CLM-01 | EVD-02 and EVD-03 share an upstream origin | Preserve lineage; obtain genuinely independent evidence if needed |
| UNC-03 | Temporal | CLM-02 | EVD-04 may supersede the original affected-version statement | Check publication, validity, and version scope |
| UNC-04 | Interpretive | CLM-02 | Deployed version and affected range may use different version semantics | Verify exact deployed build and maintainer interpretation |

These entries are not interchangeable with model confidence. A model may be highly confident while UNC-01 or UNC-03 remains unresolved.

### 4.5 Review-state progression

A possible state progression is:

| Event | State | Reason |
|---|---|---|
| Initial claim drafted | Draft | No evidence assessment completed |
| Evidence links created | Evidence-linked | Claims now have traceable evidence associations |
| Origin and version checks requested | Review-required | Integrity, independence, and temporal questions remain |
| Maintainer update assessed | Qualified | Affected range is narrowed; residual uncertainty remains |
| Release decision authorised | Approved or rejected for the defined action | Authorization applies only to the specific decision and evidence snapshot |

The final state must not be read as a universal declaration that the underlying claim is true. Approval is scoped to a particular output, version, decision, and authority.

### 4.6 Qualitative VOI example

Suppose the team can take one of three actions:

- **Action A:** verify the deployed library version against the maintainer update.
- **Action B:** acquire another news summary that repeats the same upstream advisory.
- **Action C:** request a direct clarification from the maintainer about the version boundary.

A qualitative prioritisation record might be:

| Action | Expected decision relevance | Independence / information gain | Cost and delay | Initial disposition |
|---|---|---|---|---|
| A | High: resolves whether the deployment is in scope | High for the version uncertainty | Low | Prioritise |
| B | Low: likely repeats known material | Low; shared origin | Low | Deprioritise |
| C | Potentially high: may resolve interpretation | Potentially high; depends on response | Medium / uncertain delay | Consider if A does not resolve the issue |

This is an illustrative ranking, not a measured VOI result. No numeric benefit is assigned because the scenario supplies no calibrated probabilities or defensible utility values. Mandatory review and security controls remain in force regardless of this ranking.

### 4.7 Evidence-graph fragment

A minimal relationship fragment can be represented as:

```text
SRC-01 ──ORIGINATES──> EVD-01 ──SUPPORTS──> CLM-01
   │
   ├──DERIVED-INTO──> SRC-02 ──ORIGINATES──> EVD-02
   │                                      └──SAME_ORIGIN_AS── EVD-01
   │
   └──DERIVED-INTO──> SRC-03 ──ORIGINATES──> EVD-03
                                          └──SAME_ORIGIN_AS── EVD-01

SRC-04 ──ORIGINATES──> EVD-04 ──QUALIFIES──> CLM-02
EVD-01 ──SUPPORTS (initially)──> CLM-02
EVD-04 ──SUPERSEDES / QUALIFIES (as applicable)──> prior assessment
CLM-01 ──INFORMS──> DEC-01
CLM-02 ──INFORMS──> DEC-01
DEC-01 ──REQUIRES──> REV-01
```

The exact edge vocabulary and cardinality rules belong in the versioned graph schema. The diagram is conceptual and does not claim that these identifiers or relationships are already implemented in the public benchmark.

### 4.8 Revision and downstream impact

When EVD-04 is verified, the system should not overwrite EVD-01 or delete the earlier assessment. It should:

1. Register EVD-04 with its own source, acquisition, publication, and validity metadata.
2. Create a new version of the affected claim assessment.
3. Record whether EVD-04 qualifies, contradicts, or supersedes part of the prior assessment.
4. Identify decisions that depended on the prior version.
5. Determine whether those decisions require review, notification, or no action, with rationale.
6. Preserve the original decision record and the later reassessment event.

If the prior release decision relied on a now-superseded version range, the decision is not silently rewritten. Its historical basis remains reconstructable, while its current validity is reassessed.

### 4.9 Memory admission boundary

The incident report, extracted evidence, claim assessment, and final decision are different record types. A future adaptive system must not automatically promote its own generated summary or prior decision into independent evidence.

A candidate memory should retain provenance, scope, confidence limitations, source dependence, validity conditions, and a route for supersession. If admission criteria are unmet, the item may remain retrievable as untrusted or provisional context without being treated as an accepted belief.

## 5. Mapping KSEL to common agent and RAG components

KSEL is a governance layer, not a replacement for retrieval, model reasoning, tool orchestration, or memory storage.

| Common component | What it ordinarily provides | KSEL relationship | Boundary to preserve |
|---|---|---|---|
| Retrieved chunk | A text segment returned by retrieval | May be registered as evidence or a candidate evidence object | Retrieval does not establish source validity or claim support |
| Tool result | Output returned by an external tool or API | May become an evidence object with tool, time, parameters, and transformation provenance | Tool execution success does not establish correctness |
| Model-generated claim | A proposition expressed by a model | Registered as a claim if material and reviewable | A claim is not evidence merely because a model generated it |
| Intermediate reasoning trace | Internal or external process representation | May inform an audit design where available and appropriate | KSEL does not require disclosure of private chain-of-thought; record observable claims, evidence links, transformations, and decision rationales |
| Model confidence or log probability | Model-specific signal about token or output likelihood | May be recorded as a model assessment attribute | It is not source quality, evidence strength, or calibrated real-world probability by default |
| Vector or document store | Storage and retrieval of content | May store evidence payloads or references | Storage and retrieval do not provide review state or provenance governance automatically |
| Tool-call gate / human interrupt | Controls whether an action may execute | May implement or enforce a KSEL review requirement | The gate should consume explicit policy and review records; a pause alone is not an auditable review |
| Agent memory store | Persists information across sessions | May store references to governed KSEL records or approved memory candidates | Persistence is not admission, validation, independence, or belief revision |
| Event / telemetry log | Records system activity | May supply audit events | Operational logs are not necessarily complete, immutable, semantically typed, or sufficient for decision reconstruction |

### 5.1 Integration principle

Existing components may remain unchanged where they already meet the required contract. KSEL should add the minimum records and controls needed to make evidence and decisions inspectable. Avoid duplicating large source payloads when a stable, access-controlled reference and integrity metadata are sufficient.

### 5.2 Security boundary

Retrieved content, tool outputs, and user-supplied documents must be treated as data, not as trusted instructions. Prompt-injection handling belongs at the system's instruction/data boundary and should be tested separately from the correctness of evidence extraction. A source may be authentic while containing malicious or irrelevant instructions.

## 6. Minimum record contracts

This section gives conceptual minimum fields, not a final JSON Schema. Field names, types, requiredness, validation rules, and compatibility guarantees must be specified in a later versioned schema package.

### 6.1 Claim record

- Stable claim identifier.
- Claim text or structured proposition.
- Claim type: observation, factual assertion, inference, prediction, or recommendation.
- Scope: subject, population, time, context, and relevant conditions.
- Current assessment version.
- Linked evidence and relationship rationales.
- Uncertainty references.
- Current review state.
- Creation and revision events.

### 6.2 Evidence record

- Stable evidence identifier and version.
- Source identifier and origin locator.
- Content reference or protected payload.
- Acquisition and available source-time metadata.
- Integrity metadata where applicable.
- Transformation history.
- Known source lineage and dependencies.
- Relevance and admissibility assessments.
- Limitations and access/retention constraints.

### 6.3 Uncertainty record

- Stable uncertainty identifier.
- Dimension and affected object references.
- Description and basis.
- Qualitative level or numeric estimate with method, if justified.
- Consequence if unresolved.
- Resolution or reassessment condition.
- Status and change history.

### 6.4 Review record

- Stable review identifier and target version.
- Review requirement and triggering condition.
- Reviewer or process identity and authority scope.
- Checks performed and their results.
- Decision: approve, reject, qualify, defer, or escalate.
- Rationale, timestamp, and referenced evidence snapshot.
- Expiry or reassessment trigger where applicable.

### 6.5 Audit event

- Event identifier and event type.
- Actor or process identity.
- Target object and version.
- Prior and resulting state, where relevant.
- Event time and record time.
- Reason or triggering condition.
- References to related review, decision, or evidence records.

Audit design must balance reproducibility with data minimisation, privacy, security, and retention requirements. Append-oriented does not mean every payload must be retained forever.

## 7. Conformance research and profile checks

A future implementation may publish a self-assessment against a declared profile. This is a research aid, not certification.

For each claimed capability, publish:

- profile and version;
- implementation version and deployment scope;
- required input and output records;
- validation and failure behaviour;
- tests and test results;
- known limitations and unsupported cases;
- security, privacy, and retention assumptions;
- evidence supporting the maturity label.

A capability should be marked **not implemented**, **partially implemented**, **implemented but not evaluated**, or **evaluated under stated conditions** as appropriate. Do not use a single aggregate badge to conceal missing mandatory capabilities.

## 8. Implementation-to-evaluation traceability

RN-008 defines the experimental programme. The current public benchmark starter kit provides a small synthetic development fixture and deterministic evaluator. It is not a confirmatory benchmark and does not evaluate every profile capability.

The following mapping connects the implementation profiles to existing evaluation work:

| Capability | RN-008 evaluation area | Current starter-kit coverage |
|---|---|---|
| Claim-evidence traceability | H1 / traceability metrics | Partial structural coverage |
| Provenance and admissibility | H2 / invalid-evidence detection | Partial synthetic coverage |
| Source dependence | H3 / false-corroboration rate | Partial synthetic coverage |
| Temporal validity | H4 / stale-evidence detection | Partial synthetic coverage |
| Uncertainty and contradiction | H5 / contradiction preservation and uncertainty outcomes | Partial; no full calibration assessment |
| Review and authorization | H6 / review compliance | Partial structural coverage |
| VOI and review cost | H7 / quality-cost, effort, and delay | Not measured by the current starter evaluator |
| Integrated profile effects | H8 / integrated treatment | Not established by the current development fixture |

The starter kit's 12 fictional cases are useful for evaluator development and smoke testing. They are not a blind test set, representative sample, or basis for general performance claims.

### 8.1 Suggested implementation sequence

1. **Contract validation:** validate identifiers, references, required fields, and state-transition rules.
2. **Profile A prototype:** implement records, relationships, uncertainty, review states, and audit events.
3. **Worked-case replay:** reproduce the fictional ExampleLib scenario and verify that each state and relationship is inspectable.
4. **Profile A tests:** test missing provenance, unsupported claims, unresolved contradictions, invalid state transitions, and audit reconstruction.
5. **Profile B extension:** add candidate evidence actions, qualitative VOI, constraints, and review-tier selection.
6. **Profile C extension:** add typed dependency links, versioning, temporal metadata, and change-impact queries.
7. **RN-008 evaluation preparation:** define and version baselines, adapters, expanded data, annotation procedures, resource budgets, and analysis plans before confirmatory experiments.

Passing contract tests demonstrates that specified behaviour exists in the tested implementation. It does not demonstrate that the architecture improves real-world decisions.

### 8.2 Additional evaluation tasks to consider

The following tasks may extend RN-008 in later versions:

- **Decision impact query:** given a superseded evidence version, identify all dependent claims and decisions.
- **Source-lineage challenge:** detect when multiple reports share an upstream origin.
- **Revision reconstruction:** reproduce the evidence and review state used for a prior decision.
- **Memory contamination probe:** detect when a system's own earlier output is reintroduced as independent evidence.
- **Review-state attack:** attempt unauthorised transitions from review-required to approved.
- **Cost-aware prioritisation:** compare qualitative action rankings against an independently adjudicated task-specific priority rubric.

Operational definitions, gold labels, expected failure modes, and scoring rules must be published before these tasks are used for confirmatory claims.

## 9. Limitations and unresolved design questions

### 9.1 First-implementation blockers

These should be resolved before describing a Profile A prototype as meaningfully testable:

- A versioned record contract for sources, evidence, claims, uncertainty, reviews, and audit events.
- Defined review-state transition rules and authority boundaries.
- A stable identifier and versioning strategy.
- A clear policy for missing, inaccessible, or unverifiable evidence.
- A reproducible method to reconstruct the evidence snapshot associated with a released claim.

### 9.2 Later research questions

These may be investigated after a minimal implementation exists:

- Domain-specific evidence-quality assessment without universal scoring.
- Reliable detection of correlated and shared-origin sources.
- Quantitative VOI estimation under sparse or delayed outcomes.
- Graph storage, query performance, archival, and retention at scale.
- Human-review agreement and reviewer fatigue.
- Rollback when downstream decisions have already been acted upon.
- Interactions among model updates, retrieval changes, memory systems, and policy changes.

### 9.3 Risks of false assurance

A structured record can be incomplete, incorrectly populated, or based on weak evidence. A review state can be misunderstood as proof of truth. A graph can faithfully preserve incorrect relationships. A deterministic evaluator can reward conformity to flawed annotations. Implementations must communicate these limitations and preserve the ability to challenge records.

## 10. Governance and versioning

This companion is additive to RN-001 through RN-008. It does not silently amend their claims or convert proposed mechanisms into implemented capabilities.

Changes to profile requirements, record contracts, worked examples, or evaluation mappings should be versioned and documented. If a later implementation reveals that a research proposal is infeasible or incomplete, publish the limitation and update the relevant artefact through the repository's normal review process.

Any implementation claiming alignment with this companion should identify the exact version and list deviations.

## 11. Conclusion

The KSEL research series proposes a broad evidence-governance architecture. This companion provides an incremental path for testing its operational form: begin with traceable claims, evidence, uncertainty, review, and audit records; add cost-aware evidence selection; then add typed versioned dependencies and temporal impact analysis.

The central implementation test is practical: can an independent reviewer reconstruct what was claimed, which evidence was used, what remained uncertain, which controls were applied, who or what authorised the decision, and what changed afterward?

That question can be tested without claiming that KSEL is already validated. The next scientific contribution should come from transparent implementation, controlled comparison, and independent scrutiny.

---

## Publication and research integrity statement

This document is a proposed implementation companion. The worked example is fictional. The profiles are research implementation scopes, not certified standards. No production readiness, empirical effectiveness, benchmark superiority, or independent replication is claimed. Any future implementation or evaluation should publish its version, methods, limitations, and supporting artefacts.

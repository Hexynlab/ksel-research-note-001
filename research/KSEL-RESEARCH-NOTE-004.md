# KSEL Research Note 004
## Evidence Graphs, Knowledge Representation, and Cross-Source Reasoning

**Publication series:** H3XYN LAB — Technical Research Notes  
**Document identifier:** KSEL-RN-004  
**Version:** 0.1.0  
**Status:** Preliminary research framework  
**Date:** 22 November 2026  
**Maintained by:** H3XYN LAB  
**Research area:** Knowledge representation, evidence graphs, provenance-aware reasoning, uncertainty propagation, intelligent-system governance

---

## Abstract

Evidence governance becomes difficult to operate when claims, sources, observations, transformations, uncertainties, contradictions, and decisions are stored as disconnected records. A system may preserve each item individually yet fail to represent how they depend on one another. This makes it difficult to trace a conclusion to its supporting evidence, identify shared source origins, determine which decisions are affected by a correction, or explain how uncertainty propagates through a chain of inference.

This note proposes an evidence-graph architecture for KSEL. It represents evidence objects, sources, claims, observations, transformations, methods, uncertainty assessments, review events, and decisions as typed, versioned entities connected by explicit relationships. The graph is intended to make evidence lineage queryable, preserve disagreement, distinguish direct observations from derived claims, and support bounded cross-source reasoning.

The proposal defines a graph model, relationship vocabulary, temporal and version semantics, claim-support structures, uncertainty representation, contradiction handling, reasoning boundaries, query patterns, governance controls, and an evaluation programme. It emphasizes that graph connectivity is not proof, edge existence is not truth, and automated inference must not silently convert association into causation or corroboration into certainty.

Four earlier notes establish the research context: evidence governance (RN-001), cost-aware evidence selection (RN-002), and evidence integrity and adversarial resilience (RN-003). RN-004 proposes the representational layer through which those controls can work together.

The architecture and hypotheses are preliminary. No implementation performance, validated ontology, or experimental result is claimed.

**Keywords:** evidence graph; knowledge graph; provenance; claim graph; uncertainty propagation; cross-source reasoning; temporal data; graph governance; intelligent systems

---

## 1. Introduction

An evidence-governance system must preserve more than documents and citations. It must preserve the relationships that explain why a claim is supported, which source produced an observation, how a record was transformed, what assumptions were introduced, which sources share an origin, and which decisions relied on the resulting conclusion.

A conventional document store can retain all the relevant files while leaving these relationships implicit. That creates several operational weaknesses:

- A reviewer must reconstruct the evidence chain manually.
- A correction to one source may not identify all dependent claims and outputs.
- Repeated copies of one source may be mistaken for independent corroboration.
- Conflicting claims may be overwritten or hidden by a latest-value representation.
- Derived claims may become detached from the assumptions and methods that produced them.
- Uncertainty may be recorded at the output level without indicating which evidence or inference contributes to it.

A graph representation offers a way to make these relationships explicit and inspectable. However, a graph can also create false confidence. A connected graph is not necessarily complete, accurate, unbiased, or causally meaningful. Its value depends on the quality of its entity definitions, relationship semantics, provenance, temporal handling, and governance.

### 1.1 Research question

How can KSEL represent evidence and its dependencies as a typed, versioned graph that supports traceability and cross-source reasoning without confusing association, support, independence, causality, or truth?

### 1.2 Intended contribution

This note proposes:

1. A typed evidence-graph model and core entity vocabulary.
2. Explicit relationships for provenance, support, contradiction, derivation, and decision reliance.
3. Versioned and temporal graph semantics.
4. Claim-centred support and challenge structures.
5. A representation for uncertainty and inference assumptions.
6. Bounded cross-source reasoning and graph-query patterns.
7. Change-impact analysis and governance controls.
8. Testable hypotheses and an empirical evaluation programme.

The model is a proposed starting point. Domain-specific deployments will require controlled vocabularies, validation rules, and specialist review.

## 2. Position within the KSEL research series

The four notes describe complementary parts of a proposed architecture.

| Note | Research contribution | Primary architectural concern |
|---|---|---|
| RN-001 | Evidence governance, uncertainty, and review controls | Governance lifecycle |
| RN-002 | Cost-aware evidence selection and adaptive review | Resource allocation and review decisions |
| RN-003 | Evidence integrity, provenance verification, and adversarial resilience | Trust boundaries and integrity |
| RN-004 | Evidence graphs and cross-source reasoning | Representation and relationship structure |

RN-004 does not replace the evidence records, integrity checks, or review requirements defined in the earlier notes. It provides a proposed connected representation for those objects and events.

The graph should preserve links to original records rather than become an untraceable substitute for them. Where the source is stored externally, the graph should retain a stable identifier, controlled locator, version, access policy, and integrity reference as appropriate.

## 3. Design principles

The following principles guide the proposed model.

### 3.1 Explicit semantics

Every node and edge should have a defined meaning. A generic relationship such as `related_to` may be useful for exploration but is insufficient for consequential reasoning unless its semantics are specified.

### 3.2 Provenance by construction

A derived claim should link to the evidence, methods, assumptions, and transformations from which it was produced. Provenance should not be added only after a dispute occurs.

### 3.3 Preserve disagreement

Contradictory claims and evidence should coexist in the graph. The graph should represent the nature, scope, and status of the disagreement rather than force premature resolution.

### 3.4 Separate observation, interpretation, and decision

An observation is not the same as a claim. A claim is not the same as an inference. An inference is not the same as an approved decision. The model must preserve these distinctions.

### 3.5 Time and version matter

Evidence and claims are valid only within stated contexts and time scopes. Corrections should create new versions and explicit supersession relationships, not silently rewrite historical records.

### 3.6 Uncertainty remains visible

Uncertainty should attach to the objects and inference steps where it arises. A single confidence value on a final answer is not an adequate representation of the uncertainty structure.

### 3.7 Graph structure does not establish truth

A graph can organize assertions and dependencies. It cannot guarantee that a source is truthful, that a relationship is correctly classified, or that an inference is valid.

### 3.8 Governance is part of the model

Access control, review authority, retention, policy constraints, and approval events must be represented or linked. They cannot be treated as optional interface metadata.

## 4. Proposed graph architecture

### 4.1 Graph definition

For the purposes of this note, an evidence graph is a typed, directed, version-aware graph:

[
G = (V, E, 	au_V, 	au_E, A, T, P)
]

where:

- (V) is the set of graph nodes.
- (E) is the set of directed relationships between nodes.
- (	au_V) assigns a node type.
- (	au_E) assigns a relationship type.
- (A) contains node and relationship attributes.
- (T) contains temporal and version information.
- (P) contains provenance and policy references.

This is a conceptual schema, not a claim that one graph database or serialization format is required.

### 4.2 Core node types

| Node type | Meaning | Illustrative attributes |
|---|---|---|
| Source | Origin or publisher associated with information | Identity, authority, jurisdiction, verification state |
| EvidenceObject | A document, dataset, image, recording, record, or other evidence item | ID, version, digest, media type, access class |
| Observation | A recorded measurement or directly reported observation | Subject, value, unit, method, time, conditions |
| Claim | A proposition that may be supported, challenged, or qualified | Text, scope, polarity, status, owner |
| Entity | A person, organization, asset, place, event, or concept | Type, stable identifiers, identity status |
| Method | A process used to collect, verify, or analyze information | Description, version, limitations |
| Transformation | A conversion or derivation applied to evidence | Inputs, outputs, tool, parameters, time |
| Inference | A reasoned step connecting premises to a conclusion | Rule, premises, assumptions, result |
| UncertaintyAssessment | A structured record of unresolved uncertainty | Dimension, range, basis, impact, assessor |
| Review | A human or automated review event | Reviewer, scope, outcome, rationale |
| Decision | An action, approval, rejection, or disposition | Authority, context, status, time |
| Policy | A rule or constraint governing handling or use | Scope, version, owner, effective period |
| Event | A recorded lifecycle or custody event | Actor, action, time, object, result |

A deployment may add domain-specific types. Extensions should preserve stable identifiers and explicit type definitions.

### 4.3 Relationship vocabulary

| Relationship | Directional meaning |
|---|---|
| `PUBLISHED_BY` | EvidenceObject → Source |
| `ACQUIRED_FROM` | EvidenceObject → Source |
| `DERIVED_FROM` | EvidenceObject or Claim → input object |
| `TRANSFORMED_BY` | EvidenceObject → Transformation |
| `PRODUCED` | Transformation or Method → output object |
| `REPORTS` | EvidenceObject → Observation or Claim |
| `ASSERTS` | Source → Claim |
| `SUPPORTS` | EvidenceObject, Observation, or Claim → Claim |
| `CHALLENGES` | EvidenceObject, Observation, or Claim → Claim |
| `QUALIFIES` | Claim or EvidenceObject → Claim |
| `DEPENDS_ON` | Claim or Inference → premise, method, or assumption |
| `CONTRADICTS` | Claim ↔ Claim, with scope and basis |
| `CORROBORATES` | EvidenceObject or Observation → claim or observation, subject to independence assessment |
| `SUPERSEDES` | New version or record → prior version or record |
| `REVIEWED_BY` | Claim, EvidenceObject, or Decision → Review |
| `AUTHORIZED_BY` | Decision or action → authority or policy |
| `RELIED_UPON_BY` | Claim or EvidenceObject → Decision |
| `AFFECTS` | Event or changed object → dependent object |
| `SAME_ORIGIN_AS` | EvidenceObject → evidence object, with confidence and basis |
| `HAS_UNCERTAINTY` | Node or relationship → UncertaintyAssessment |

Relationship names should be treated as typed predicates with documented domain, range, cardinality, and constraints. They are not interchangeable.

### 4.4 Edge attributes

An edge may need its own metadata, especially when it represents a judgement rather than a simple structural link.

Recommended attributes include:
- Relationship identifier.
- Relationship type and schema version.
- Assertion status: asserted, assessed, verified, disputed, or withdrawn.
- Actor or process that created the relationship.
- Creation and effective times.
- Supporting method or evidence.
- Scope and conditions.
- Confidence or uncertainty representation, if justified.
- Review status and policy reference.
- Supersession or correction linkage.

For example, `SUPPORTS` should not be a bare connection if the support relationship depends on a specific interpretation, method, or scope. The graph should preserve the rationale and its provenance.

## 5. Claim-centred representation

### 5.1 Claims as first-class objects

A claim should have a stable identifier, a carefully bounded proposition, subject, predicate, object where applicable, scope, relevant time interval, source language or formulation, and status.

A natural-language claim can be retained for readability, while structured fields support validation and query. The structured representation must not be treated as a lossless replacement for the original wording.

### 5.2 Atomicity and decomposition

Compound claims should be decomposed where doing so improves verification. For example, a statement that an organization acquired an asset in a particular year and deployed it in a particular location contains multiple propositions.

Decomposition should preserve the original compound statement and its relationship to the component claims. Otherwise, a system may incorrectly imply that all components were independently verified.

### 5.3 Support is scoped

An evidence item may support one part of a claim while failing to support another. A source can confirm that an announcement was made without confirming that the announced event occurred.

The graph should distinguish:
- Evidence that a statement was published.
- Evidence that an event occurred.
- Evidence that a particular actor caused the event.
- Evidence that the event had a stated consequence.

Support edges must identify the proposition and scope they address.

### 5.4 Claim status

Possible claim states include:
- Proposed.
- Supported within stated scope.
- Partially supported.
- Challenged.
- Contradicted.
- Unresolved.
- Withdrawn.
- Superseded.

These are governance states, not universal truth values. A deployment must define transitions and approval authority.

## 6. Provenance and source dependency graph

### 6.1 Provenance paths

A claim's provenance path should be traversable from the claim through inference and transformation steps to the underlying evidence objects and sources.

A minimal path might be:

[
	ext{Decision}
leftarrow 	ext{Claim}
leftarrow 	ext{Inference}
leftarrow 	ext{Observation}
leftarrow 	ext{EvidenceObject}
leftarrow 	ext{Source}
]

Real cases may contain multiple premises, derived datasets, transformations, and reviewers. The model should retain each material branch.

### 6.2 Shared-origin detection

A graph should record known or suspected shared origins. If several sources copy one original report, the dependency structure should make that visible.

The absence of a `SAME_ORIGIN_AS` edge does not prove independence. The graph should support states such as confirmed shared origin, suspected dependency, assessed independent, and unknown dependency.

### 6.3 Independence is claim-specific

Two sources may be independent for one claim but dependent for another. Independence can depend on the collection method, underlying dataset, witness, ownership, incentives, or transmission chain.

Therefore, source independence should be assessed in relation to a defined claim and purpose, not assigned as a permanent universal property of a publisher.

### 6.4 Avoiding evidence multiplication

A reasoning engine must not treat the number of graph nodes as the number of independent confirmations. Multiple copies, translations, summaries, and reposts may be one evidence lineage.

Any aggregation of corroboration should account for common origins, shared methods, and unknown dependencies. If independence cannot be assessed, the system should preserve that uncertainty rather than assume independence.

## 7. Temporal and version semantics

### 7.1 Multiple notions of time

Evidence graphs often need to distinguish:
- **Event time:** When the described event occurred.
- **Source time:** When the source claims the information was created or published.
- **Acquisition time:** When the system obtained the evidence.
- **Processing time:** When a transformation or analysis occurred.
- **Effective time:** When a fact or policy applies.
- **Record time:** When the graph recorded the assertion.

These times may differ. A system should not silently substitute acquisition time for event time or treat a source-claimed timestamp as independently verified.

### 7.2 Valid time and transaction time

A bitemporal approach may be useful:
- Valid time describes when a fact is asserted to apply in the represented world.
- Transaction time describes when the system stored or changed the record.

This allows a system to answer both “What do we currently believe applied at that time?” and “What had the system recorded at the time of the earlier decision?”

### 7.3 Versioning and correction

Corrections should create new versions or assertions linked through `SUPERSEDES`, with reason, actor, and time. Historical decisions should remain linked to the exact versions they used.

A current graph view may hide superseded records by default, but audit and reconstruction views must be able to recover them.

### 7.4 Temporal uncertainty

When an event time is approximate, disputed, or bounded, the graph should store an interval or qualified temporal expression rather than inventing a precise timestamp.

## 8. Uncertainty and inference representation

### 8.1 Uncertainty belongs to the reasoning chain

Uncertainty may arise from source authenticity, measurement error, missing context, transformation loss, model interpretation, conflicting reports, unknown dependencies, or assumptions.

The graph should attach uncertainty assessments to the relevant node, edge, method, or inference. A final claim may summarize these uncertainties, but it should remain possible to inspect their origin.

### 8.2 Dimensions of uncertainty

A proposed uncertainty record may include:
- Type or dimension.
- Affected node or relationship.
- Description and scope.
- Evidence basis.
- Assessment method.
- Qualitative category or calibrated quantitative representation.
- Impact on the claim or decision.
- Assumptions and dependencies.
- Assessor and review state.
- Reassessment trigger.

A numerical probability should be used only when the event space, estimation method, and calibration basis are defensible. Otherwise, qualitative uncertainty with explicit rationale is preferable.

### 8.3 Avoid naive propagation

Uncertainty cannot generally be propagated by averaging confidence labels or multiplying arbitrary source scores. Dependencies, shared origins, conditional assumptions, and model misspecification matter.

A formal probabilistic model may be appropriate for some domains, but its assumptions must be explicit and validated. In other contexts, a structured argument graph or qualitative dependency analysis may be more defensible.

### 8.4 Inference records

Each material inference should record:
- Premise identifiers and exact versions.
- Rule, method, model, or procedure used.
- Assumptions and boundary conditions.
- Output claim and scope.
- Known alternatives or counterarguments.
- Uncertainty and limitations.
- Execution or assessment metadata.
- Reviewer and approval state where required.

A model-generated inference should identify the model and relevant configuration where available. The existence of a model output does not establish that the inference is valid.

## 9. Contradiction and competing explanations

### 9.1 Contradictions are graph objects, not data errors to erase

Two claims may contradict each other because one is false, because they refer to different time periods or definitions, because the evidence is incomplete, or because both are partially correct under different conditions.

The graph should preserve the claims and record the basis for the contradiction relationship.

### 9.2 Contradiction assessment

A contradiction assessment should consider:
- Whether the claims refer to the same subject and proposition.
- Whether their time and scope overlap.
- Whether terms and units are compatible.
- Whether sources share an origin.
- Whether one claim is a correction or supersession rather than a true contradiction.
- Whether the disagreement can be resolved with additional evidence.
- Whether a qualified conclusion is possible.

### 9.3 Competing hypotheses

For complex questions, the graph may represent multiple competing hypotheses and the evidence relevant to each. It should not force a single conclusion where evidence remains insufficient.

The system may identify what additional observation would discriminate between hypotheses. This links graph reasoning to the cost-aware evidence-action process in RN-002.

## 10. Cross-source reasoning

### 10.1 Reasoning pipeline

A proposed KSEL reasoning pipeline is:

1. Define the decision or question.
2. Identify material claims and scope.
3. Retrieve relevant evidence and graph neighborhoods.
4. Validate identity, integrity, provenance, and access constraints.
5. Expand source dependencies and transformation lineage.
6. Identify supporting, challenging, and qualifying evidence.
7. Assess temporal compatibility and contextual relevance.
8. Identify unresolved contradictions and uncertainty.
9. Apply explicit inference methods within their declared scope.
10. Produce a traceable conclusion or a justified unresolved state.
11. Record the exact graph snapshot and evidence versions used.
12. Trigger review or reassessment when required.

Each stage should produce inspectable events and should be capable of stopping or escalating when a mandatory condition fails.

### 10.2 Bounded traversal

Unrestricted graph traversal can produce irrelevant, stale, or adversarial context. Querying should be bounded by claim scope, time range, source policy, relationship types, graph depth, access permissions, and resource budget.

A traversal limit is an operational constraint, not proof that omitted evidence is irrelevant. The system should disclose material search boundaries where they affect interpretation.

### 10.3 Evidence paths and argument paths

An evidence path traces the origin and handling of information. An argument path traces how premises support or challenge a conclusion. They are related but not identical.

A system should be able to display both:
- **Evidence path:** source → object → transformation → observation.
- **Argument path:** observation → premise → inference → claim → decision.

Combining them into one opaque chain can obscure where a source fact ends and a system inference begins.

### 10.4 Explainability requirements

A graph-backed answer should be able to identify:
- The claims it makes.
- The evidence objects and versions relied upon.
- The relevant provenance and transformations.
- The support and challenge relationships.
- The material assumptions.
- The unresolved uncertainty.
- The graph scope and retrieval boundaries.
- The review or approval status.

An explanation should not imply that every graph relationship was independently verified. It should label asserted, inferred, and reviewed relationships distinctly.

## 11. Illustrative graph queries

The following examples describe query intent rather than prescribe a specific graph query language or database.

### 11.1 Trace a decision to original sources

Starting from a decision node, traverse `RELIED_UPON_BY` in reverse to claims, then through `DEPENDS_ON`, `SUPPORTS`, `DERIVED_FROM`, and provenance relationships to original evidence objects and sources.

Expected output: a version-aware path with transformations, uncertainty, and review state.

### 11.2 Find decisions affected by a corrected source

Starting from a corrected or superseded evidence object, traverse downstream through derived objects, observations, claims, inferences, and decisions.

Expected output: all known dependent records, their versions, and reassessment status.

### 11.3 Detect apparent corroboration with shared origin

For a claim, collect evidence objects connected by `SUPPORTS` or `CORROBORATES`, then inspect source and lineage dependencies.

Expected output: clusters of common-origin evidence, unknown dependencies, and independently assessed evidence paths.

### 11.4 Retrieve unresolved contradictions

Find claim pairs connected by `CONTRADICTS` where the assessment status is unresolved and the claims overlap in subject, time, and scope.

Expected output: competing claims, supporting evidence, known limitations, and the authority responsible for resolution.

### 11.5 Identify unsupported material claims

For a decision, traverse its material claims and identify those without adequate support relationships or with only unverified, stale, or out-of-scope evidence.

Expected output: claims requiring qualification, additional evidence, review, or rejection.

These queries should return the reasoning path and relevant limitations, not merely a count or ranking.

## 12. Governance, security, and operational controls

### 12.1 Graph integrity

Graph nodes and edges are records and require the same integrity controls as evidence objects. The system should preserve actor identity, schema version, timestamps, change history, and authorization context.

A relationship must not be silently changed from `CHALLENGES` to `SUPPORTS` without a traceable correction event.

### 12.2 Access control

Access may need to apply at node, edge, attribute, or subgraph level. A user authorized to see a claim may not be authorized to access the underlying personal data or confidential source.

Query results must not leak restricted information through relationship counts, identifiers, summaries, or inferred existence.

### 12.3 Schema governance

The ontology and relationship vocabulary should be versioned. Schema changes require migration rules, compatibility assessment, and documentation of changed semantics.

A new relationship type should not be introduced solely because it is convenient for one query. Its definition, domain, range, and governance implications should be reviewed.

### 12.4 Graph poisoning and adversarial records

An attacker may insert false nodes, misleading relationships, duplicated identities, or hostile metadata. Graph ingestion should validate schemas, authenticate authorized writers, isolate untrusted assertions, and preserve provenance for every relationship.

Automated entity resolution should not merge identities solely because names or descriptions are similar. Ambiguous matches should remain separate or be marked as unresolved.

### 12.5 Human oversight

High-consequence conclusions require appropriate human or institutional authority. Graph-derived rankings and inferred relationships should not be treated as self-authorizing decisions.

Reviewers should be able to inspect the evidence path, challenge an edge, request a correction, and record a reasoned disposition.

### 12.6 Retention and deletion

Graph relationships can retain information about deleted or restricted source material. Retention policies must cover nodes, edges, indexes, backups, derived objects, and audit records. Legal and privacy requirements may require controlled deletion, redaction, or restricted tombstones rather than unrestricted permanent retention.

## 13. Proposed reference architecture

A conceptual implementation may contain the following components:

| Component | Responsibility |
|---|---|
| Ingestion gateway | Accepts evidence and validates authorization and format |
| Evidence registry | Stores object identity, versions, references, and integrity metadata |
| Provenance service | Records source lineage, custody, and transformations |
| Graph store | Stores typed entities and relationships |
| Schema registry | Defines node, edge, and attribute semantics |
| Identity resolution service | Links entities while preserving ambiguity and match evidence |
| Reasoning service | Executes bounded, policy-aware graph reasoning |
| Uncertainty service | Stores assessments and inference limitations |
| Review workflow | Routes cases to appropriate human or automated review |
| Policy and access layer | Enforces permissions, restrictions, and retention |
| Audit service | Preserves traceable events and graph snapshots |
| Explanation interface | Exposes claims, evidence paths, contradictions, and limitations |

These components may be deployed as separate services or combined in a smaller implementation. The architecture is logical rather than a required microservice topology.

### 13.1 System flow

A typical workflow is:

1. Evidence arrives through an authorized ingestion path.
2. The evidence registry assigns an identifier and version.
3. Integrity and source checks are performed according to policy.
4. Provenance and transformation events are recorded.
5. Entities, observations, and claims are extracted or entered.
6. Candidate relationships are created with their source and status.
7. Validation and review determine which relationships may be relied upon.
8. The reasoning service retrieves a bounded graph view for a defined question.
9. The output records the exact evidence and graph versions used.
10. A later correction or change triggers downstream impact analysis.

### 13.2 Graph snapshot for decisions

A consequential decision should record a reproducible reference to the graph state used at decision time. This may be a versioned snapshot, a set of node and edge versions, or another immutable reference strategy.

The snapshot should include query parameters and relevant policy versions. It should not require exposing restricted evidence to unauthorized readers.

## 14. Evaluation programme

The proposed graph architecture requires testing against realistic evidence tasks and carefully designed adversarial cases.

### 14.1 Falsifiable hypotheses

**H1 — Traceability:** Typed evidence graphs improve the accuracy and speed with which independent reviewers reconstruct the support path for a material decision, compared with disconnected document-and-citation records.

**H2 — Change-impact completeness:** Explicit lineage and dependency relationships increase the proportion of downstream claims and decisions correctly identified after a source correction or withdrawal.

**H3 — Corroboration quality:** Source-dependency representation reduces false independence assessments when multiple evidence objects share an origin.

**H4 — Contradiction preservation:** Explicit competing-claim representation reduces the rate at which material contradictions are omitted or silently overwritten in generated assessments.

**H5 — Reasoning auditability:** Recording premises, methods, assumptions, and graph snapshots increases the proportion of consequential conclusions that can be independently reconstructed.

These hypotheses have not been tested in this publication.

### 14.2 Experimental conditions

A proposed evaluation may compare:

- **Baseline:** Document repository with ordinary citations and manual cross-referencing.
- **Structured records:** Evidence registry with typed claims and provenance metadata, but no graph-based traversal.
- **Evidence graph:** Typed graph with lineage, contradiction, temporal, and decision relationships.
- **Governed graph:** Evidence graph plus access controls, versioned snapshots, uncertainty records, and bounded reasoning.

Tasks should be matched across conditions. Reviewer expertise, evidence availability, time limits, and acceptance criteria should be documented. Where feasible, assignment should be randomized or counterbalanced.

### 14.3 Test corpus

The corpus may include:
- Independent sources supporting the same claim.
- Multiple copies derived from one original source.
- Conflicting records with overlapping and non-overlapping time scopes.
- Corrected and superseded evidence.
- Stale evidence presented as current.
- Derived summaries with transformation errors.
- Ambiguous entity identities.
- Missing provenance links.
- Restricted evidence and access boundaries.
- Adversarially inserted graph relationships.
- Claims that are only partially supported.
- Cases where the correct outcome is unresolved.

Synthetic and authorized data should be used for controlled tests. The corpus should include benign ambiguity as well as deliberate manipulation.

### 14.4 Outcome measures

| Measure | Definition |
|---|---|
| Trace reconstruction accuracy | Proportion of required provenance and argument links correctly identified |
| Trace reconstruction time | Time required for independent reviewers to recover a decision's support path |
| Impact-analysis recall | Proportion of truly affected downstream objects and decisions identified |
| Impact-analysis precision | Proportion of flagged downstream objects that are actually affected |
| False-independence rate | Dependent sources incorrectly treated as independent |
| Contradiction retention | Material conflicts preserved in the final assessment |
| Temporal-scope accuracy | Correct treatment of valid time, record time, and version |
| Unsupported-claim rate | Material claims lacking adequate support under the evaluation rubric |
| Access-control leakage | Restricted information exposed through graph queries or derived outputs |
| Reasoning reproducibility | Proportion of outputs independently reconstructed from recorded graph state |
| Operational overhead | Storage, compute, query latency, and reviewer effort |

Metrics should be reported individually. A composite score could hide a serious privacy or security failure behind improved traceability.

### 14.5 Ablation and stress testing

Ablations should examine typed relationships, source dependency edges, temporal versioning, uncertainty records, graph snapshots, bounded traversal, and access controls.

Stress tests should include high-degree nodes, cyclic relationships, duplicate entities, malformed edges, stale indexes, partial graph outages, contradictory updates, and attempts to infer restricted information through query patterns.

### 14.6 Reproducibility requirements

Evaluation reports should document graph schema and version, ingestion rules, entity-resolution procedures, query definitions, inference methods, task corpus, reviewer rubric, access-control configuration, software versions, and known missing data.

A graph benchmark should publish enough information for independent replication without exposing personal, confidential, or security-sensitive records.

## 15. Limitations and open research questions

The proposed approach has significant limitations:

1. **Ontology design burden:** A poorly designed schema can make the graph inconsistent or difficult to extend.
2. **Entity-resolution errors:** Incorrectly merging or separating entities can distort provenance and reasoning.
3. **Incomplete graph coverage:** Missing edges may create misleading paths or false absence.
4. **Semantic ambiguity:** Different teams may interpret relationship labels differently.
5. **Uncertainty complexity:** Dependencies and conditional uncertainty are difficult to represent with simple scores.
6. **Graph scale and latency:** Large, highly connected graphs can make bounded reasoning expensive.
7. **Access leakage:** Relationship structure itself can reveal sensitive information.
8. **Adversarial graph poisoning:** Malicious nodes and edges may manipulate retrieval and inference.
9. **False explainability:** A visually clear path may still encode invalid assumptions.
10. **Maintenance cost:** Schema governance, review, and correction require sustained operational effort.

Open questions include how to represent uncertainty over relationships, how to reason over incomplete provenance, how to align multiple domain ontologies, how to preserve privacy while enabling audit, and how to measure the quality of a graph explanation rather than its visual complexity.

## 16. Conclusion

An evidence-governance architecture needs a representation that makes relationships among sources, evidence, claims, transformations, uncertainty, review, and decisions explicit.

KSEL Research Note 004 proposes a typed, versioned evidence graph with claim-centred support and challenge relationships, provenance lineage, temporal semantics, uncertainty assessments, contradiction preservation, bounded cross-source reasoning, and change-impact analysis.

The graph is intended to make reasoning inspectable and decisions easier to reconstruct. It is not a truth engine. Its conclusions remain dependent on source quality, relationship validity, inference methods, governance, and the completeness of the represented evidence.

The central principle is:

**A graph can expose how a conclusion is connected to evidence; it cannot make an invalid connection valid merely by representing it.**

The proposed architecture requires implementation, domain-specific schema governance, controlled evaluation, and independent scrutiny before consequential use.

---

## Appendix A — Minimum node record

A generic node record may include:

- Stable node ID.
- Node type and schema version.
- Human-readable label.
- Structured attributes.
- Source or creator reference.
- Creation and record timestamps.
- Valid-time scope where applicable.
- Object or record version.
- Integrity reference where applicable.
- Access classification.
- Review and assertion status.
- Supersession or correction links.

## Appendix B — Minimum relationship record

A generic relationship record may include:

- Stable relationship ID.
- Source node ID and version.
- Target node ID and version.
- Typed predicate.
- Scope and temporal qualifiers.
- Assertion or verification status.
- Creator or asserting process.
- Supporting evidence or method.
- Uncertainty assessment.
- Creation and effective timestamps.
- Policy and access references.
- Correction or supersession history.

## Appendix C — Claim review worksheet

For each material claim, record:
- Exact proposition and scope.
- Subject, predicate, and relevant time.
- Supporting evidence and exact versions.
- Challenging and qualifying evidence.
- Source dependency and independence assessment.
- Transformations and inference methods.
- Assumptions and uncertainty.
- Contradictions and unresolved alternatives.
- Review authority and outcome.
- Decisions that rely on the claim.
- Reassessment triggers.

## Appendix D — Suggested event types

An implementation may record events such as:

- graph_node_created
- graph_relationship_created
- claim_decomposed
- evidence_linked_to_claim
- source_dependency_assessed
- contradiction_recorded
- uncertainty_assessment_added
- entity_match_proposed
- entity_match_confirmed
- entity_match_rejected
- graph_schema_versioned
- graph_snapshot_created
- reasoning_run_completed
- decision_linked_to_graph_snapshot
- source_correction_received
- downstream_impact_analysis_started
- dependent_decision_reopened
- graph_relationship_superseded

Event names are illustrative. Production schemas should define stable identifiers, authenticated actors, timestamps, object versions, authorization context, and integrity protections.

## Appendix E — Terminology

**Evidence graph:** A typed, directed, version-aware graph representing evidence objects and their relationships to sources, claims, transformations, uncertainty, reviews, and decisions.

**Claim:** A bounded proposition that may be supported, challenged, qualified, or left unresolved.

**Evidence lineage:** The traceable relationships describing the origin, custody, copying, and transformation of evidence.

**Argument path:** A structured sequence of premises, methods, assumptions, and inferences leading to a claim or decision.

**Source dependency:** A relationship in which multiple evidence objects derive from or rely on a shared origin, method, dataset, or information path.

**Temporal validity:** The time interval during which a claim or record is asserted to apply.

**Graph snapshot:** A versioned reference to the nodes, relationships, schema, and relevant policy state used for a particular query or decision.

**Graph poisoning:** The insertion or manipulation of graph entities or relationships to distort retrieval, interpretation, or downstream reasoning.

**Bounded traversal:** A graph query constrained by declared scope, relationship types, depth, time, access policy, and resource limits.

---

## Selected references and related work

These works provide background on knowledge-graph representation, provenance, and interoperable graph data. Their existence does not establish that a particular KSEL graph schema is correct or that graph connectivity proves causality.

1. Hogan, A., et al. (2021). Knowledge Graphs. *ACM Computing Surveys, 54*(4), Article 71. https://doi.org/10.1145/3447772 — A broad survey of graph models, query languages, validation, and knowledge representation.
2. Buneman, P., Khanna, S., & Tan, W.-C. (2001). Why and Where: A Characterization of Data Provenance. In *Database Theory — ICDT 2001*, 316–330. https://doi.org/10.1007/3-540-44503-X_20 — Provenance semantics for data derived from source records.
3. W3C. (2013). *PROV-O: The PROV Ontology*. W3C Recommendation. https://www.w3.org/TR/prov-o/ — Interoperable representation of provenance entities, activities, and agents.
4. W3C. (2014). *RDF 1.1 Concepts and Abstract Syntax*. W3C Recommendation. https://www.w3.org/TR/rdf11-concepts/ — Foundational concepts for graph-based data representation.

## Publication and integrity statement

This document presents a preliminary research framework. It does not report completed validation experiments, establish a validated ontology, certify a graph implementation, or claim that graph representation guarantees factual correctness, causal validity, or secure reasoning. All relationship semantics, inference procedures, and access controls require domain-specific specification and testing. Future empirical work should publish methods, schemas, baselines, evaluation criteria, limitations, and reproducibility information sufficient for independent scrutiny.

**Suggested citation**

H3XYN LAB. (2026). *KSEL Research Note 004: Evidence Graphs, Knowledge Representation, and Cross-Source Reasoning* (Version 0.1.0). H3XYN LAB Technical Research Notes. https://github.com/Hexynlab/ksel-research-note-001

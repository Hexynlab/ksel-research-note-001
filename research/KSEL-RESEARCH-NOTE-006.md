# KSEL Research Note 006

## Temporal Intelligence, Evidence Evolution, and Continuous Knowledge Validation

**Series:** KSEL — Knowledge, Source, Evidence Layer  
**Institution:** H3XYN LAB  
**Publication type:** Preliminary research framework  
**Version:** 0.1.0  
**Date:** 22 November 2026  
**Status:** Proposed architecture and research hypotheses; not empirically validated

---

## Abstract

Intelligent systems increasingly depend on information whose validity changes over time. A source may be authentic while its contents become obsolete; a claim may have been well supported at one point but cease to describe the current state; a decision may remain recorded even after the assumptions that justified it have changed. Systems that preserve evidence without modelling its temporal conditions risk treating historical truth as present truth.

This note proposes a temporal intelligence extension to the KSEL evidence-governance architecture. It defines temporal validity as a property that must be assessed separately from provenance, integrity, source reliability, and confidence. It distinguishes event time, observation time, publication time, ingestion time, and assessment time; introduces validity intervals, freshness policies, temporal dependencies, revalidation triggers, and change-impact propagation; and proposes a controlled lifecycle for evidence and derived claims as they evolve.

The framework aims to support systems that can answer not only “What is currently supported?” but also “When was this supported?”, “What changed?”, “Which conclusions depend on the changed information?”, and “What must be reviewed before acting again?” It treats freshness as context-dependent rather than as a universal age threshold. It also distinguishes a source update from a substantive change in the world, and a changed observation from a changed interpretation.

The note defines a proposed temporal evidence model, lifecycle states, validation workflow, architecture, governance controls, evaluation hypotheses, and a reproducibility programme. All components are proposals. No implementation performance, empirical validation, or production deployment is claimed.

**Keywords:** temporal intelligence, evidence evolution, temporal validity, knowledge freshness, continuous validation, evidence provenance, change detection, dependency graphs, reassessment governance, KSEL.

---

## 1. Problem statement

### 1.1 The temporal failure mode

Evidence systems commonly preserve what was observed, where it came from, and how it was interpreted. These are necessary controls, but they do not fully answer whether the information remains suitable for a present task.

Consider five distinct cases:

1. A regulation was accurately recorded but has since been amended.
2. A sensor reading was authentic but described a transient condition that no longer exists.
3. A company report remains unchanged, while the business circumstances it describes have materially changed.
4. A forecast was reasonable at publication time but is now superseded by new observations.
5. A decision was authorised using valid evidence, but a critical assumption later became false.

In each case, the historical record may remain authentic. The problem is not necessarily corruption or source unreliability. It is a mismatch between the temporal scope of the evidence and the temporal scope of the question or decision.

A system that equates “stored”, “verified”, or “previously accepted” with “currently valid” can produce stale conclusions with an appearance of confidence and traceability.

### 1.2 Research question

How should an evidence-governance system represent, detect, evaluate, and respond to temporal change so that claims and decisions remain appropriately grounded in evidence valid for their intended time and context?

### 1.3 Scope

This note addresses temporal semantics for evidence, claims, assumptions, and decisions; distinctions between timestamps and validity intervals; context-sensitive freshness and expiry policies; revalidation triggers and change detection; dependency-aware propagation of temporal changes; historical reconstruction and version continuity; escalation, review, and authorization controls; and evaluation methods for temporal validation systems.

It does not attempt to solve general time-series forecasting, establish a universal freshness threshold, or replace domain-specific regulatory and safety requirements.

### 1.4 Design objective

The proposed system should preserve historical records while making present applicability explicit. It should avoid silently rewriting the past, silently carrying expired conclusions forward, or automatically treating every new source version as a substantive change.

The central design objective is:

> Preserve what was known, when it was known, what period it described, why it was considered valid, and what later change requires reassessment.

---

## 2. Conceptual foundations

### 2.1 Temporal validity is not provenance

The following dimensions must remain distinct:

| Dimension | Core question |
|---|---|
| Provenance | Where did this information originate, and how did it reach the system? |
| Integrity | Has the recorded content remained intact? |
| Authenticity | Is the source or artifact what it claims to be? |
| Reliability | How dependable is this source for this type of claim? |
| Temporal validity | For what time or interval does the information apply? |
| Contextual applicability | Does it apply to this entity, jurisdiction, population, system, or decision? |
| Epistemic status | Is it observed, reported, inferred, estimated, disputed, or unknown? |

A record can score strongly on provenance and integrity while being temporally inapplicable. Conversely, a recently published item may be unreliable or refer to an earlier period.

No single “verified” flag should collapse these dimensions.

### 2.2 Five important times

A temporal evidence record should distinguish at least five time concepts:

- **Event time:** when the described event or state occurred.
- **Observation time:** when an observation was made or measured.
- **Publication time:** when the source made the information available.
- **Ingestion time:** when the system received or stored it.
- **Assessment time:** when the system evaluated its relevance, validity, or implications.

These timestamps are not interchangeable. A report ingested today may describe events from months earlier. A source published today may retrospectively revise a historical series. A sensor may report a delayed observation.

Where relevant, systems should also record the time a source version became effective, the time a correction was issued, and the time a decision was authorised.

### 2.3 Valid time and record time

The framework adopts a bitemporal distinction:

- **Valid time:** the interval during which a fact or claim is asserted to apply in the described world.
- **Record time:** the interval during which the system held that version of the record.

This distinction enables historical questions such as: What did the system believe on a particular date? What do we now believe was true on that date? When did the system learn that its earlier representation required correction?

The two answers may differ, and the difference must be inspectable.

### 2.4 Temporal scope of claims

Claims should carry an explicit temporal scope where the domain permits it. Examples include a point-in-time assertion, an interval assertion, a recurring schedule, a forecast horizon, a historical statement, a condition that remains true until a specified event, or an assertion whose validity is unknown.

A claim without a meaningful temporal scope should not automatically be treated as timeless. The system should mark the scope as unspecified and determine whether that omission is acceptable for the task.

### 2.5 Freshness is task-dependent

Freshness is not equivalent to recency. A ten-year-old historical record may be perfectly suitable for a question about an event ten years ago. A five-minute-old market quote may be stale for a high-frequency decision. A recently updated web page may still repeat old information.

Freshness should therefore be evaluated against the question's reference time, the claim's temporal scope, the rate at which the underlying phenomenon can change, the consequence of acting on stale information, the source's update and revision behaviour, the availability and cost of revalidation, and domain-specific legal, operational, and safety obligations.

A freshness policy is a governance rule for a defined use case, not a universal property of a document.

---

## 3. Proposed temporal evidence model

### 3.1 Core record

The proposed temporal evidence object extends the evidence and graph concepts developed in earlier KSEL notes.

| Field | Purpose |
|---|---|
| temporal_record_id | Stable identifier for the temporal record |
| evidence_id | Link to the underlying evidence object |
| version_id | Identifier for this specific content or interpretation version |
| subject | Entity, event, process, or state being described |
| predicate | Property or relationship asserted |
| value | Recorded value or proposition |
| event_time | Time of the described event |
| observation_time | Time of observation |
| publication_time | Time of publication |
| ingestion_time | Time received by the system |
| assessment_time | Time of temporal assessment |
| valid_from / valid_to | Claimed validity interval |
| record_from / record_to | System record-time interval |
| temporal_precision | Exact, bounded, approximate, date-only, or unknown |
| temporal_basis | Source statement, measurement, inference, or policy |
| update_policy | Applicable revalidation policy |
| last_validated_at | Most recent completed validation time |
| next_review_at | Scheduled review time, if applicable |
| temporal_status | Current temporal assessment state |
| supersedes / superseded_by | Version lineage |
| dependencies | Claims, decisions, or records that depend on this object |
| assessment_rationale | Explanation and supporting evidence |

The schema is illustrative. Implementations may use different names or storage formats, but should preserve the semantic distinctions.

### 3.2 Temporal precision and uncertainty

Time itself may be uncertain. A source may state “early March”, provide a date without a time zone, or report an event within a measurement window.

The system should not manufacture precision. It should represent temporal uncertainty explicitly: exact timestamp with known time zone; date-only value; bounded interval; approximate period; relative expression resolved against a recorded reference time; or unknown or conflicting time.

Temporal uncertainty should be propagated where it affects claim validity or decision relevance. If an event could have occurred either before or after a critical deadline, the system should preserve that ambiguity rather than select a convenient point estimate.

### 3.3 Interval semantics

An interval should specify whether its endpoints are inclusive or exclusive and how open-ended intervals are interpreted. Implementations should define consistent rules for point events, continuous states, overlapping intervals, gaps between observations, unknown end times, retroactive corrections, and conflicting valid-time assertions.

A claim may be valid for one interval and invalid for another. The system should support partial validity rather than forcing every record into a single current/expired binary.

### 3.4 Temporal relationships

A temporal evidence graph may use typed relationships such as:

- VALID_DURING
- OBSERVED_AT
- PUBLISHED_AT
- INGESTED_AT
- ASSESSED_AT
- SUPERSEDES
- CORRECTS
- RETRACTS
- REVALIDATES
- CONTRADICTS_DURING
- DEPENDS_ON
- TRIGGERS_REVIEW_OF
- DERIVED_FROM_VERSION
- APPLIES_AFTER
- EXPIRES_AT

Relationships must carry provenance and, where relevant, their own temporal scope. A correction relationship should identify what was corrected, by whom or by what process, when the correction was received, and which claims were affected.

### 3.5 Version continuity

New evidence should create a new version or evidence object linked to the previous one; it should not silently overwrite historical content. The system should preserve original content or a verifiable reference to it, version identifiers and integrity metadata, source-reported revision history where available, system-observed change time, change classification and rationale, and downstream objects affected by the change.

A new version does not automatically invalidate every earlier claim. It initiates an assessment of whether the new version changes the evidence's meaning, scope, reliability, or applicability.

---

## 4. Freshness and temporal validity assessment

### 4.1 Freshness as a function

The framework proposes that freshness be evaluated as a contextual function rather than a fixed age score:

[
F = f(t_q, t_e, \Delta t, \lambda, C, R, U, P)
]

Where (t_q) is the reference time of the question or decision; (t_e) is the relevant evidence time; (Delta t) is elapsed time under the selected temporal semantics; (lambda) represents the expected rate of change in the domain; (C) represents the consequence of stale information; (R) represents source revision behaviour; (U) represents uncertainty about temporal scope; and (P) represents the applicable freshness policy.

This is a conceptual representation, not a calibrated scoring function. The variables and their operational definitions require domain-specific research.

### 4.2 Three separate assessments

A temporal assessment should not return only one confidence value. At minimum, it should distinguish:

1. **Temporal fit:** Does the evidence cover the time period relevant to the question?
2. **Current-state freshness:** Is the evidence recent enough for the intended use, given the domain's change rate and risk?
3. **Revision status:** Is the evidence known to have been corrected, superseded, withdrawn, or challenged?

These assessments may produce different outcomes. A historical record may have excellent temporal fit but be unsuitable for a current-state question. A recent record may be temporally fresh but later withdrawn.

### 4.3 Freshness policies

A policy should define the use case and affected evidence classes; required reference time; maximum age or review interval, if justified; event-based triggers that override time-based schedules; consequence-based escalation rules; acceptable temporal uncertainty; required source diversity or corroboration; behaviour when revalidation is unavailable; and the authority permitted to accept an exception.

Time-to-live values may be useful operational controls, but a TTL expiration should normally trigger review or a restricted-use state. It should not rewrite history or imply that the historical observation was false.

### 4.4 No universal decay curve

A simple exponential decay model may be useful in selected domains, but it should not be treated as a general law of evidence validity. Some facts change continuously, some change abruptly, some remain stable for long periods, and some are historical by definition.

Where a mathematical decay function is used, it should be justified by observed domain behaviour, calibrated against an appropriate baseline, and tested for failure under regime changes. The system should expose the model and its limitations.

### 4.5 Unknown freshness

When the system cannot establish the relevant time or update history, it should represent freshness as unknown. Unknown must not be silently mapped to fresh, expired, or low confidence. The correct response depends on the task's risk and constraints.

---

## 5. Evidence evolution and revalidation lifecycle

### 5.1 Proposed lifecycle states

| State | Meaning |
|---|---|
| UNASSESSED | Temporal applicability has not yet been evaluated |
| CURRENT | Evidence is assessed as suitable for the defined temporal use |
| REVIEW_DUE | A scheduled or policy-defined review point has been reached |
| CHANGE_DETECTED | A possible substantive or metadata change has been identified |
| REVALIDATION_REQUIRED | Existing dependent claims should not be treated as current until review |
| REVALIDATING | A review is in progress |
| VALID_WITH_LIMITATIONS | Evidence remains usable only within stated temporal or contextual limits |
| SUPERSEDED | A later version replaces this version for a defined purpose |
| RETRACTED | The source or responsible authority has withdrawn the assertion |
| EXPIRED_FOR_USE | Evidence is no longer suitable for a specified use, without erasing historical value |
| CONFLICTED | Material temporal assertions cannot currently be reconciled |
| UNAVAILABLE | Revalidation could not be completed |

These states are not necessarily mutually exclusive across all dimensions. A historical version can be superseded for current use while remaining valid as a record of what was published at an earlier time.

### 5.2 Trigger classes

Revalidation may be initiated by a scheduled review interval, a new source version, a correction or retraction notice, a newly observed event, a changed entity or operating context, a contradiction from an independent source, a failed integrity or authenticity check, a changed assumption in a dependent claim, a decision review date, or an authorized reviewer request.

Triggers should be recorded with their origin, time, detection method, and confidence. A trigger indicates a need to assess; it is not itself proof that the underlying claim is false.

### 5.3 Change classification

A detected change should be classified before its consequences are propagated. Proposed categories include:

- **Metadata-only:** formatting, indexing, or non-substantive metadata changed.
- **Correction:** an earlier error is explicitly corrected.
- **Substantive revision:** the source changes a material assertion.
- **Scope change:** the population, jurisdiction, entity, or period covered changes.
- **Status transition:** an item becomes active, inactive, approved, withdrawn, or otherwise changes state.
- **New observation:** new evidence is added without changing the prior record.
- **Contradiction:** a new source conflicts with an existing claim.
- **Unclear change:** the difference cannot yet be interpreted safely.

Classification should be evidence-based and reversible through an auditable review process.

### 5.4 Revalidation workflow

A proposed workflow is:

1. Detect a scheduled or event-driven trigger.
2. Preserve the trigger and source version.
3. Identify the temporal object and affected evidence.
4. Compare the new material with the prior version.
5. Classify the change and estimate its materiality.
6. Identify dependent claims, assumptions, recommendations, and decisions.
7. Reassess temporal fit, source reliability, provenance, and contextual applicability.
8. Update affected claims only through versioned review.
9. Escalate unresolved conflicts or high-consequence changes.
10. Record reviewer authority, rationale, and any restrictions.
11. Monitor whether further evidence or action is required.

Automation may support detection, comparison, dependency discovery, and review prioritisation. It should not silently convert uncertain changes into authoritative conclusions.

### 5.5 Failure to revalidate

If revalidation cannot be completed, the system should preserve the last known assessment and clearly mark its limitations. Depending on risk, it may permit historical use only, permit current use with an explicit stale-data warning, require human review before consequential action, suspend a recommendation or dependent workflow, or escalate to a designated authority.

The appropriate response must be defined by domain policy and consequence, not chosen solely by a model confidence score.

---

## 6. Dependency-aware change impact

### 6.1 Why dependency matters

A temporal change rarely affects only one record. A revised regulation may affect multiple compliance claims, risk assessments, and decisions. A corrected sensor calibration may affect an entire sequence of derived measurements. A changed business status may affect eligibility conclusions and recommendations.

The evidence graph should therefore represent dependencies between evidence versions, claims, assumptions, analyses, recommendations, and decisions.

### 6.2 Impact graph

Let a directed graph be:

[
G_t = (V, E, \tau)
]

Where (V) is the set of versioned evidence, claim, assumption, analysis, and decision nodes; (E) is the set of typed dependency and derivation edges; and (	au) assigns temporal semantics to nodes and edges.

When a source node changes, the system should traverse relevant dependency paths to identify downstream objects requiring assessment.

Graph reachability alone is insufficient. A dependency may be informational, contextual, optional, or mandatory. Each edge should express its role and, where possible, its strength or condition.

### 6.3 Impact classification

Potential downstream impact can be classified as direct, transitive, contextual, non-material, or unknown. A non-material classification should include a rationale and the assumptions under which it holds. It must not be used as a shortcut to avoid review in high-consequence cases.

### 6.4 Avoiding indiscriminate invalidation

Not every update should invalidate every dependent conclusion. A typographical correction may have no substantive effect; a change to one historical data point may affect only a limited interval; a new observation may strengthen a conclusion without changing its validity period.

The framework therefore proposes selective reassessment based on semantic change, temporal overlap, dependency role, and consequence. Selective propagation must be conservative where dependencies or temporal scopes are uncertain.

### 6.5 Decision re-opening

A decision record should retain its original evidence snapshot and authorization history. If a material dependency changes, the system should create a review event linked to the original decision. It should not rewrite the original decision as though the new information had been available at the time.

The review may conclude that the decision remains justified, requires modification, should be suspended pending further evidence, should be reversed or replaced by an authorized decision-maker, or cannot be reassessed because critical evidence is unavailable.

The system can identify and explain the need for review; authority to change a consequential decision remains governed by the relevant human or institutional process.

---

## 7. Architecture proposal

### 7.1 Functional components

A reference architecture may include:

1. **Temporal Ingestion Adapter** — captures source timestamps, version identifiers, time zones, and revision metadata.
2. **Temporal Normalization Service** — normalizes time representations while preserving original expressions and uncertainty.
3. **Version and Lineage Registry** — stores immutable or append-only version history and links superseding or correcting records.
4. **Temporal Policy Engine** — applies use-case-specific freshness and review policies.
5. **Change Detection Service** — identifies new versions, corrections, status changes, and potential semantic differences.
6. **Temporal Assessment Engine** — evaluates time fit, freshness, revision status, and uncertainty.
7. **Dependency Impact Analyzer** — finds affected claims, analyses, recommendations, and decisions.
8. **Review Orchestrator** — schedules, prioritizes, and routes reassessment work.
9. **Decision Governance Interface** — exposes impact summaries and routes decisions to authorized reviewers.
10. **Audit and Monitoring Layer** — records triggers, evaluations, overrides, outcomes, and unresolved issues.

### 7.2 Processing boundary

The architecture should distinguish machine-generated signals from authoritative state transitions. A change detector may propose that a source has materially changed. A policy engine may determine that review is mandatory. A reviewer or authorized process may approve a new claim status.

The system should retain these as separate events with separate actors and evidence.

### 7.3 Illustrative processing sequence

[
\text{New Version}
\rightarrow \text{Change Assessment}
\rightarrow \text{Temporal Evaluation}
\rightarrow \text{Dependency Analysis}
\rightarrow \text{Review}
\rightarrow \text{Authorized Update}
]

Each stage should emit a traceable record. Failed stages should not be represented as successful completion.

### 7.4 Integration with prior KSEL notes

This proposal extends earlier KSEL research themes:

- RN-001 provides evidence governance, uncertainty, and review controls.
- RN-002 contributes cost-aware evidence selection and value-of-information reasoning.
- RN-003 contributes integrity, provenance verification, and adversarial resilience.
- RN-004 contributes versioned evidence graphs and cross-source reasoning.
- RN-005 connects evidence to causal assumptions, recommendations, authorization, and outcomes.

RN-006 adds a temporal governance layer across these capabilities. It does not replace their controls. Temporal freshness cannot compensate for weak provenance, and verified provenance cannot compensate for expired applicability.

---

## 8. Governance, safety, and operational safeguards

### 8.1 Historical integrity

Historical records should remain reconstructable. Corrections should create explicit new versions or correction events. Systems should preserve what was known at the time and what is understood now.

### 8.2 Time-source reliability

Time metadata can be wrong, manipulated, missing, or inconsistent. Systems should record time zones, clock sources, synchronization assumptions, and any normalization applied. High-assurance settings may require trusted timestamping or independent corroboration.

### 8.3 Adversarial update risks

An attacker may attempt to introduce a false update or retraction, backdate or forward-date content, trigger excessive revalidation to exhaust resources, manipulate source version identifiers, exploit ambiguous time zones, replace a trusted source with a lookalike, or inject instructions into updated content to influence downstream agents.

Temporal update handling must therefore reuse KSEL provenance, integrity, source-authenticity, and untrusted-content controls. A new version is data to assess, not an instruction to obey.

### 8.4 Review prioritisation

Review priority may consider consequence, uncertainty, dependency centrality, time sensitivity, and cost of delay. However, mandatory safety, privacy, legal, and security constraints must remain hard constraints. A low estimated review value must not override a mandatory review requirement.

### 8.5 Human oversight and contestability

Reviewers should be able to inspect what changed and when; which source version was used previously; which temporal assumptions were applied; which dependent objects were identified; why an item was classified as material or non-material; what remains uncertain; and who authorized a consequential state change.

Users and affected stakeholders should have a route to challenge incorrect timestamps, stale classifications, or incomplete dependency mappings.

### 8.6 Privacy and retention

Temporal histories can reveal behavioural patterns, location histories, operational schedules, and sensitive personal information. Retention should be purpose-limited and governed by applicable law and policy. Immutable auditability must not become an excuse for indiscriminate retention of personal data. Where deletion or minimization obligations apply, systems need a documented approach that preserves only legally and operationally justified audit metadata.

---

## 9. Evaluation programme and falsifiable hypotheses

The following hypotheses are proposed for future empirical evaluation. They are not findings.

### H1 — Temporal metadata improves stale-evidence detection

**Hypothesis:** Systems that explicitly distinguish event, observation, publication, ingestion, assessment, and valid time will identify temporally inapplicable evidence more accurately than systems using a single timestamp or undifferentiated recency heuristic.

**Evaluation:** Construct benchmark cases with delayed ingestion, retrospective publication, revised historical data, ambiguous intervals, and current-state queries. Compare detection precision, recall, calibration, and error categories.

### H2 — Context-dependent freshness policies outperform universal age thresholds

**Hypothesis:** Freshness policies conditioned on task reference time, domain change rate, consequence, and temporal scope will reduce inappropriate stale/fresh classifications compared with one global time-to-live threshold.

**Evaluation:** Compare policies across domains with different change dynamics. Measure false-fresh and false-stale rates, policy violations, and downstream decision impact. Evaluate whether gains generalize beyond the calibration dataset.

### H3 — Versioned dependency analysis reduces missed downstream reassessments

**Hypothesis:** A typed, version-aware dependency graph will identify more materially affected claims and decisions than a flat evidence store or untyped link graph.

**Evaluation:** Introduce controlled source changes into synthetic and, where available, appropriately governed real-world workflows. Compare affected-object recall, irrelevant review volume, missed critical dependencies, and traceability.

### H4 — Change classification reduces unnecessary invalidation

**Hypothesis:** Explicit classification of metadata-only, corrective, substantive, scope, status, and unclear changes will reduce unnecessary downstream invalidation without increasing missed material changes.

**Evaluation:** Use blinded expert-labelled change sets. Measure classification agreement, downstream over-invalidation, under-invalidation, reviewer workload, and severity-weighted error.

### H5 — Bitemporal history improves historical reconstruction

**Hypothesis:** Maintaining both valid-time and record-time histories will improve the accuracy of reconstructing what a system represented at a prior time compared with systems that overwrite records or store only current state.

**Evaluation:** Ask evaluators to reconstruct historical system knowledge and contemporaneous decision bases from versioned scenarios. Measure factual accuracy, temporal attribution, completeness, and reconstruction time.

### H6 — Trigger-based revalidation improves responsiveness to material change

**Hypothesis:** Combining scheduled reviews with event-driven triggers will reduce time-to-reassessment for material changes compared with scheduled review alone, without producing unacceptable review burden.

**Evaluation:** Simulate changes with varied arrival patterns and materiality. Measure detection latency, review latency, false-trigger rate, workload, and unresolved exposure time.

### H7 — Explicit uncertainty about time reduces false precision

**Hypothesis:** Representing temporal precision and interval uncertainty explicitly will reduce unjustified point-time assumptions and improve reviewer calibration in ambiguous-date cases.

**Evaluation:** Compare systems that preserve approximate or bounded time with systems that normalize all timestamps to a single point. Measure temporal attribution error, confidence calibration, and reviewer decisions.

### 9.1 Experimental design requirements

A credible evaluation should include clearly defined tasks, domains, and temporal reference conditions; ground-truth labels created through documented expert procedures; baselines including single-timestamp, fixed-TTL, and no-dependency approaches; ablations for temporal metadata, policy rules, change classification, and dependency propagation; stress tests involving delayed, missing, contradictory, manipulated, and retrospectively corrected timestamps; separate reporting of false-fresh and false-stale outcomes; severity-weighted analysis where errors have unequal consequences; confidence intervals or other appropriate uncertainty estimates; reproducible datasets, code, policy configurations, and evaluation protocols where lawful and feasible; and documentation of annotator disagreement and unresolved ground-truth ambiguity.

### 9.2 Metrics

| Metric | Purpose |
|---|---|
| Temporal applicability precision | Proportion of evidence classified as applicable that is actually applicable |
| Temporal applicability recall | Proportion of applicable evidence correctly identified |
| False-fresh rate | Inapplicable evidence incorrectly treated as fresh |
| False-stale rate | Applicable evidence incorrectly rejected as stale |
| Change detection latency | Time between source change availability and system detection |
| Revalidation latency | Time between trigger and completed reassessment |
| Impact recall | Proportion of materially affected dependencies identified |
| Over-invalidation rate | Proportion of unaffected objects unnecessarily invalidated |
| Historical reconstruction accuracy | Accuracy of reconstructing system knowledge at a past time |
| Review burden | Human effort required for triggered reviews |
| Escalation appropriateness | Agreement between system routing and defined review requirements |

No single metric is sufficient. High recall with excessive false alarms may be operationally unusable; low review burden achieved by missing material changes is unacceptable.

---

## 10. Limitations and open research questions

This framework has important limitations:

1. **Temporal ground truth is often unavailable.** Sources may disagree about when an event occurred or when a state became effective.
2. **Change is domain-specific.** A single freshness model cannot represent every domain's dynamics.
3. **Semantic change detection remains difficult.** Textual differences do not necessarily imply changed meaning, and meaning can change without obvious textual differences.
4. **Dependency graphs may be incomplete.** Unrecorded assumptions and implicit reasoning paths can cause impact analysis to miss affected conclusions.
5. **Revalidation has a cost.** Continuous checking can create excessive load, especially where sources are numerous or unstable.
6. **Sources may be inaccessible.** A system cannot honestly claim that evidence remains current when it cannot verify the relevant source.
7. **Time metadata can be adversarial.** Timestamp integrity and source authenticity require separate controls.
8. **Historical validity is not current applicability.** Systems must preserve historical usefulness without confusing it with present validity.
9. **Human review can be inconsistent.** Governance requires clear policies, reviewer training, and auditability.
10. **Automation can create false authority.** Machine-generated status changes must not be confused with authorized decisions.

Open questions include how freshness policies should be calibrated without embedding unsafe assumptions; how temporal uncertainty should propagate through causal and probabilistic reasoning; how systems should reason about recurring, seasonal, or event-triggered validity; how semantic change detection can be evaluated across languages and formats; how temporal dependency should be represented when a claim relies on a combination of evidence versions; what balance should exist between continuous monitoring and cost-aware review; how conflicting source histories should be represented when no authoritative timeline exists; and how systems can communicate “last known valid” without implying “currently verified”.

---

## 11. Implementation research priorities

A staged implementation programme is proposed:

**Stage A — Data model:** Define temporal fields, interval semantics, precision representation, and bitemporal version history.

**Stage B — Policy prototype:** Implement explicit, inspectable freshness and revalidation policies for a narrow domain.

**Stage C — Change detection:** Ingest source versions and classify metadata, corrective, substantive, and uncertain changes.

**Stage D — Dependency impact:** Connect changed evidence versions to claims and decisions through typed graph relationships.

**Stage E — Review workflow:** Route revalidation tasks, record reviewer rationale, and preserve authorization boundaries.

**Stage F — Evaluation:** Run baselines, ablations, adversarial tests, and historical reconstruction experiments.

**Stage G — Governance review:** Assess privacy, security, auditability, operational burden, and domain-specific obligations before any consequential deployment.

Each stage should produce versioned specifications, test cases, known limitations, and reproducible evidence. Progress through a stage must not be described as validation of the complete architecture.

---

## 12. Conclusion

Evidence governance must account for time as a first-class dimension. Provenance can establish where information came from; integrity can establish whether a record has changed; neither alone establishes whether the information remains applicable to a present question.

KSEL RN-006 proposes a temporal intelligence layer that preserves the distinction between when something happened, when it was observed, when it was published, when the system recorded it, and when it was assessed. It introduces context-dependent freshness policies, versioned temporal records, change classification, revalidation triggers, dependency-aware impact analysis, and controlled decision reopening.

The intended outcome is not a system that claims to know that all information is current. It is a system that can state what it has checked, what period the evidence covers, what changed, what remains uncertain, which conclusions may be affected, and what review is required.

Temporal intelligence should make the evolution of knowledge inspectable rather than conceal it behind a current-state label.

---

## Appendix A — Illustrative temporal record

The following example is hypothetical and exists only to demonstrate the proposed fields.

| Attribute | Illustrative value |
|---|---|
| Record | TEMP-EXAMPLE-001 |
| Subject | Example equipment operating status |
| Assertion | Equipment is certified for a defined operating configuration |
| Event / valid time | 1 January–30 June 2026 |
| Publication time | 5 January 2026 |
| Ingestion time | 6 January 2026 |
| Assessment time | 7 January 2026 |
| Temporal precision | Date-bounded interval |
| Policy | Revalidate on certificate revision or before a specified operation |
| Trigger | New certificate version detected |
| Change class | Unclear pending comparison |
| State | REVALIDATION_REQUIRED |
| Dependent objects | Operating eligibility claim; related recommendation |
| Required action | Compare versions and route to authorized reviewer |

This example does not describe a real certificate, equipment item, or completed validation.

## Appendix B — Minimum temporal review record

A review event should capture, at minimum: review event identifier; trigger identifier and origin; affected evidence and version identifiers; reference time and assessment time; applicable freshness policy and policy version; temporal scope and precision; change classification and comparison evidence; affected dependency paths; assessment result and uncertainty; restrictions or escalation requirements; reviewer or process identity and authority; decision rationale and timestamp; and follow-up action and next review condition.

## Appendix C — Suggested conformance questions

An implementation claiming alignment with this proposed framework should be able to answer:

1. Can it distinguish event, observation, publication, ingestion, and assessment time?
2. Can it represent valid time separately from record time?
3. Can it preserve approximate, bounded, and unknown temporal precision?
4. Can it explain why evidence is considered fresh for a particular use?
5. Can it distinguish source revision from substantive change?
6. Can it identify dependent claims and decisions affected by a change?
7. Can it preserve historical decision context without rewriting prior records?
8. Can it mark revalidation as unavailable or incomplete?
9. Can it route consequential changes through an authorized review process?
10. Can it reproduce the temporal assessment from retained versions, policies, and audit records?

These questions are proposed evaluation prompts, not a certification checklist or established standard.

---

## Selected references and related work

These sources provide foundations for temporal data semantics, provenance, and changing data distributions. KSEL's proposed freshness policies and reassessment rules require domain-specific validation.

1. Jensen, C. S., et al. (1994). A Consensus Glossary of Temporal Database Concepts. *ACM SIGMOD Record, 23*(1), 52–64. https://doi.org/10.1145/181550.181560 — Shared terminology for temporal database concepts.
2. Snodgrass, R. T. (1999). *Developing Time-Oriented Database Applications in SQL*. Morgan Kaufmann. https://shop.elsevier.com/books/developing-time-oriented-database-applications-in-sql/snodgrass/978-0-08-050422-3 — Temporal and bitemporal database application design.
3. W3C. (2013). *PROV-O: The PROV Ontology*. W3C Recommendation. https://www.w3.org/TR/prov-o/ — Provenance representation, including activities and temporal metadata.
4. Gama, J., Žliobaitė, I., Bifet, A., Pechenizkiy, M., & Bouchachia, A. (2014). A survey on concept drift adaptation. *ACM Computing Surveys, 46*(4), Article 44. https://doi.org/10.1145/2523813 — Changes in data distributions and adaptation/evaluation methods.

## Publication and research integrity statement

This document presents a preliminary research framework developed for the KSEL research-note series of H3XYN LAB. Its architecture, schema, lifecycle states, hypotheses, metrics, and implementation stages are proposals for investigation.

No empirical validation, benchmark result, production deployment, certification, or demonstrated performance is claimed by this publication. The illustrative records are hypothetical. The hypotheses require independent testing, documented methods, suitable baselines, and reproducible evidence.

Future revisions should identify material changes, preserve version history, document corrections, and distinguish proposed concepts from experimentally supported conclusions.

**End of KSEL Research Note 006.**

**Suggested citation**

H3XYN LAB. (2026). *KSEL Research Note 006: Temporal Intelligence, Evidence Evolution, and Continuous Knowledge Validation* (Version 0.1.0). H3XYN LAB Technical Research Notes. https://github.com/Hexynlab/ksel-research-note-001

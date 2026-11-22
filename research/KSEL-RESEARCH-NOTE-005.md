# KSEL Research Note 005
## Decision Intelligence, Causal Reasoning, and Evidence-Based Decision Systems

**Research programme:** KSEL — Knowledge, Source, Evidence Layer  
**Institution:** H3XYN LAB  
**Publication type:** Preliminary research framework  
**Version:** 0.1.0  
**Date:** 22 November 2026  
**Status:** Proposed architecture and research agenda; not experimentally validated

---

## Abstract

Evidence systems commonly retrieve, classify, summarise, and connect information. Consequential decisions require a further discipline: connecting governed evidence to possible actions while preserving the distinction between observation, inference, assumption, preference, recommendation, and authorization.

This note proposes a decision-intelligence layer for KSEL. It defines a structured representation of decision problems, objectives, constraints, alternatives, causal assumptions, scenarios, uncertainty, recommendations, approvals, and observed outcomes. It proposes causal reasoning safeguards, sensitivity analysis, alternative comparison, and post-decision monitoring.

Evidence may inform a decision without mechanically determining it. A decision also depends on objectives, constraints, risk tolerance, time horizon, reversibility, and the authority of the decision-maker. The system should support structured and contestable reasoning rather than conceal normative choices inside a score.

All architecture, workflows, hypotheses, and evaluation methods are proposals. No empirical validation or performance claim is made.

**Keywords:** evidence governance, decision intelligence, causal reasoning, uncertainty, counterfactuals, decision analysis, human oversight

## 1. Purpose and scope

Research Notes 001–004 address evidence governance, cost-aware evidence acquisition, integrity and provenance, and evidence-graph representation. This note examines how governed evidence can support decisions without confusing evidence with authority or inference with fact.

The proposed scope includes:
- Formal representation of decision problems and context.
- Separation of objectives, constraints, alternatives, assumptions, and evidence.
- Causal reasoning safeguards and counterfactual limitations.
- Scenario and consequence analysis.
- Uncertainty propagation and sensitivity analysis.
- Alternative comparison without hiding value judgements.
- Decision records, review, authorization, and post-decision monitoring.
- A falsifiable evaluation programme.

It does not prescribe a universal decision algorithm, establish domain-specific policy, or authorize autonomous execution of high-impact actions. Legal, clinical, financial, safety, and operational requirements remain domain-specific constraints.

### 1.1 Relationship to prior notes

| Note | Contribution |
|---|---|
| RN-001 | Evidence governance, uncertainty, review states, auditability |
| RN-002 | Cost-aware evidence acquisition, sufficiency, stopping rules |
| RN-003 | Integrity, provenance, adversarial resilience |
| RN-004 | Evidence graphs, temporal semantics, cross-source reasoning |
| RN-005 | Decision representation, causal reasoning, alternative comparison, authorization |

RN-005 is a conceptual extension. It does not imply that earlier proposals have been implemented or validated.

## 2. Foundational principles

### 2.1 Evidence informs; authorized actors decide

A system may identify evidence, expose implications, compare alternatives, and estimate possible outcomes. It must not represent a recommendation as an authorized decision. Decision authority must be explicit and attributable.

### 2.2 Descriptive and normative reasoning remain distinct

Descriptive statements concern what is observed or estimated. Normative statements concern what should be preferred. Preferences and risk tolerance must not be disguised as objective facts.

- **Descriptive:** Under stated assumptions, Alternative A has a lower estimated operating cost.
- **Normative:** Operating cost should receive greater weight than implementation speed.
- **Decision:** The authorized decision-maker selected Alternative A.

These are different statement types and should be separately represented.

### 2.3 Preserve the evidence-to-action chain

A decision record should trace the decision question, alternatives, objectives, constraints, evidence, assumptions, causal model, uncertainty, analysis, recommendation, authorization, and subsequent outcomes. A concise explanation does not replace the underlying trace.

### 2.4 Uncertainty is multidimensional

Uncertainty may arise from measurement, missing information, source reliability, model specification, causal identification, changing conditions, or disagreement about objectives. A single confidence score can conceal materially different weaknesses.

### 2.5 Constraints are not preferences

Mandatory legal, safety, privacy, security, and authorization requirements must be represented as constraints. They must not be converted into weighted preferences that can be outweighed by an attractive score.

### 2.6 Recommendations must be contestable

Reviewers should be able to challenge evidence selection, provenance, assumptions, causal structure, objectives, weights, and interpretation. Relevant dissent should be retained.

## 3. Decision problem representation

### 3.1 Proposed decision object

| Field | Description |
|---|---|
| Decision ID | Stable identifier |
| Decision question | Question to be resolved |
| Decision owner | Accountable actor |
| Decision authority | Actor or process authorized to approve |
| Context | Operational, temporal, and environmental conditions |
| Objectives | Desired outcomes or criteria |
| Constraints | Mandatory conditions |
| Alternatives | Candidate actions, including status quo, defer, or gather evidence |
| Time horizon | Period over which consequences are assessed |
| Stakeholders | Parties affected or entitled to participate |
| Evidence set | Governed evidence and provenance |
| Assumptions | Premises not established by evidence |
| Causal model | Proposed relationships between actions, conditions, and outcomes |
| Uncertainty profile | Known uncertainty dimensions and unresolved questions |
| Analysis method | Methods used to compare alternatives |
| Recommendation | Optional system-generated assessment |
| Authorization record | Approval, rejection, deferral, or escalation |
| Review trigger | Conditions requiring reassessment |
| Outcome record | Observed consequences and later findings |

Decision objects should be versioned. Changes to the question, constraints, evidence, assumptions, or alternatives may materially change the analysis and must not silently overwrite prior states.

### 3.2 Decision question quality

A decision question should identify the decision-maker, action space, context, time horizon, relevant objectives, and constraints. If these are unclear, the system should record ambiguity or request clarification rather than manufacture a complete problem statement.

### 3.3 Alternatives and status quo

The alternatives should include, where relevant:
- Take no action or maintain the current arrangement.
- Defer the decision.
- Gather additional evidence.
- Conduct a limited or reversible pilot.
- Escalate to a qualified authority.

The system must not imply that the listed alternatives exhaust all possible actions unless this has been established.

### 3.4 Objectives, constraints, and stakeholders

Objectives may include cost, reliability, safety, timeliness, reversibility, resilience, or service quality. Their definitions, measurement methods, priorities, and owners should be recorded.

Constraints should be evaluated before preference-based ranking. An alternative that violates a mandatory constraint should be marked infeasible or escalated, not kept competitive through compensation from unrelated benefits.

Aggregate outcomes may conceal who benefits and who bears the cost. Where material, record distributional consequences, affected groups, procedural fairness, and missing stakeholder perspectives. Do not infer consent from silence or from public-data availability.

## 4. From evidence graph to decision graph

### 4.1 Architectural extension

RN-004 proposes a typed, versioned evidence graph. This note proposes connecting it to a decision graph through explicit relationships. They may share one graph store or use interoperable stores, provided identifiers, provenance, versioning, and access controls remain consistent.

Evidence objects, claims, causal assumptions, alternatives, and approvals must not be collapsed into generic nodes.

### 4.2 Proposed node types

| Node type | Purpose |
|---|---|
| Decision | Decision problem and lifecycle |
| Objective | Desired outcome or criterion |
| Constraint | Mandatory boundary |
| Alternative | Candidate action or inaction |
| ContextVariable | Relevant condition |
| CausalVariable | Variable in a causal model |
| CausalRelation | Proposed causal dependency |
| Outcome | Consequence or measured result |
| Scenario | Coherent assumed conditions |
| Assumption | Premise not directly established by evidence |
| Estimate | Model- or analyst-produced quantity |
| RiskAssessment | Structured adverse-outcome assessment |
| Recommendation | System-generated proposal |
| Authorization | Approval, rejection, delegation, or deferral |
| MonitoringEvent | Post-decision observation or trigger |
| ReviewRecord | Human or institutional examination |

Existing RN-004 types remain available, including Source, EvidenceObject, Observation, Claim, Entity, Method, Transformation, Inference, UncertaintyAssessment, Review, Policy, and Event.

### 4.3 Proposed relationship vocabulary

| Relationship | Meaning |
|---|---|
| ADDRESSES | Decision addresses a question |
| PURSUES | Decision or alternative pursues an objective |
| SUBJECT_TO | Decision or alternative is governed by a constraint |
| CONSIDERS | Decision includes an alternative |
| EXCLUDES | Alternative was considered but ruled out, with reason |
| RELIES_ON | Analysis relies on evidence, claims, or assumptions |
| INFORMS | Evidence contributes to an estimate or assessment |
| ASSUMES | Analysis explicitly depends on an assumption |
| MODELS | Causal model represents a defined system |
| CAUSES | Causal relation asserted within a specified model |
| AFFECTS | Variable or action affects an outcome in the model |
| ESTIMATES | Method produces an estimate |
| COMPARES | Analysis compares alternatives |
| RECOMMENDS | Analysis produces a recommendation |
| AUTHORIZED_BY | Outcome is authorized by an actor or process |
| IMPLEMENTED_AS | Authorized decision is translated into action |
| MONITORED_BY | Decision or action is monitored |
| TRIGGERED_REVIEW | Event initiates reassessment |
| SUPERSEDES | Later version replaces an earlier record |
| CONTESTS | Reviewer or evidence challenges a conclusion or assumption |

Relationship semantics must be documented and versioned. CAUSES is not a synonym for correlates with, predicts, or is associated with.

### 4.4 Traceability

Each recommendation should expose supporting and challenging claims, provenance and freshness, source dependencies, transformations, analytical methods, assumptions, causal links, uncertainty, objectives, constraints, excluded alternatives, and the versions of models and policies applied.

Traceability makes reasoning inspectable; it does not establish correctness.

## 5. Causal reasoning safeguards

### 5.1 Association is not causation

Observed association alone does not establish that changing one variable will change another. A causal conclusion requires an explicit identification strategy and assumptions appropriate to the domain and data.

The system should distinguish:
- Descriptive association.
- Predictive relationship.
- Mechanistic hypothesis.
- Causal estimate under stated assumptions.
- Experimentally identified causal effect.
- Expert judgement about a causal relationship.

These categories are not interchangeable levels of certainty.

### 5.2 Causal model specification

A causal model should document variables and operational definitions; proposed direction and temporal ordering; potential confounders, mediators, and moderators; selection and measurement mechanisms; missing variables and plausible alternative structures; evidence supporting each proposed relation; identification assumptions; and model version and responsible analyst.

A diagram alone is insufficient; a written specification and limitations are required.

### 5.3 Confounding and selection

Analysts should consider common causes, selection into observed samples, survivorship, measurement practices, and missing data. A large dataset is not necessarily representative; statistical significance does not establish causality.

### 5.4 Counterfactual claims

Counterfactual analysis asks what might have happened under an alternative action or condition. Such claims depend on a model, assumptions, and estimand. Disclose the target population, action and comparator, outcome, horizon, identification strategy, assumptions, uncertainty, and generalization limits.

Where these cannot be specified, label the output a scenario or hypothetical projection rather than an identified causal effect.

### 5.5 Intervention validity and causal humility

Historical relationships may not remain valid after intervention. Policy changes, human adaptation, market responses, feedback, and operational constraints can invalidate historical patterns. When evidence does not identify a causal effect, say so. Conditional scenarios may still be useful, but must not be expressed as confident causal conclusions.

## 6. Scenario and consequence analysis

A scenario is a coherent set of conditions under which an alternative is assessed; it is not automatically a prediction. Record its assumptions, context-variable values or ranges, evidence basis, time horizon, dependencies, exclusions, plausibility rationale where assessed, author, and version.

Assess relevant consequences such as benefits, direct and indirect costs, safety, security, feasibility, reversibility, time to effect, distributional impact, externalities, failure modes, and monitoring needs. Absence of an identified consequence is not evidence that no consequence exists.

Comparisons must preserve the conditions under which estimates were produced. Estimates from different horizons, populations, baselines, or assumptions must not be compared without qualification. Scenarios should include adverse as well as benign conditions.

Where uncertainty is high and action is not urgent, consider reversible pilots, staged rollout, or additional evidence. Compare the value and risks of waiting, learning, and acting now.

## 7. Uncertainty propagation and sensitivity

### 7.1 Uncertainty dimensions

Preserve distinct assessments for:
1. Measurement uncertainty.
2. Source uncertainty.
3. Sampling uncertainty.
4. Model uncertainty.
5. Causal uncertainty.
6. Scenario uncertainty.
7. Operational uncertainty.
8. Value uncertainty.

An aggregate confidence score must not replace this profile.

### 7.2 Propagation

Where quantitative methods are justified, propagate input and model uncertainty using an appropriate method and document distributions, dependencies, and assumptions. Where numerical propagation is not justified, use qualitative ranges, explicit caveats, or structured scenarios. False precision is not an improvement over honest qualitative uncertainty.

### 7.3 Sensitivity and robustness

Test how conclusions change when material assumptions, parameters, weights, or scenario conditions vary. Identify influential variables, decision thresholds, weakly supported but critical assumptions, feasibility boundaries, and unstable recommendations.

A recommendation may be called robust only relative to a defined set of alternatives, scenarios, assumptions, and criteria. State what was varied and what remained fixed. Sensitivity analysis does not substitute for causal identification or evidence quality.

## 8. Comparing alternatives without hiding value judgements

### 8.1 Proposed sequence

1. Apply mandatory constraints.
2. Remove or escalate infeasible alternatives.
3. Assess evidence sufficiency relative to the stakes.
4. Estimate consequences under stated assumptions.
5. Compare alternatives against declared objectives.
6. Examine sensitivity and distributional effects.
7. Present trade-offs and unresolved issues.
8. Refer the decision to the authorized actor.

This is a proposed governance pattern, not a universal algorithm.

### 8.2 Multi-criteria analysis

Multi-criteria decision analysis can organize trade-offs, but weights and scales encode value judgements. They must be declared, justified, versioned, and reviewable. A weighted sum is not objective truth and cannot authorize constraint violations. If stakeholders disagree about weights, show how rankings change across plausible preference sets rather than manufacture consensus.

### 8.3 Expected utility and expected value

These methods may be appropriate when outcomes and probabilities can be meaningfully specified. Disclose assumptions about probabilities, utility, risk attitude, and context. Highest expected value is not automatically the preferred action: tail risks, irreversible harms, distributional effects, legal constraints, and risk tolerance may matter.

### 8.4 Dominance and incomparability

An alternative may dominate another only relative to the declared criteria and measurements. Incomparable alternatives should remain visibly incomparable rather than be forced into one ranking.

### 8.5 No universal score

KSEL should not impose a universal decision score across domains. A common representation and audit structure may support domain-specific methods, but the meaning of risk, acceptable evidence, utility, and authorization varies by context.

## 9. Evidence sufficiency and value of further information

Evidence is sufficient only relative to a particular decision, its stakes, constraints, alternatives, and uncertainty tolerance. The same evidence may be adequate for a reversible low-impact action and inadequate for an irreversible high-impact action.

Identify decision-critical gaps: unresolved questions whose plausible answers could materially change feasibility, ranking, or risk.

Building on RN-002, an estimate of further information value may consider the probability that new evidence changes the decision; consequences of choosing incorrectly; acquisition cost and delay; whether evidence can arrive in time; likely independence and reliability; and privacy, safety, and security risks of acquisition.

Value-of-information analysis cannot waive mandatory controls or justify harmful evidence collection.

Possible analysis outcomes include proceed to authorized review, gather specified evidence, defer pending a condition, escalate, reject an infeasible alternative, or decline to recommend because evidence or model quality is inadequate. State the reason and condition for reopening.

## 10. Recommendation, authorization, and execution boundaries

A recommendation is an analytical output. Authorization is an attributable act by an actor or process with the required authority. They require separate records and states.

### 10.1 Proposed decision states

| State | Meaning |
|---|---|
| DRAFT | Decision problem is being defined |
| ANALYSIS_PENDING | Evidence or analysis incomplete |
| READY_FOR_REVIEW | Analysis package available |
| REVIEW_REQUIRED | Specialist or independent review required |
| RECOMMENDATION_ISSUED | Recommendation recorded |
| AUTHORIZED | Authorized actor approved a defined action |
| REJECTED | Proposed action or recommendation rejected |
| DEFERRED | Decision postponed pending a condition |
| ESCALATED | Higher or specialist authority required |
| IMPLEMENTATION_PENDING | Authorized action awaits execution |
| IMPLEMENTED | Execution recorded |
| MONITORING | Outcomes and triggers observed |
| REASSESSMENT_REQUIRED | New information or conditions require review |
| CLOSED | Lifecycle formally closed |

Transitions should be policy-controlled and recorded with actor, timestamp, rationale, and version.

### 10.2 High-impact decisions and execution controls

High-impact or irreversible decisions should support stronger review, independent challenge, specialist participation, documented dissent, and explicit human authorization. Domain governance must define the appropriate controls.

Where operational tools are connected, separate the decision record from execution. Verify scope, approval validity, and changed conditions before action. This note does not propose unrestricted autonomous execution.

## 11. Explanation and contestability

A decision-support explanation should identify the question, alternatives, constraints, material evidence, assumptions, causal claims and their basis, uncertainty, trade-offs, conditions that could change the recommendation, and the authority responsible for deciding.

Natural-language explanations must correspond to the actual analytical process and stored records. They must not invent a post-hoc rationale or contradict the computation. Reviewers should be able to challenge evidence, source independence, assumptions, causal links, criteria, weights, estimates, and constraints. Relevant dissent should be retained.

An explanation improves inspectability; it does not prove validity. Pair it with method documentation, validation evidence, and independent review proportionate to the stakes.

## 12. Post-decision monitoring and learning

Where outcomes can be observed, define expected outcomes, indicators, baseline, measurement method, interval, responsible owner, warning thresholds, adverse-event triggers, pause or rollback conditions, and data governance.

Distinguish decision-process quality from realized outcome. A sound decision can produce a bad outcome under uncertainty; a poor decision can succeed by chance. Process evaluation examines evidence use, constraints, assumptions, and authorization. Outcome evaluation examines realized effects relative to objectives and baseline.

New evidence should update the current assessment while preserving prior versions and the information available at the time. Do not silently insert later knowledge into the original record. Monitoring should detect changing conditions, invalid assumptions, unintended consequences, and model drift, triggering reassessment where needed.

## 13. Security, privacy, and governance

Decision-specific threats include manipulation of objectives or constraints, selective alternatives, strategic distortion of assumptions, adversarial evidence, unauthorized approval or execution, compromised identities, hidden model or weight changes, suppression of dissent, and sensitive-data leakage.

Where appropriate, separate evidence acquisition, analysis, review, authorization, and execution. Privileged actions should be logged and reviewed. Use only data necessary for the defined purpose; establish access, retention, sharing, and deletion requirements before processing.

Record policy, model, criteria, and configuration versions. Changes must be attributable and reviewable. The deploying organization remains accountable for policy, data practices, model selection, controls, and decisions. A system-generated recommendation does not transfer institutional responsibility to software.

## 14. Proposed reference architecture

The following logical components may be services, modules, or a unified system:

1. **Decision Intake:** captures question, context, owner, and horizon.
2. **Objective and Constraint Registry:** records objectives, hard constraints, and policy versions.
3. **Evidence Interface:** retrieves governed claims and evidence.
4. **Provenance and Integrity Service:** exposes lineage and verification warnings.
5. **Causal Model Workspace:** stores variables, assumptions, identification strategies, and model versions.
6. **Scenario Engine:** evaluates alternatives under explicit conditions.
7. **Uncertainty and Sensitivity Service:** tracks uncertainty and tests assumptions.
8. **Alternative Comparison Service:** presents feasibility and trade-offs.
9. **Explanation and Review Interface:** exposes reasoning paths, challenges, and dissent.
10. **Authorization Gateway:** records approvals and verifies authority.
11. **Execution Boundary:** passes only authorized, scoped actions to operational systems.
12. **Monitoring and Reassessment Service:** tracks outcomes and triggers renewed review.
13. **Audit and Version Ledger:** preserves lifecycle changes and actor attribution.

**Logical flow:** Intake → Define objectives and constraints → Retrieve governed evidence → Specify assumptions and causal model → Evaluate alternatives and scenarios → Propagate uncertainty → Test sensitivity → Prepare review package → Authorize or defer → Execute within scope → Monitor → Reassess.

A failure at any stage should produce an explicit blocked, deferred, or escalated state rather than an apparently complete recommendation.

Visible failure conditions include unavailable or stale evidence, failed integrity checks, unevaluable constraints, missing or contradicted causal assumptions, excessive model uncertainty, sensitivity to unsupported assumptions, absent or expired authority, and material changes after approval.

## 15. Illustrative workflow

The following example is hypothetical and makes no empirical claim.

An organization must decide whether to replace an existing service component during the next maintenance cycle.

1. **Question:** Should replacement occur during the next cycle?
2. **Alternatives:** Replace now; continue with enhanced monitoring; run a limited pilot; defer pending inspection.
3. **Objectives:** Reliability, safety, lifecycle cost, and service continuity.
4. **Constraints:** Applicable safety requirements, procurement rules, and service obligations.
5. **Evidence:** Maintenance records, inspection reports, specifications, and incident history.
6. **Assumptions:** Future operating load, component availability, and installation time.
7. **Causal model:** Document a hypothesis linking component condition and operating load to failure risk, including confounders and limitations.
8. **Scenarios:** Normal operation, elevated load, delayed supply, and installation disruption.
9. **Analysis:** Compare alternatives against declared criteria and disclose uncertainty and sensitivity.
10. **Review:** A qualified reviewer challenges evidence, assumptions, and feasibility.
11. **Decision:** The authorized owner approves, rejects, defers, or escalates separately from the system recommendation.
12. **Monitoring:** Compare observed failures, costs, delays, and service effects with documented expectations.

No numerical outcome is asserted and no alternative is declared preferable.

## 16. Proposed evaluation programme

### 16.1 Objective

Evaluate whether an explicit evidence-to-decision architecture improves traceability, uncertainty communication, reviewability, and resistance to reasoning errors compared with less structured workflows. Test failure modes as well as potential benefits.

### 16.2 Falsifiable hypotheses

**H1 — Traceability:** Explicit links among evidence, assumptions, criteria, analysis, and authorization will improve independent reviewers' ability to reconstruct the basis of a decision compared with records lacking those links.

**H2 — Uncertainty discrimination:** A multidimensional uncertainty representation will improve reviewers' ability to distinguish source, measurement, model, causal, and value uncertainty compared with a single aggregate confidence indicator.

**H3 — Causal claim discipline:** Explicit causal-model documentation and claim-type controls will reduce the rate at which observational associations are classified as established causal effects.

**H4 — Sensitivity awareness:** Showing decision thresholds and sensitivity to material assumptions will improve identification of fragile recommendations and decision-critical information gaps.

**H5 — Authorization integrity:** Separating recommendations from authorization records will reduce ambiguity about whether a system-generated output has been approved for action.

These hypotheses remain untested proposals.

### 16.3 Proposed design

Compare a baseline workflow using conventional evidence summaries and recommendations with a structured workflow using the KSEL evidence graph, decision graph, uncertainty profile, causal-model record, and authorization boundary.

Participants should receive equivalent case information. Control or document assignment, case order, reviewer expertise, and prior domain knowledge. Use cases with known ground truth where possible and realistic cases where no single definitive answer exists.

### 16.4 Evaluation tasks and measures

Tasks may include reconstructing evidence paths, identifying unsupported causal claims, distinguishing evidence from assumptions and preferences, detecting constraint violations, identifying decision-critical gaps, testing recommendation sensitivity, checking authorization status, and identifying reassessment triggers.

Potential measures:
- Evidence-to-decision trace reconstruction accuracy.
- Independent review time.
- Unsupported causal-claim detection rate.
- Correct uncertainty-type identification.
- Constraint-violation detection rate.
- Sensitivity-threshold identification accuracy.
- Reviewer agreement and disagreement patterns.
- False authorization interpretation rate.
- Omission and hallucination rates in explanations.
- Cognitive workload and usability ratings.

Measures must be operationally defined before testing. Faster review is not a benefit if it results from missed risks or weaker scrutiny.

### 16.5 Ablation and stress testing

Ablate provenance links, uncertainty dimensions, causal-model documentation, sensitivity analysis, and authorization separation to examine component contributions.

Stress cases should include correlated sources, fabricated evidence, stale information, missing confounders, incorrect causal direction, manipulated objective weights, hidden constraint violations, selectively framed alternatives, changed conditions after approval, ambiguous authority, distribution shifts, and unexpected outcomes.

### 16.6 Reproducibility and negative results

Disclose the corpus or lawful description, participant selection, protocol, model and policy versions, configurations, scoring rubrics, exclusions, statistical methods, limitations, and replication artifacts. Protect sensitive data.

Publish null, mixed, and adverse findings. If the architecture increases cognitive burden, creates false confidence, or fails to improve review quality, report that result.

## 17. Limitations and open questions

1. How should disagreement over objectives be represented without imposing artificial consensus?
2. Which causal formalisms are suitable across domains?
3. How can assumptions be reviewed when domain knowledge is incomplete?
4. How should uncertainty dimensions be calibrated without false comparability?
5. What evidence threshold is appropriate for different impact and reversibility levels?
6. How can explanations remain faithful to complex analytical pipelines?
7. How should confidential evidence be handled when not every reviewer may see it?
8. How should source dependence affect downstream estimates?
9. What constitutes adequate independent review in small organizations?
10. How can monitoring distinguish model drift, environmental change, and random variation?
11. How can procedural complexity be limited without weakening governance?
12. What prevents manipulation of objectives, constraints, and weights?

The architecture may improve documentation without improving evidence or causal validity, and may create administrative burden. These are empirical questions.

## 18. Implementation research priorities

**Stage A — Formal specification:** Define decision objects, state transitions, typed links to RN-004, objective and constraint records, versioning, and authorization semantics.

**Stage B — Prototype:** Implement a bounded workflow for traceability, uncertainty, and manual causal and scenario records. Keep recommendation and authorization separate.

**Stage C — Controlled evaluation:** Construct benchmark cases, compare workflows, measure traceability and review quality, and document failures.

**Stage D — Domain-specific validation:** Select a bounded domain, define constraints and qualified review roles, validate measures with relevant experts, and conduct security and privacy assessment.

**Stage E — Governance review:** Review results, revise the architecture, publish limitations, and avoid claiming production readiness from prototype completion alone.

## 19. Conclusion

KSEL's proposed decision-intelligence layer is intended to preserve the path from evidence to authorized action. It treats decisions as structured, contextual, and accountable processes rather than the output of a ranking function.

The proposed contribution is a typed connection among governed evidence, objectives, constraints, alternatives, assumptions, causal models, scenarios, uncertainty, recommendations, authorization, and observed outcomes. Causal reasoning must disclose identification assumptions; uncertainty must remain visible; value judgements must not be disguised as measurements; and constraints must not be traded away through scoring.

Recommendations remain separate from authorization, and consequential actions require governance proportionate to their impact. The framework remains a research proposal requiring controlled evaluation, domain-specific scrutiny, and transparent reporting.

## Appendix A — Minimum decision record checklist

- [ ] Decision question and context defined.
- [ ] Decision owner and authorized decision-maker identified.
- [ ] Objectives and mandatory constraints explicit.
- [ ] Alternatives include status quo or deferral where relevant.
- [ ] Evidence references include provenance and version.
- [ ] Assumptions distinguished from evidence.
- [ ] Causal claims and identification limitations documented.
- [ ] Scenarios and time horizon specified.
- [ ] Uncertainty dimensions recorded.
- [ ] Material sensitivity and trade-offs examined.
- [ ] Exclusions and reasons recorded.
- [ ] Recommendation labelled non-authoritative.
- [ ] Authorization recorded separately.
- [ ] Monitoring and reassessment triggers defined.
- [ ] Audit and version history preserved.

## Appendix B — Minimum recommendation disclosure

A recommendation should disclose the decision question, alternatives, constraints, material evidence, assumptions and causal model, analysis method and version, uncertainty and sensitivity, trade-offs, conditions that could change the recommendation, and required review and authorization.

## Appendix C — Terminology

**Alternative:** Candidate action, including inaction or deferral.  
**Assumption:** Premise used in analysis but not established as fact by available evidence.  
**Authorization:** Attributable approval by an actor or process with required authority.  
**Causal model:** Representation of hypothesized or identified causal relationships.  
**Constraint:** Mandatory condition an alternative must satisfy.  
**Decision graph:** Typed representation connecting decisions to objectives, constraints, alternatives, assumptions, evidence, analysis, authorization, and outcomes.  
**Decision intelligence:** Structured analysis supporting decisions while preserving traceability, uncertainty, and accountability.  
**Evidence sufficiency:** Adequacy of evidence relative to a decision, its stakes, and requirements.  
**Objective:** Desired outcome or criterion used to assess alternatives.  
**Recommendation:** Analytical proposal that is not itself authorization.  
**Scenario:** Coherent set of assumed conditions used to examine possible consequences.  
**Sensitivity analysis:** Examination of how conclusions change when inputs, assumptions, or preferences vary.

## Selected references and related work

These sources inform causal reasoning and decision analysis. They are included to situate the proposed architecture, not to imply that a graph or a model output alone identifies causal effects.

1. Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press. https://www.cambridge.org/9780521895606 — Structural causal models, interventions, and causal reasoning.
2. Hernán, M. A., & Robins, J. M. (2020). *Causal Inference: What If*. Chapman & Hall/CRC. https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/ — Causal inference methods, assumptions, and longitudinal data.
3. Keeney, R. L., & Raiffa, H. (1976). *Decisions with Multiple Objectives: Preferences and Value Tradeoffs*. Wiley. https://doi.org/10.1017/CBO9781139174084 — Objectives, constraints, and preference-sensitive decision analysis.
4. Howard, R. A. (1966). Information Value Theory. *IEEE Transactions on Systems Science and Cybernetics, 2*(1), 22–26. https://doi.org/10.1109/TSSC.1966.300074 — The value of information in decisions under uncertainty.

## Appendix D — Publication integrity statement

This document presents a preliminary research framework developed within the KSEL programme at H3XYN LAB. Its architecture, node types, relationships, workflows, hypotheses, and evaluation methods are proposals for investigation.

No empirical validation, benchmark result, production deployment, certification, or demonstrated performance is claimed. Illustrative examples are hypothetical. Causal effects must not be inferred from association, graph connectivity, or model output alone. Future empirical claims should include reproducible methods, evidence, limitations, and independent scrutiny.

---

**End of KSEL Research Note 005**

**Suggested citation**

H3XYN LAB. (2026). *KSEL Research Note 005: Decision Intelligence, Causal Reasoning, and Evidence-Based Decision Systems* (Version 0.1.0). H3XYN LAB Technical Research Notes. https://github.com/Hexynlab/ksel-research-note-001

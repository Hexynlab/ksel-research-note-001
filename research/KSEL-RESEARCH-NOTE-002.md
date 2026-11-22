# KSEL Research Note 002
## Cost-Aware Evidence Selection and Adaptive Review Governance

**Publication series:** HEXYN LAB — Technical Research Notes  
**Document identifier:** KSEL-RN-002  
**Version:** 0.1.0  
**Status:** Preliminary research framework  
**Date:** 22 November 2026  
**Maintained by:** HEXYN LAB  
**Research area:** Evidence selection, decision theory, uncertainty management, review governance

---

## Abstract

Evidence-intensive intelligent systems operate under practical constraints: retrieval has a cost, verification consumes time, reviewers have limited capacity, and decisions may lose value while information is being gathered. Indiscriminate evidence collection can become expensive without materially improving a decision. Premature stopping can produce recommendations that are inadequately supported.

This note develops a proposed KSEL approach to cost-aware evidence selection and adaptive review governance. It frames evidence acquisition as a decision-focused process: identify the uncertainty that matters to a decision, select information-gathering actions likely to reduce that uncertainty, estimate their costs and potential consequences, and determine whether further review is justified. It defines review escalation, stopping conditions, evidence sufficiency, and reassessment triggers.

The approach distinguishes information value from source quality, model confidence, and procedural compliance. Mandatory evidence and safety requirements are treated as constraints that cannot be traded away through a favourable cost calculation. The note proposes testable hypotheses and an evaluation protocol. No experimental results or validated performance claims are asserted.

**Keywords:** evidence selection; value of information; decision theory; adaptive review; uncertainty; evidence sufficiency; governance; intelligent systems

---

## 1. Introduction

Evidence governance requires more than collecting sources and recording citations. An operational system must also decide what to investigate, what to verify, when to request additional review, and when available evidence is sufficient for a particular purpose.

Evidence acquisition is not free. Potential costs include direct financial or service costs, retrieval and computational expenditure, analyst and reviewer time, decision delay, privacy and security exposure, and operational complexity. The benefit of additional evidence is uncertain: a new source may resolve a decisive ambiguity, reveal a contradiction, or have no effect on the eventual decision.

The value of an information-gathering action therefore depends on the decision context, not simply on the amount of information it produces.

KSEL Research Note 001 established a proposed evidence-governance foundation: traceable claims, provenance, explicit uncertainty, review states, and a conceptual cost-aware Value of Information (VOI) procedure. This note develops the operational decision logic around that procedure.

### 1.1 Research question

How can an intelligent system prioritize evidence acquisition and review effort according to expected decision benefit, uncertainty, consequence, and resource cost, while preserving mandatory evidence and oversight requirements?

### 1.2 Intended contribution

This note proposes:
1. A decision-centred evidence selection model.
2. A structured representation of candidate evidence actions.
3. A cost-aware VOI formulation.
4. Adaptive review escalation rules.
5. Evidence sufficiency and stopping criteria.
6. A governance protocol for exceptions and reassessment.
7. An empirical evaluation programme.

These are design proposals for investigation, not validated algorithms.

## 2. Relationship to KSEL Research Note 001

Research Note 001 defines the evidence lifecycle and the governance objects required to inspect an output. Research Note 002 addresses the allocation problem that arises within that lifecycle.

| Research Note 001 | Research Note 002 extension |
|---|---|
| Evidence registry | Candidate evidence-action catalogue |
| Claim-to-evidence mapping | Decision-relevant evidence prioritization |
| Uncertainty register | Decision-sensitive uncertainty assessment |
| Review gates | Adaptive escalation and reviewer allocation |
| Cost-aware VOI concept | Explicit action-level decision procedure |
| Release states | Evidence sufficiency and stopping conditions |
| Reassessment triggers | Change-driven review prioritization |

The second note does not replace the first. It assumes the evidence and review records described in RN-001 are available, or that an implementation provides equivalent traceability.

## 3. Decision-centred evidence acquisition

### 3.1 Start with the decision, not the search

A search process should begin with a defined decision or claim. Without that context, relevance is difficult to assess and additional information can accumulate without a clear purpose.

A decision context should specify the decision to be made, available actions or outcomes, claims material to the decision, time horizon, consequences of error or delay, required evidence and review constraints, and the accountable decision owner.

The same evidence item may have high value for one decision and negligible value for another.

### 3.2 Decision-relevant uncertainty

Not every uncertainty deserves equal investigation. An uncertainty is decision-relevant when resolving it could plausibly change the preferred action, estimated consequences, satisfaction of a mandatory condition, need for escalation, or timing and reversibility of the decision.

KSEL should distinguish uncertainty present in the system from uncertainty material to the current decision. This distinction must not be used to hide uncertainty. Other limitations may still need disclosure where they affect interpretation, future reuse, or downstream reliance.

### 3.3 Candidate evidence actions

The unit of prioritization is an evidence-gathering or verification action, not an abstract source count.

Examples include retrieving an authoritative record, checking a source's date or version, obtaining independent corroboration, verifying a disputed measurement, asking a qualified reviewer to inspect a claim, testing a calculation or transformation, or obtaining missing context from an authorized data owner.

Each candidate action should state the uncertainty or claim it is intended to address.

## 4. Evidence-action record

A candidate action should be registered before execution where practical.

| Field | Description |
|---|---|
| Action ID | Stable identifier |
| Decision ID | Decision or assessment being supported |
| Target claims | Claims affected by the action |
| Uncertainty references | Uncertainty entries the action may reduce |
| Action type | Retrieval, verification, corroboration, review, test, or other |
| Expected information | What the action may reveal |
| Source or method | Intended source, tool, reviewer, or procedure |
| Expected decision effect | How the result could change the decision |
| Direct cost | Monetary or service cost |
| Resource cost | Compute, analyst, and reviewer effort |
| Delay cost | Cost associated with waiting |
| Privacy/security impact | Additional exposure or access requirements |
| Mandatory status | Whether the action is required by policy or safety constraints |
| Dependencies | Prerequisites or other actions |
| Outcome | Completed, unavailable, inconclusive, failed, or deferred |
| Actual cost | Observed cost and effort |
| Resulting evidence IDs | Evidence records created or updated |

An action that returns no useful information is still a valid recorded outcome. Failed retrievals, unavailable sources, and inconclusive checks must not disappear from the audit trail.

## 5. Cost-aware Value of Information

### 5.1 Conceptual formulation

Let D denote the decision context, A the available decision actions, X the current evidence and uncertainty state, Yₐ the possible result of information-gathering action a, and U(d, θ) the utility of decision d under state θ.

A conventional decision-theoretic expression for the expected value of sample information can be represented as:

\[
\operatorname{EVSI}(a)
=
\mathbb{E}_{Y_a \mid X}
\left[
\max_{d \in A}
\mathbb{E}[U(d,\theta)\mid X,Y_a]
\right]
-
\max_{d \in A}
\mathbb{E}[U(d,\theta)\mid X]
\]

A simplified net-value expression is:

\[
\operatorname{NetVOI}(a)
=
\operatorname{EVSI}(a)
-
C_{\text{acquisition}}(a)
-
C_{\text{analysis}}(a)
-
C_{\text{review}}(a)
-
C_{\text{delay}}(a)
\]

This formulation is conceptual. Numeric estimation requires a defensible probability model, a defined utility function, appropriate cost units, and evidence that estimates are sufficiently calibrated for the intended use.

Where these requirements cannot be met, the system should use qualitative prioritization and record the rationale rather than outputting unsupported precision.

### 5.2 Costs are not always interchangeable

Monetary cost, elapsed time, reviewer capacity, privacy exposure, and safety risk should not automatically be collapsed into one scalar.

Some are hard constraints:
- A required independent review cannot be skipped because it is expensive.
- A prohibited data source cannot become acceptable because it has high expected value.
- A safety-critical verification cannot be removed by a low estimated VOI.
- Privacy and access restrictions remain binding regardless of expected decision benefit.

A practical implementation may use a multi-criteria decision procedure, constrained optimization, or a combination of mandatory rules and economic prioritization.

### 5.3 Avoiding false precision

VOI estimates are vulnerable to poorly calibrated probabilities, incomplete outcome spaces, underestimated delay or review costs, correlated sources treated as independent, utility functions that omit important harms, selection bias in historical examples, and uncertainty about the effectiveness of an acquisition action.

Implementations should expose assumptions, ranges, sensitivity analyses, and qualitative caveats. A point estimate should not be presented as objective truth.

## 6. Evidence prioritization

### 6.1 Priority dimensions

Candidate actions should be evaluated across at least these dimensions:

1. **Decision sensitivity:** Could the result change the preferred decision?
2. **Consequence:** How serious would an incorrect decision be?
3. **Uncertainty reduction:** How much relevant uncertainty might be resolved?
4. **Evidence independence:** Would the action provide genuinely new information?
5. **Source suitability:** Is the proposed source or method fit for the claim?
6. **Timeliness:** Can the result arrive before the decision loses value?
7. **Cost and burden:** What resources and delay are required?
8. **Constraint status:** Is the action mandatory, prohibited, or conditional?

These dimensions should be documented separately before any aggregation.

### 6.2 Practical priority classification

| Priority | Typical condition | Default handling |
|---|---|---|
| Critical | May resolve a high-consequence uncertainty or mandatory condition | Escalate and act before release where required |
| High | Could materially change the decision or expose a significant contradiction | Prioritize |
| Medium | Improves support or narrows a relevant limitation | Schedule according to capacity |
| Low | Unlikely to affect the current decision | Defer, document, or omit with rationale |
| Prohibited | Violates legal, privacy, security, or policy constraints | Do not perform |

This classification is a proposed operational aid. Organizations must define thresholds and decision rights for their context.

### 6.3 Independence and information overlap

Multiple sources do not necessarily provide multiple independent confirmations. They may repeat the same original report, rely on a common dataset, or share a methodological weakness.

KSEL should record source lineage and known dependencies. Correlated evidence must not be counted as independent corroboration without justification.

## 7. Adaptive review governance

### 7.1 Review is a resource-allocation decision with constraints

Review effort should increase when the consequence of error, uncertainty, or potential for irreversible harm increases. Adaptation must occur within pre-established governance boundaries.

A review controller should consider intended use and decision impact, unresolved material uncertainty, evidence quality and independence, contradictions and missing information, reversibility and downstream reliance, reviewer competence and independence, and mandatory oversight requirements.

### 7.2 Proposed review tiers

| Tier | Review mode | Illustrative conditions |
|---|---|---|
| Tier 0 | Automated checks and traceability validation | Low-impact, reversible, well-bounded tasks |
| Tier 1 | Targeted human review | Material claims or moderate uncertainty require inspection |
| Tier 2 | Independent specialist review | High consequence, disputed evidence, or complex interpretation |
| Tier 3 | Formal governance escalation | Critical impact, unresolved safety concerns, policy exception, or authority conflict |

These tiers are illustrative. They are not a universal risk taxonomy, and automated checks do not establish substantive correctness.

### 7.3 Escalation triggers

Escalation should occur when defined conditions are met, such as a critical claim lacking adequate evidence, materially conflicting independent sources, an unverifiable required source, uncertainty exceeding the permitted level, expired or superseded evidence, operation outside a validated scope, potentially irreversible harm, uncertain reviewer competence, or an incomplete mandatory control.

The system should record the trigger, affected claims, escalation destination, and resulting disposition.

### 7.4 Human review quality

Human review is not automatically reliable. Reviewers may lack domain competence, share assumptions, experience workload pressure, or be influenced by automation bias.

A governance design should specify reviewer qualifications, independence requirements, access to underlying evidence, disclosure of model-generated recommendations, a documented challenge and override process, and periodic review of reviewer agreement and error patterns.

## 8. Evidence sufficiency and stopping conditions

### 8.1 Sufficiency is purpose-specific

There is no universal quantity of evidence that makes a claim sufficiently supported. Sufficiency depends on the claim, intended use, consequence, applicable standards, and unresolved uncertainty.

A KSEL evidence sufficiency assessment should ask:

1. Are all material claims identified?
2. Is the provenance of relied-upon evidence inspectable?
3. Is the evidence relevant to the exact claim and scope?
4. Are source limitations and dependencies understood?
5. Have material contradictions been resolved or disclosed?
6. Is remaining uncertainty acceptable for the intended use?
7. Have mandatory checks and reviews been completed?
8. Are limitations and conditions visible to downstream users?

A positive answer is not a guarantee of correctness. It records that defined criteria were assessed for a particular output and version.

### 8.2 Proposed stopping conditions

Further evidence acquisition may stop when mandatory evidence and review requirements are satisfied; remaining uncertainty is within the approved tolerance; no feasible information action is expected to materially change the decision; expected benefit is lower than justified acquisition and review cost; delay would create greater expected harm than the information could reasonably prevent; or a governance authority explicitly accepts a documented limitation.

Stopping is not permitted merely because a search budget has been exhausted. If minimum evidence requirements remain unmet, the correct state may be defer, qualify, escalate, or reject.

### 8.3 Stop, defer, or escalate

- **Stop:** Defined evidence and review criteria are met for the intended use.
- **Defer:** More information is needed, but it is not currently available or timely.
- **Escalate:** A human or governance authority must resolve a material issue.
- **Qualify:** A restricted output may be released with explicit limitations, if policy permits.
- **Reject:** The output does not meet required conditions and must not be used as approved.

These states must not be treated as interchangeable.

## 9. Reassessment and dynamic evidence validity

Evidence sufficiency is time-dependent. A conclusion may become unreliable when a source is corrected or withdrawn, new evidence contradicts an earlier claim, the underlying situation changes, a dataset or model version changes, a key assumption no longer holds, or the intended use expands beyond the original scope.

Each material output should have reassessment conditions. Triggers may be time-based, event-based, or change-based.

A reassessment process should identify the changed evidence or condition, determine which claims and decisions depend on it, evaluate materiality, reopen the necessary review scope while preserving dependencies, and record the new outcome and supersession relationship.

A fixed review interval may be useful, but it should not replace event-driven reassessment where material changes can occur between scheduled reviews.

## 10. Governance, accountability, and exceptions

### 10.1 Decision rights

An implementation should identify who may define mandatory evidence requirements, approve source classes and acquisition methods, set risk and uncertainty thresholds, authorize exceptions, approve consequential outputs, accept residual risk, and reopen or revoke a previous approval.

These responsibilities should not be assigned implicitly to a model.

### 10.2 Exception records

An exception should include the requirement not met, reason for the request, affected claims and intended use, known risks and uncertainty, compensating controls, approving authority and date, and expiry or reassessment condition.

An exception is not equivalent to satisfying the original requirement. The output must retain the exception status and restrictions.

### 10.3 Separation of duties

For high-consequence use, the person or process generating an output may need to be separated from the party approving it. The degree of separation should reflect the threat model, organizational structure, and applicable obligations.

## 11. Security, privacy, and responsible acquisition

Evidence selection can itself create risk. Additional collection may increase exposure of personal or confidential information, expand the attack surface, or introduce malicious content.

Before an acquisition action is performed, the system should consider whether the data is necessary, whether the source is authorized, whether collection is proportionate, whether sensitive information is involved, whether access and retention controls are adequate, and whether source content may contain prompt injection or adversarial instructions.

A high-value information action is not automatically permissible. Acquisition must comply with applicable privacy, security, contractual, and legal requirements.

## 12. Evaluation programme

The proposed approach requires controlled evaluation. The following hypotheses are intended to be falsifiable.

**H1 — Decision relevance:** Decision-centred evidence selection reduces the proportion of acquired evidence that reviewers judge irrelevant to the stated decision, compared with an unconstrained retrieval workflow.

**H2 — Resource efficiency:** Cost-aware prioritization reduces evidence-acquisition and review effort while maintaining or improving predefined decision-quality and governance outcomes.

**H3 — Escalation sensitivity:** Explicit escalation triggers improve detection of high-consequence unresolved uncertainties and material evidence conflicts.

**H4 — Stopping discipline:** Purpose-specific sufficiency criteria reduce premature release and unnecessary continued acquisition relative to a documented baseline.

**H5 — Reassessment effectiveness:** Change-driven reassessment triggers reduce the time between material evidence changes and review of affected outputs.

These hypotheses have not been tested in this publication.

### 12.1 Experimental conditions

A proposed study may compare:

- **Baseline condition:** The organization's documented current evidence and review workflow.
- **Structured condition:** KSEL evidence records and claim mapping, without adaptive prioritization.
- **Adaptive condition:** Structured KSEL controls plus cost-aware evidence selection and review escalation.

The same task sets, source access, and acceptance criteria should be used across conditions where practical. Task allocation should be randomized or counterbalanced when feasible.

### 12.2 Outcome measures

| Measure | Definition |
|---|---|
| Decision quality | Performance against independently defined outcome criteria |
| Evidence relevance | Proportion of acquired evidence judged relevant to the decision |
| Unsupported claim rate | Material claims lacking adequate support under the rubric |
| Mandatory-control completion | Proportion of required checks completed before release |
| Escalation recall | Proportion of seeded or independently identified escalation conditions detected |
| Premature release rate | Outputs released before required conditions are met |
| Acquisition effort | Time, monetary cost, and compute used to obtain evidence |
| Review effort | Human and automated review resources consumed |
| Reassessment latency | Time from material change to review of affected output |
| Calibration | Agreement between predicted information or decision effects and observed outcomes, where probabilistic estimates are used |

Evaluation should report sample size, task design, reviewer expertise, measurement definitions, uncertainty intervals, missing data, and deviations from protocol. Trade-offs should be reported rather than hidden inside a composite score.

### 12.3 Ablation and stress testing

Ablation studies should examine the contribution of decision-centred uncertainty mapping, source independence tracking, cost and delay estimates, mandatory constraint handling, review escalation, evidence sufficiency criteria, and change-driven reassessment.

Stress tests should include misleading sources, correlated reports, stale records, contradictory evidence, unavailable sources, adversarial source content, and time-constrained decisions.

## 13. Limitations and open questions

The proposed model faces important limitations:

1. Expected decision benefit may be difficult to estimate when outcomes are rare or delayed.
2. Utility functions may fail to represent distributional effects or harms to different stakeholders.
3. Cost estimates may omit organizational friction and opportunity cost.
4. Source independence can be difficult to determine.
5. Qualitative priority categories may produce inconsistent results without clear rubrics.
6. Adaptive review can create automation bias if users treat system-assigned tiers as authoritative.
7. A stopping rule may be exploited to rationalize insufficient investigation.
8. Review capacity constraints may create inequitable or inconsistent access to scrutiny.

Further research is needed on robust VOI under model uncertainty, multi-stakeholder utility, reviewer workload, uncertainty propagation, and governance under changing operating conditions.

## 14. Conclusion

Cost-aware evidence governance is not a mandate to minimize research or review. It is a proposal to direct limited resources toward information that matters to a defined decision, while preserving mandatory controls and making residual uncertainty visible.

KSEL Research Note 002 extends the evidence-governance foundation of RN-001 with a decision-centred acquisition model, action-level cost accounting, adaptive review tiers, purpose-specific evidence sufficiency, and explicit stopping and reassessment states.

The central principle is that evidence acquisition should be purposeful, review should be proportionate but constrained by non-negotiable requirements, and stopping should be justified by documented criteria rather than convenience.

The framework remains a research proposal. Its benefits, limitations, and operational risks must be established through transparent implementation and independent evaluation.

---

## Appendix A — Evidence-action decision worksheet

For each proposed action, record the decision and affected claims; uncertainty to be addressed; expected information outcome; potential decision change; source suitability and independence; direct, analytical, review, and delay costs; privacy and security considerations; mandatory or prohibited status; expected and actual result; evidence records created; and follow-up or reassessment requirement.

## Appendix B — Release and stopping checklist

- [ ] Decision, scope, and intended use are explicit.
- [ ] Material claims and decision-relevant uncertainties are identified.
- [ ] Candidate evidence actions have documented purposes.
- [ ] Mandatory evidence and review requirements are satisfied.
- [ ] Source dependencies and contradictions are assessed.
- [ ] Review tier and escalation conditions are appropriate.
- [ ] Remaining uncertainty is acceptable for the defined use, or is disclosed.
- [ ] Stopping rationale is documented.
- [ ] Exceptions are authorized and visible.
- [ ] Reassessment triggers and ownership are defined.

## Appendix C — Suggested implementation event types

An implementation may record events such as:

- decision_context_created
- evidence_action_proposed
- evidence_action_authorized
- evidence_action_completed
- evidence_action_failed
- evidence_record_created
- uncertainty_updated
- review_escalated
- review_completed
- exception_requested
- exception_authorized
- release_qualified
- release_approved
- release_rejected
- reassessment_triggered
- output_superseded

Event names are illustrative. Implementations should define stable schemas, actor identity, timestamps, object versions, and integrity controls.

## Appendix D — Terminology

**Candidate evidence action:** A proposed retrieval, verification, corroboration, test, or review intended to provide information relevant to a defined decision.

**Decision-relevant uncertainty:** An unresolved uncertainty that could plausibly affect a decision, its consequences, or the governance required for its use.

**Expected Value of Sample Information (EVSI):** The expected improvement in decision value from obtaining a sample of additional information before choosing an action.

**Net Value of Information (NetVOI):** An estimate of information-related decision benefit after accounting for acquisition, analysis, review, and delay costs, subject to mandatory constraints.

**Evidence sufficiency:** A purpose-specific assessment that defined evidence and review criteria have been met for a particular claim or output.

**Adaptive review:** A review process that allocates scrutiny according to defined risk, uncertainty, and governance conditions.

**Stopping condition:** A documented criterion for ending evidence acquisition, deferring a decision, escalating an issue, or releasing a qualified output.

---

## Selected references and related work

These sources inform the decision-theoretic and governance concepts discussed here. They do not establish a universally valid VOI formula or validate the KSEL proposals.

1. Howard, R. A. (1966). Information Value Theory. *IEEE Transactions on Systems Science and Cybernetics, 2*(1), 22–26. https://doi.org/10.1109/TSSC.1966.300074 — Foundational treatment of the decision value of information.
2. Keeney, R. L., & Raiffa, H. (1993). *Decisions with Multiple Objectives: Preferences and Value Tradeoffs*. Cambridge University Press. https://doi.org/10.1017/CBO9781139174084 — Multi-objective decision analysis and explicit value trade-offs.
3. National Institute of Standards and Technology. (2023). *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. NIST AI 100-1. https://doi.org/10.6028/NIST.AI.100-1 — Risk-based governance and context-sensitive management.
4. Hernán, M. A., & Robins, J. M. (2020). *Causal Inference: What If*. Chapman & Hall/CRC. https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/ — A reference for distinguishing decision evidence, causal assumptions, and uncertainty.

## Publication and integrity statement

This document presents a proposed research framework. It does not report completed validation experiments, establish a universally applicable VOI method, certify an implementation, or claim compliance with an external standard. Numerical decision-theoretic expressions are conceptual unless supported by calibrated models and validated data. Future empirical work should publish methods, assumptions, baselines, evaluation criteria, limitations, and reproducibility information sufficient for independent scrutiny.

**Suggested citation**

HEXYN LAB. (2026). *KSEL Research Note 002: Cost-Aware Evidence Selection and Adaptive Review Governance* (Version 0.1.0). HEXYN LAB Technical Research Notes. https://github.com/Hexynlab/ksel-research-note-001

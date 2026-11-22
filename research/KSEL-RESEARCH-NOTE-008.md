# KSEL Research Note 008

## Empirical Evaluation of Evidence Governance in Intelligent Systems

**Subtitle:** Benchmark Design, Experimental Methods, and Comparative Performance Assessment  
**Series:** KSEL — Knowledge, Source, Evidence Layer  
**Institution:** H3XYN LAB  
**Publication type:** Preliminary experimental protocol  
**Version:** 0.1.0  
**Date:** 22 November 2026  
**Status:** Proposed protocol; no experiments or empirical findings are reported

---

## Abstract

KSEL proposes mechanisms for evidence provenance, uncertainty representation, source-dependence analysis, temporal validation, review governance and controlled knowledge revision. The existence of these mechanisms does not establish that they improve system performance. Their value must be tested against explicit baselines under controlled conditions.

This note defines a proposed empirical programme for evaluating selected KSEL mechanisms. It specifies research questions, comparison conditions, scenario families, candidate metrics, controls, ablation studies, reporting requirements and threats to validity. The programme is designed to test both intended benefits and potential costs, including review burden, latency, false rejection of useful evidence, missed updates and added operational complexity.

The protocol does not report completed experiments, benchmark scores or validated performance. Dataset construction, operational definitions, baseline implementations and acceptance thresholds must be finalised and versioned before confirmatory testing. Results should include positive, negative and inconclusive outcomes.

**Keywords:** evidence governance, empirical evaluation, benchmark design, provenance, uncertainty, source dependence, temporal validation, review governance, reproducibility.

---

## 1. Research problem

Intelligent systems may generate claims from sources that are incomplete, duplicated, stale, dependent, manipulated or incorrectly interpreted. Governance mechanisms are intended to make these processes more inspectable and controllable. However, additional controls may also increase latency, cost, complexity and human review burden.

The central question is therefore not whether a system contains governance components, but whether defined components produce measurable improvements under specified conditions and at acceptable cost.

### 1.1 Primary research question

Under controlled evaluation conditions, do selected KSEL governance mechanisms improve evidence traceability, provenance handling, uncertainty management, temporal validity and revision quality compared with clearly specified non-governed or partially governed baselines?

### 1.2 Secondary questions

1. Which individual mechanisms contribute measurable benefit?
2. Which combinations produce interaction effects?
3. Do the mechanisms reduce false acceptance without causing unacceptable false rejection?
4. Can systems identify dependent sources and avoid false corroboration?
5. Do temporal controls improve detection of stale or superseded evidence?
6. Do review controls improve decision reconstruction and authorization compliance?
7. What operational overhead is introduced?
8. How robust are the results across domains, tasks and evidence distributions?

### 1.3 Scope boundaries

This protocol evaluates defined evidence-governance tasks. It does not claim to measure general intelligence, establish universal safety, prove truth, or certify a system. Results from one task or domain must not be generalised beyond the tested conditions without additional evidence.

---

## 2. Evaluation principles

The evaluation programme should follow these principles:

- **Falsifiability:** each hypothesis must admit an observable outcome that could contradict it.
- **Comparability:** baselines and treatment conditions must be clearly specified.
- **Isolation:** ablations should separate component effects where feasible.
- **Symmetry:** measure false acceptance and false rejection, not only one error type.
- **Cost awareness:** measure latency, compute, review effort and implementation complexity.
- **Traceability:** preserve exact versions of data, models, prompts, policies and evaluation code.
- **Predefinition:** define primary metrics and analysis procedures before confirmatory runs.
- **Transparency:** report deviations, failures, null results and limitations.
- **Safety and privacy:** do not release sensitive data or unsafe operational details in the name of reproducibility.

---

## 3. Proposed hypotheses

These hypotheses are proposed for testing and are not findings.

### H1 — Evidence-to-claim traceability

Systems using explicit evidence-to-claim records will produce more complete and accurate traceability than systems relying on unstructured references or final answers alone.

**Primary outcome:** traceability completeness and correctness under a predefined annotation rubric.

### H2 — Provenance and integrity assessment

Systems using provenance and integrity checks will identify more manipulated, unverifiable or contextually invalid evidence than systems without those checks, subject to an acceptable false-rejection rate.

**Primary outcomes:** detection sensitivity, specificity, false-acceptance rate and false-rejection rate.

### H3 — Source-dependence governance

Systems tracking lineage and source dependence will make fewer false-corroboration errors when multiple reports derive from a common upstream source.

**Primary outcome:** false-corroboration rate.

### H4 — Temporal validation

Systems using explicit temporal metadata and freshness policies will identify more stale, superseded or temporally inapplicable evidence than systems using publication or ingestion time alone.

**Primary outcomes:** stale-evidence detection and valid-evidence retention.

### H5 — Uncertainty and contradiction handling

Systems representing uncertainty dimensions and preserving unresolved contradictions will produce better-calibrated assessments and fewer unjustified certainty claims than systems using a single undifferentiated confidence value.

**Primary outcomes:** calibration error, contradiction preservation and unsupported certainty rate.

### H6 — Review governance

Systems using explicit review states and authorization gates will produce more complete decision histories and fewer unauthorized state transitions than systems without those controls.

**Primary outcomes:** audit reconstruction accuracy and unauthorized transition rate.

### H7 — Cost-effectiveness

The benefits of selected governance mechanisms will vary by task risk, evidence complexity and consequence level; a context-sensitive review policy will achieve a more favourable quality-cost trade-off than a uniform review policy.

**Primary outcomes:** quality-cost frontier, review effort and error severity.

### H8 — Integrated governance

A defined combination of KSEL mechanisms will improve a preregistered composite of evidence-governance outcomes compared with a baseline, without unacceptable deterioration in predefined safety, privacy or operational constraints.

**Primary outcome:** preregistered composite score, with all component outcomes also reported separately.

---

## 4. Experimental conditions

The normative comparison conditions for RN-008 are defined in [the Baseline and Treatment Protocol](../benchmark/BASELINE-AND-TREATMENT-PROTOCOL.md). That document is the controlling specification for condition names and fairness controls.

In summary:

- **B0 — Task-native baseline:** a capable system performs the task using its ordinary workflow, with outputs mapped to the common prediction contract by a documented, non-reasoning adapter.
- **B1 — Basic source-metadata baseline:** the same task is performed with ordinary source identifiers and available metadata, but without the selected KSEL governance workflow.
- **K1 — KSEL governance treatment:** a versioned implementation of the selected KSEL mechanisms, with the exact active controls and human-authorized actions documented.

K1 is an experiment-specific treatment, not a claim that one complete immutable KSEL implementation already exists. Where feasible, use ablations to isolate selected mechanisms. Do not mix the older K1–K7 shorthand in this note with separate condition definitions; identify individual components and ablations within the registered study.

No B0, B1 or K1 implementation is claimed to exist or to have been run as part of this protocol.

## 5. Scenario and test-set design

Construct controlled test sets containing the following scenario families:

1. **Clean evidence:** relevant, authentic and temporally applicable material.
2. **Missing provenance:** content with incomplete or unverifiable source history.
3. **Manipulated evidence:** altered content or metadata with ground-truth labels.
4. **Duplicate evidence:** repeated copies of the same underlying source.
5. **Dependent evidence:** multiple reports derived from one upstream origin.
6. **Conflicting evidence:** sources that disagree in material ways.
7. **Stale evidence:** previously valid material that has become outdated.
8. **Superseded evidence:** a source or claim replaced by a newer authoritative version.
9. **Context mismatch:** authentic evidence applied outside its valid population, location, domain or time.
10. **Prompt-injection content:** untrusted instructions embedded in material intended to be treated as evidence.
11. **Self-generated evidence:** prior system outputs reintroduced as if they were independent observations.
12. **Incomplete evidence:** cases where the correct outcome is uncertainty, deferral or no conclusion.

Each scenario should have a documented expected property or adjudication rubric. Ambiguous cases should be labelled as ambiguous rather than forced into artificial ground truth.

### 5.1 Dataset composition

Dataset construction should define:

- Domain and task coverage.
- Sampling strategy and inclusion criteria.
- Number of cases per scenario family.
- Difficulty levels and expected error severity.
- Source and evidence provenance.
- Annotation instructions and adjudication process.
- Training, development and held-out test separation where applicable.
- Duplicate and leakage checks.
- Dataset version and change log.

No sample size is prescribed here. It must be justified by the research question, expected effect size, variability and available resources before confirmatory evaluation.

### 5.2 Annotation quality and independent adjudication

For any confirmatory dataset using human gold labels:

1. Use at least two annotators who label each relevant item independently before discussion.
2. Record each annotator's relevant domain experience, training and any conflicts of interest. Do not imply that a title alone establishes expertise.
3. Publish the annotation handbook, operational definitions, examples, allowed labels and decision rules before annotation.
4. Keep annotators blind to system condition and model outputs where feasible.
5. Preserve the original independent labels. Do not overwrite disagreement with a single undocumented consensus label.
6. Report raw agreement and an appropriate chance-corrected agreement statistic when its assumptions fit the label structure; explain exclusions and missing labels.
7. Send disagreements to a separately identified adjudicator or panel. Record the adjudication rationale and final label.
8. Retain an explicit ambiguous/uncertain/unresolved outcome. Do not force a binary source-dependence label when available evidence cannot justify one.
9. Distinguish author-created development annotations from independently reviewed or adjudicated confirmatory labels.

The current 15-case public synthetic fixture is hand-authored and has not undergone this independent annotation procedure. Its labels are development annotations, not externally established ground truth.

---

## 6. Metrics and operational definitions

Metrics must be classified by whether the current public evaluator can actually calculate them. Definitions and calculation rules for any confirmatory study must be frozen before testing.

### 6.1 Operationalised by the current public evaluator

The evaluator currently calculates:

- traceability-link micro precision, recall and F1;
- invalid-evidence detection precision, recall and F1;
- valid-evidence retention;
- false-acceptance rate;
- stale-evidence detection recall;
- dependent-pair and independent-pair precision, recall and F1 over explicitly annotated pairs;
- false-independence and false-dependence rates over explicitly annotated gold pairs;
- contradiction-preservation precision, recall and F1;
- exact-match decision-status accuracy against case-specific expected labels;
- review and authorization compliance.

These measures are calculated against the hand-authored annotations in the public 15-case development fixture. They do not establish factual truth, general reasoning ability or real-world effectiveness.

### 6.2 Proposed but not operationalised by the current evaluator

The following remain research outcomes requiring additional instrumentation, data structures, measurement protocols and/or independent human assessment:

| Proposed outcome | Additional requirement |
|---|---|
| Provenance detection sensitivity/specificity beyond current invalid-evidence labels | Explicit provenance-failure taxonomy and adjudicated labels |
| Unsupported-certainty rate | Operational rubric for certainty claims and support sufficiency |
| Probabilistic calibration | Probability-bearing predictions, defined outcomes and calibration analysis |
| Audit reconstruction accuracy | Ordered event histories and a reconstruction rubric |
| Unauthorized state-transition rate | State-transition logs and authorization-event records |
| Human review burden | Time/effort instrumentation and a defined unit of work |
| Latency | Repeated timing under controlled execution conditions |
| Compute and monetary cost | Resource instrumentation and transparent cost assumptions |
| Regression rate | Versioned repeated-task comparisons and a predefined regression rule |
| Quality-cost frontier | Comparable quality and cost observations across registered conditions |

Do not report these proposed outcomes as if the current evaluator measures them. A study may add them only through a versioned schema, protocol and analysis plan.

### 6.3 Reporting discipline

Report operationalised metrics separately. Do not introduce an unregistered composite or imply that a single metric establishes overall superiority. Undefined denominators, missing observations and ambiguous labels must be handled according to the frozen analysis plan.

## 7. Experimental procedure

A proposed study should follow this sequence:

1. Finalise the research question, hypotheses and primary outcomes.
2. Publish or timestamp the protocol and analysis plan before confirmatory testing where feasible.
3. Define and version datasets, scenario labels and adjudication rules.
4. Specify baseline and treatment implementations.
5. Verify that each condition receives equivalent task inputs and comparable resources.
6. Run pilot tests to identify procedural defects; do not merge pilot outcomes into confirmatory results without disclosure.
7. Execute the predefined evaluation with recorded software, model and configuration versions.
8. Preserve raw outputs and logs subject to privacy and security controls.
9. Apply the predefined scoring and adjudication process.
10. Analyse primary outcomes, uncertainty and trade-offs.
11. Run planned ablations and robustness checks.
12. Document deviations, failed runs and exclusions.
13. Publish the results, limitations and reproducibility artefacts.

Where stochastic systems are evaluated, specify the number of repetitions, seed handling and aggregation procedure. Do not select only favourable runs.

---

## 8. Ablation and robustness programme

Ablations should remove or disable one mechanism at a time where feasible, including:

- Evidence-to-claim mapping.
- Provenance verification.
- Source-dependence tracking.
- Temporal validity checks.
- Multidimensional uncertainty.
- Contradiction preservation.
- Review and authorization gates.
- Post-update regression checks.

Robustness testing should vary evidence volume, source quality, duplication rate, conflict rate, temporal drift, domain and task consequence. Include realistic combinations of failure modes, not only isolated synthetic cases.

Ablation outcomes should be interpreted cautiously when components interact or when removing a component changes system behaviour in multiple ways.

---

## 9. Analysis plan

Before confirmatory testing, specify:

- Primary and secondary outcomes.
- Unit of analysis.
- Aggregation and weighting.
- Treatment of missing observations.
- Statistical tests or estimation methods.
- Confidence or credible intervals where appropriate.
- Multiple-comparison handling where relevant.
- Subgroup and scenario analyses.
- Practical significance thresholds.
- Criteria for inconclusive results.

Report effect sizes and uncertainty, not only thresholded significance values. Distinguish statistical significance from practical importance. Avoid causal claims where assignment, controls or study design do not support them.

---

## 10. Acceptance and failure criteria

Acceptance thresholds must be selected before confirmatory analysis and justified for the domain. This note intentionally does not invent universal numerical thresholds.

A treatment should not be described as beneficial solely because one metric improves. Assess whether it causes unacceptable deterioration in:

- False rejection of valid evidence.
- Missed material updates.
- Privacy or security compliance.
- Safety or mandatory review requirements.
- Calibration or uncertainty representation.
- Latency, cost or review burden.
- Performance on previously supported tasks.

A study may conclude that a mechanism is ineffective, too costly, harmful under some conditions, or useful only in a restricted domain. Such findings are valid research outcomes.

---

## 11. Reproducibility requirements

A completed evaluation report should include, where safe and lawful:

- Protocol version and date.
- Dataset description, provenance and access conditions.
- Scenario generation or sampling procedures.
- Annotation rubric and adjudication procedure.
- Baseline and treatment specifications.
- Model, prompt, policy and software versions.
- Configuration and dependency manifests.
- Evaluation scripts and synthetic fixtures.
- Metric definitions and analysis code.
- Raw or suitably aggregated results.
- Deviations and failed-run records.
- Limitations and threats to validity.

If artefacts cannot be released, state the restriction and describe the impact on independent reproduction.

---

## 12. Threats to validity

The evaluation programme must consider:

1. **Construct validity:** metrics may not capture the intended governance property.
2. **Internal validity:** observed differences may result from uncontrolled implementation differences.
3. **External validity:** synthetic scenarios may not represent operational environments.
4. **Annotation validity:** labels may reflect evaluator assumptions or disagreement.
5. **Benchmark leakage:** systems may have encountered test material during development.
6. **Baseline weakness:** a poorly selected baseline can exaggerate apparent benefit.
7. **Metric gaming:** optimisation may improve measured outcomes while degrading unmeasured behaviour.
8. **Domain dependence:** results may vary substantially across fields and consequence levels.
9. **Resource confounding:** treatment systems may receive more time, compute or human attention.
10. **Version drift:** model or service updates may change results during the study.

These threats should be addressed in study design and discussed in every final report.

---

## 13. Planned outputs

The proposed programme may produce:

- A versioned benchmark specification.
- Synthetic evidence and provenance fixtures.
- Annotation and adjudication guidelines.
- Baseline and treatment implementations, where safe to release.
- Evaluation scripts and metric definitions.
- A preregistered or predeclared analysis plan.
- A results report including negative and inconclusive findings.
- An independent replication package.

These are planned outputs, not existing artefacts or completed deliverables.

---

## 14. Limitations

This protocol is not yet a validated benchmark. The scenario taxonomy, metrics and comparison conditions require review and refinement. Some properties, including source reliability and decision defensibility, may be difficult to reduce to a single objective label. Domain experts may disagree. A synthetic benchmark can test controlled failure modes but cannot establish real-world performance by itself.

The integrated KSEL treatment must be specified precisely enough to implement and compare. Until then, claims about the performance of the integrated architecture remain premature.

---

## 15. Conclusion

KSEL's proposed governance mechanisms should be judged by observable performance, not by architectural completeness or terminology. A credible evaluation must compare defined alternatives, isolate component contributions where possible, measure both error reduction and operational cost, and publish limitations and unfavourable results.

RN-008 establishes a proposed framework for that work. It makes no claim that experiments have been completed or that KSEL has demonstrated empirical effectiveness. The next scientific step is to finalise operational definitions, build and validate the test set, specify the baselines, and freeze the analysis plan before confirmatory evaluation.

---

## Selected references and related work

These works inform benchmark construction, documentation, reproducibility, and adaptive-system evaluation. They are methodological references, not evidence that KSEL has achieved any benchmark result.

1. Pineau, J., et al. (2021). Improving Reproducibility in Machine Learning Research: A Report from the NeurIPS 2019 Reproducibility Program. *Journal of Machine Learning Research, 22*(164), 1–20. https://www.jmlr.org/papers/v22/20-303.html — Reproducibility practices and reporting in machine-learning research.
2. Dodge, J., et al. (2019). Show Your Work: Improved Reporting of Experimental Results. In *Proceedings of EMNLP-IJCNLP 2019*, 2185–2194. https://doi.org/10.18653/v1/D19-1224 — Reporting experimental conditions and computational requirements.
3. Gebru, T., et al. (2021). Datasheets for Datasets. *Communications of the ACM, 64*(12), 86–92. https://doi.org/10.1145/3458723 — Dataset documentation and intended-use transparency.
4. Mitchell, M., et al. (2019). Model Cards for Model Reporting. *Proceedings of the Conference on Fairness, Accountability, and Transparency*, 220–229. https://doi.org/10.1145/3287560.3287596 — Documentation of model evaluation and limitations.
5. Gama, J., et al. (2014). A survey on concept drift adaptation. *ACM Computing Surveys, 46*(4), Article 44. https://doi.org/10.1145/2523813 — Evaluation of adaptation under changing data distributions.

## Publication and research integrity statement

This document is a preliminary experimental protocol developed for the KSEL research-note series of H3XYN LAB. Its hypotheses, scenario families, metrics, comparison conditions and procedures are proposals for investigation.

No experiment, benchmark result, statistical finding, independent review, production deployment or validation is claimed. Any future report must identify the exact protocol version used, disclose deviations and distinguish exploratory analysis from confirmatory findings.

**End of KSEL Research Note 008.**

**Suggested citation**

H3XYN LAB. (2026). *KSEL Research Note 008: Empirical Evaluation of Evidence Governance in Intelligent Systems* (Version 0.1.0). H3XYN LAB Technical Research Notes. https://github.com/Hexynlab/ksel-research-note-001

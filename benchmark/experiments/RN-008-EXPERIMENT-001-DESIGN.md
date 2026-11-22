# RN-008 — Experiment 001 Design

**Title:** Source-Lineage Tracking and False-Corroboration Errors  
**Study ID:** RN-008-EXP-001  
**Protocol status:** Proposed design; not preregistered  
**Version:** 0.1.0-draft  
**Date:** 22 November 2026  
**Institution:** HEXYN LAB

---

## 1. Purpose and scope

This document specifies a proposed first experiment under KSEL Research Note 008 (RN-008). It isolates the source-dependence question in hypothesis H3.

The experiment asks whether explicit source-lineage tracking reduces false claims of independent corroboration when multiple reports derive from a common upstream source.

This is a design document only. It does not report completed implementation, data collection, experimental runs, results, or validated KSEL effectiveness.

The experiment is intentionally narrower than the full RN-008 programme. It does not test all KSEL governance mechanisms or establish general system reliability.

## 2. Research question

**Primary research question:** Does explicit source-lineage tracking reduce false-independence classifications, and resulting false-corroboration errors, compared with task-native and basic source-metadata handling?

## 3. Hypotheses

### Primary hypothesis (H1-EXP001)

On a held-out dataset containing adjudicated source-dependence relationships, the KSEL source-lineage treatment (K1) will produce a lower false-independence rate than the task-native baseline (B0).

### Comparative hypothesis (H2-EXP001)

K1 will produce a lower false-independence rate than the basic source-metadata baseline (B1).

### Competing and null explanations

- There may be no measurable difference between conditions.
- Basic source identifiers or metadata may provide the same benefit as explicit lineage tracking.
- Explicit lineage tracking may reduce false-independence errors while increasing false-dependence errors or unresolved classifications.
- Performance may vary by lineage structure, evidence ambiguity, or source-history completeness.

These possibilities must remain reportable outcomes. No directional result is assumed.

## 4. Unit of analysis and scope

The primary unit of analysis is an **adjudicated evidence pair within a case** for which the gold annotation establishes source dependence.

The experiment will include cases with:
- direct copying or republication from a common source;
- multi-hop derivation chains;
- system-generated summaries derived from external evidence;
- conflicting source-lineage assertions;
- incomplete or ambiguous lineage, where neither dependence nor independence can be established;
- genuinely independent source pairs.

The primary analysis must not treat unlabelled or ambiguous pairs as independent. Ambiguous cases must be retained and reported separately.

## 5. Experimental conditions

Use the condition definitions in `benchmark/BASELINE-AND-TREATMENT-PROTOCOL.md` as the controlling specification.

- **B0 — Task-native baseline:** ordinary task workflow, without required KSEL-specific governance records.
- **B1 — Basic source-metadata baseline:** ordinary source identifiers and available metadata, without the selected explicit KSEL lineage-governance workflow.
- **K1 — KSEL source-lineage treatment:** a versioned implementation of explicit source-lineage representation and source-dependence classification.

For this experiment, K1 must be limited to the source-lineage mechanisms necessary to test H3. Other KSEL controls must either be held constant across conditions or excluded from the treatment. Any unavoidable differences must be documented.

No B0, B1, or K1 implementation is currently asserted by this design document to exist or to have been run.

## 6. Dataset requirements

The existing public synthetic development fixture may be used for engineering checks and evaluator validation only. It is not confirmatory test data and must not be represented as independently adjudicated ground truth.

A separate held-out dataset is required for confirmatory evaluation. Before use, its specification must document:

- domain and case-generation or sampling method;
- source and evidence construction process;
- lineage structures represented;
- inclusion and exclusion criteria;
- handling of duplicates, cycles, multi-hop derivations and conflicting lineage assertions;
- separation from development data and controls against leakage;
- licensing, privacy and security review;
- dataset version and immutable commit identifier.

### 6.1 Annotation and adjudication

Every confirmatory evidence pair used for gold-labelled dependence or independence scoring must be independently assessed by at least two annotators before discussion.

The annotation handbook must define:
- dependent;
- independent;
- ambiguous or insufficient information;
- conflicting lineage evidence;
- direct and transitive derivation;
- the evidence required to assign each label.

Annotators should be blinded to system condition and outputs where feasible. Preserve original labels, report disagreement and agreement statistics with their assumptions, and use a separately identified adjudicator or panel for disagreements. Retain adjudication rationales. Do not force uncertain pairs into binary labels.

Annotator qualifications, training and conflicts of interest must be recorded in the study materials.

## 7. Outcomes

### 7.1 Primary outcome

**False-independence rate:** the proportion of gold-labelled dependent evidence pairs that a system predicts as independent.

The existing evaluator exposes this as `false_independence_rate`. Its denominator is the number of adjudicated dependent pairs. The implementation and aggregation must be checked against the frozen dataset and prediction contract before confirmatory use.

### 7.2 Secondary outcomes

Report, at minimum:

- dependent-pair precision, recall and F1;
- independent-pair precision, recall and F1;
- false-dependence rate;
- unresolved/abstained classification rate, if supported by the frozen prediction contract;
- performance by lineage scenario family;
- invalid or unlabelled pair handling;
- latency and resource use, where measured.

A lower false-independence rate alone is not sufficient to establish overall superiority. False-dependence errors and the treatment's ability to retain genuinely independent pairs must be reported alongside it.

If the current prediction schema or evaluator cannot represent unresolved classifications, this limitation must be resolved and versioned before preregistration, not patched after confirmatory results are observed.

## 8. Fairness and execution controls

Apply the fairness controls in the RN-008 Baseline and Treatment Protocol. In particular, record and hold constant where the design permits:

- model family and exact version;
- task instructions and case inputs;
- external information access and tools;
- token/context, compute and time budgets;
- retry and sampling policy;
- execution environment;
- output contract and scoring code.

The adapter must not infer missing lineage, repair source histories, or add reasoning for one condition. Version and review adapter code independently from the systems being evaluated.

Record all deviations and failures. Do not silently discard failed runs or cases.

## 9. Analysis plan — items to freeze before preregistration

The following decisions remain open and must be justified and frozen before confirmatory runs:

1. Confirmatory dataset size and composition, with a sample-size rationale.
2. Exact system, model, prompt, adapter and code versions for B0, B1 and K1.
3. Randomisation or execution-order method and run/repetition policy.
4. Primary aggregation method and statistical uncertainty procedure, accounting for pairs clustered within cases where appropriate.
5. Missing-output and failed-run handling.
6. Practical significance threshold, if one is justified.
7. Multiple-comparison handling for secondary and subgroup analyses.
8. Stopping rule and criteria for declaring the result inconclusive.

No sample size, effect threshold, confidence interval, statistical test or stopping rule is asserted here as already selected.

## 10. Validity risks

Key threats include:

- synthetic or overly regular lineage patterns that make dependence unusually easy to detect;
- leakage between development fixtures and held-out cases;
- inconsistent human interpretations of dependence and independence;
- differences between conditions beyond the lineage-governance mechanism;
- adapter behaviour that unintentionally favours one condition;
- treating unavailable lineage information as proof of independence;
- improving one error type while worsening the other;
- insufficient coverage of real-world source histories.

The final study report must discuss these risks in light of the actual dataset and implementation.

## 11. Prerequisites and sequence

Confirmatory evaluation must not begin until the following are complete:

1. Review and approve this experiment design.
2. Define and version the annotation handbook.
3. Construct and independently annotate the held-out dataset.
4. Implement and version B0, B1 and K1.
5. Confirm that all conditions emit the same prediction contract.
6. Validate evaluator behaviour with hand-constructed test fixtures, including dependent, independent, ambiguous and conflicting lineage cases.
7. Freeze the analysis plan, sample-size rationale, execution controls and stopping rule.
8. Complete the RN-008 preregistration template and publish it before confirmatory runs.
9. Record immutable code and dataset identifiers.

Development runs may be used to debug systems and scoring, but must remain clearly separated from confirmatory evaluation.

## 12. Reporting commitments

Report:
- all registered primary and secondary outcomes;
- false-independence and false-dependence results together;
- unresolved and ambiguous cases;
- deviations, failed runs and missing outputs;
- uncertainty estimates and analysis limitations;
- negative, null and inconclusive findings;
- exact system, dataset, evaluator and protocol versions.

Do not claim that KSEL improves evidence governance beyond the tested task, dataset and conditions. Do not describe this experiment as completed until the work has actually been performed and documented.

## 13. Current status

**Proposed design only.** No confirmatory dataset, completed annotation, baseline implementation, K1 implementation, preregistration, experimental run or empirical result is claimed by this document.

This draft is intended for review and refinement before any preregistration or confirmatory work.

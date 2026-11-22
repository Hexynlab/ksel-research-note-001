# KSEL RN-008 — Benchmark Specification v0.2.0

**Status:** Development specification; not a validated benchmark  
**Owner:** HEXYN LAB  
**Related publication:** KSEL Research Note 008  
**Date:** 22 November 2026

## 1. Purpose

Define the 0.2.0 public development fixture and machine-readable prediction contract for testing selected KSEL evidence-governance tasks. This is an engineering specification for a small synthetic fixture, not a validated or confirmatory benchmark.

## 2. Unit of evaluation

The unit is one synthetic case containing:
- one or more claims;
- a set of evidence records;
- gold annotations for required claim-evidence links;
- gold valid and invalid evidence sets;
- known dependent-source pairs;
- known contradiction pairs;
- a review-required flag;
- an expected decision-status label for a coarse abstention/review outcome check.

A system processes each case and emits one prediction record conforming to `schemas/prediction.schema.json`. The prediction includes a coarse decision status: `supported`, `uncertain`, `unsupported` or `review_required`.

## 3. Development fixture

The v0.2.0 fixture at `data/dev/ksel-synthetic-dev-v0.2.jsonl` contains 15 hand-authored fictional cases covering:

- clean evidence and traceability;
- duplicated and source-dependent evidence;
- stale, superseded and context-mismatched evidence;
- provenance failure and incomplete provenance;
- contradictory evidence and conflicting source-history assertions;
- embedded untrusted instructions;
- system-generated evidence;
- insufficient causal evidence;
- review and authorization gates;
- ambiguous lineage requiring uncertainty or review;
- multi-hop source dependence.

The fixture is intended for smoke testing and evaluator development only. It is public, small, synthetic and not independently adjudicated. It is not a blind test set and cannot support claims about real-world prevalence, generalisation or system effectiveness.

## 4. Gold annotation model

Each case includes:
- `required_links`: claim/evidence relationships that should be retained for inspection;
- `valid_evidence_ids`: evidence considered admissible for the specific fictional task;
- `invalid_evidence_ids`: evidence that should not be accepted as valid support;
- `stale_evidence_ids`: evidence that is temporally stale or superseded;
- `dependent_pairs`: pairs that must not be counted as independent corroboration;
- `contradiction_pairs`: material contradictions that should remain visible;
- `review_required`: whether the case requires review and authorization records;
- `expected_decision_status`: case-specific expected decision state for a limited exact-match metric.

An evidence item may be valid yet insufficient to establish a claim. The labels are case-specific and do not imply that evidence validity alone proves the claim.

## 5. Prediction contract

A prediction contains the case ID, traceability links, accepted evidence IDs, flagged evidence IDs, independent source pairs, optional unresolved source pairs, contradiction pairs, review completion and authorization validity. Exact field names and types are defined in the JSON Schema.

Unknown or missing case IDs are errors. Duplicate prediction rows are errors. The evaluator does not silently impute missing predictions.

## 6. Metrics

The current deterministic evaluator operationalises the following measures:

- micro precision, recall and F1 for traceability links;
- precision, recall and F1 for invalid-evidence detection;
- valid-evidence retention;
- false-acceptance rate;
- stale-evidence detection recall;
- dependent-pair and independent-pair precision, recall and F1 over explicitly annotated pairs;\n- explicit unresolved-prediction rate and source-dependence classification coverage across all explicitly labelled pairs;
- false-independence and false-dependence rates over explicitly annotated gold pairs;
- contradiction-preservation precision, recall and F1;
- decision-status exact-match accuracy against the case-specific expected status;
- review and authorization compliance.

Unlabelled source pairs are not silently treated as independent or dependent; predictions for unlabelled pairs are rejected. Ambiguous and conflicting gold pairs are excluded from binary dependence metrics and reported separately. Explicit unresolved predictions are abstentions, not independence claims. Unresolved rate and classification coverage use all explicitly labelled gold pairs as the denominator; omitted labelled pairs reduce coverage but are not explicit unresolved predictions. PRF components with undefined denominators, including empty-empty categories, are null rather than perfect scores. No weighted composite is defined.

The RN-008 research programme also proposes outcomes such as calibration, unsupported-certainty rate, audit reconstruction, unauthorized state transitions, human review effort, latency, compute and monetary cost. These are **not operationalised by the current public evaluator**. They require additional schemas, event records, measurement procedures and/or human annotation before they can be reported. They must not be presented as current benchmark metrics.

## 7. Known limitations

- Small sample count and limited scenario diversity.
- Hand-authored rather than independently adjudicated labels.
- Synthetic, fictional, English-language examples.
- No domain expert panels or inter-annotator agreement data.
- No real-world dataset or deployment evidence.
- No latency, compute, monetary-cost or human-workload measurement in the current evaluator.
- No probabilistic outputs; calibration and unsupported-certainty rates are not measured.
- No event-history representation for audit reconstruction or unauthorized-transition measurement.
- No adversarial robustness claim beyond one illustrative content case.
- No causal-effect claim.

## 8. Versioning and change control

Any change to case wording, gold labels, metric definitions or evaluator logic requires a version increment and changelog entry. Published scores must identify the exact dataset and evaluator versions. Do not compare scores across versions without explaining changed content or scoring rules.

## 9. Gate to confirmatory evaluation

Do not label a study confirmatory until:
1. the protocol and primary outcomes are frozen;
2. baseline and treatment systems are specified and versioned;
3. resource budgets and execution conditions are comparable;
4. gold annotations have undergone independent review;
5. sample-size rationale and analysis plan are documented;
6. a separate held-out set or leakage-control strategy is established;
7. privacy, security, licensing and safety reviews are complete.

## 10. Interpretation rule

A high score on this public development fixture means only that a submitted output aligns with the annotations in these 15 fictional cases under the published evaluator. It does not establish factual accuracy, general reasoning ability, real-world governance effectiveness, safety, certification or independent validation.

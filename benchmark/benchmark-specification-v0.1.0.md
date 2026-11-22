# KSEL RN-008 — Benchmark Specification v0.1.0

**Status:** Development specification; not a validated benchmark  
**Owner:** H3XYN LAB  
**Related publication:** KSEL Research Note 008  
**Date:** 22 November 2026

## 1. Purpose

Define a small, transparent development fixture and machine-readable prediction contract for testing whether KSEL evaluation concepts can be operationalised. This specification is a first engineering step, not a claim that the benchmark is scientifically complete.

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

The v0.1.0 fixture contains 12 hand-authored fictional cases covering:
- clean evidence;
- duplicated and dependent sources;
- stale evidence;
- provenance failure;
- context mismatch;
- contradictory evidence;
- embedded untrusted instructions;
- incomplete provenance;
- system-generated evidence;
- superseded versions;
- insufficient causal evidence;
- review and authorization gates.

The fixture is intended for smoke testing and evaluator development only. It is too small and too artificial to support general performance claims.

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

A prediction contains the case ID, traceability links, accepted evidence IDs, flagged evidence IDs, independent source pairs, contradiction pairs, review completion and authorization validity. Exact field names and types are defined in the JSON Schema.

Unknown or missing case IDs are errors. Duplicate prediction rows are errors. The evaluator does not silently impute missing predictions.

## 6. Metrics

The evaluator calculates:
- micro precision, recall and F1 for traceability links;
- precision, recall and F1 for invalid-evidence detection;
- valid-evidence retention;
- false-acceptance rate;
- stale-evidence detection recall;
- false-corroboration rate;
- contradiction-preservation precision, recall and F1;
- review and authorization compliance.

All metrics are reported separately. No weighted composite is defined in v0.1.0 because weights would encode unvalidated value judgements.

## 7. Known limitations

- Small sample count and limited scenario diversity.
- Hand-authored rather than independently adjudicated labels.
- Synthetic, fictional, English-language examples.
- No domain expert panels or inter-annotator agreement data.
- No real-world dataset or deployment evidence.
- No latency, compute, monetary-cost or human-workload measurement.
- No probabilistic outputs; calibration is not measured.
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

A high score on this public development fixture means only that a submitted output aligns with the annotations in these 12 fictional cases under the published evaluator. It does not establish factual accuracy, general reasoning ability, real-world governance effectiveness, safety, certification or independent validation.

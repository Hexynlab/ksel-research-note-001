# RN-008 Experimental Starter Kit

This directory contains the first public, executable research artefacts for KSEL RN-008.

## Status and scope

**Version:** 0.2.0  
**Status:** Synthetic development fixture and deterministic evaluator; not a validated benchmark.

The 15 cases in `data/dev/ksel-synthetic-dev-v0.2.jsonl` are fictional, hand-authored development examples. They exercise a small set of structural tasks: traceability, invalid-evidence detection, source dependence, temporal validity, contradiction preservation, and review/authorization records.

They are not representative of real-world prevalence, domain difficulty, or operational risk. They are intentionally public and therefore unsuitable as a blind test set. Do not report scores on this fixture as evidence of general KSEL effectiveness.

## Contents

- `benchmark-specification-v0.2.0.md` — versioned benchmark scope, annotations and current evaluator metric specification.
- `data/dev/ksel-synthetic-dev-v0.2.jsonl` — 15 annotated synthetic cases, including ambiguous lineage, multi-hop dependence and conflicting provenance histories.
- `schemas/prediction.schema.json` — expected prediction record shape.
- `examples/predictions.example.jsonl` — one example prediction.
- `evaluation/evaluate.py` — standard-library-only evaluator.
- `evaluation/test_evaluate.py` — evaluator unit tests.
- `BASELINE-AND-TREATMENT-PROTOCOL.md` — comparison-condition definitions.

## Run

From the repository root, with Python 3.10 or later:

```bash
python benchmark/evaluation/evaluate.py \
  --dataset benchmark/data/dev/ksel-synthetic-dev-v0.2.jsonl \
  --predictions benchmark/examples/predictions.example.jsonl
```

The example file intentionally contains only one row and will fail completeness validation against the 15-case dataset. It is a format example, not a scored submission. Create one prediction row per dataset case before running a complete evaluation.

Run the test suite with:

```bash
python -m unittest discover -s benchmark/evaluation -p "test_*.py" -v
```

## Prediction contract

Each prediction JSON object must include:

- `case_id`
- `traceability_links`: array of objects with `claim_id` and `evidence_id`
- `accepted_evidence_ids`: evidence IDs treated as admissible
- `flagged_evidence_ids`: evidence IDs flagged as invalid or requiring exclusion
- `independent_pairs`: pairs treated as independent corroboration, each with `evidence_a` and `evidence_b`
- `dependent_pairs`: pairs treated as source-dependent, same pair shape
- `contradiction_pairs`: pairs retained as materially contradictory, same pair shape
- `decision_status`: one of `supported`, `uncertain`, `unsupported`, or `review_required`
- `review_completed`: boolean
- `authorization_valid`: boolean

A system may abstain by leaving links or acceptance lists empty. Abstention is not automatically correct: the evaluator reports missed links and retention failures.

## Metric definitions

The current evaluator operationalises only the measures listed below. RN-008 proposes additional outcomes—such as calibration, unsupported-certainty rate, audit reconstruction, unauthorized state transitions, human review effort, latency and operating cost—that are not measured by this evaluator. Those require separate instrumentation, schema support and/or human annotation; they are future research outcomes, not current benchmark results.

- Traceability: micro precision, recall and F1 over required claim-evidence links.
- Invalid-evidence detection: precision, recall and F1 for the gold invalid evidence IDs.
- Valid-evidence retention: proportion of gold valid evidence retained by the system.
- False-acceptance rate: proportion of gold invalid evidence accepted by the system.
- Stale-evidence detection recall: proportion of stale evidence flagged.
- Dependent-pair and independent-pair detection: precision, recall and F1 over explicitly annotated pairs.\n- False-independence and false-dependence rates: misclassification rates over the corresponding explicitly annotated gold pairs.\n- Unlabelled source pairs: predictions are rejected; ambiguous lineage is not silently treated as independence.
- Contradiction preservation: precision, recall and F1 over annotated contradiction pairs.
- Decision-status accuracy: exact match against the case-specific expected status. This is a coarse annotation check, not a measure of general reasoning quality.
- Review and authorization compliance: proportion of review-required cases with both review completion and valid authorization recorded.

Undefined denominators are reported as `null`, not silently converted to zero.

## Important interpretation limits

1. Gold labels are annotations for these fictional cases, not universal truth labels.
2. The evaluator checks submitted structured outputs. It does not inspect model internals or prove how a system reached an answer.
3. It does not measure factual truth, calibration, human review quality, security, privacy, or causal reasoning.
4. The development set is public and small. Tuning to it creates overfitting risk.
5. A complete benchmark requires expanded domain-specific cases, annotation guidance, independent adjudication, stronger baselines, a frozen protocol and separate evaluation data.
6. No result should be described as independent validation or certification.

## Next research work

Before confirmatory experiments, H3XYN LAB should:
- review the task definitions and gold annotations;
- expand the dataset using documented generation and sampling procedures;
- establish baseline and KSEL treatment implementations with equivalent resource budgets;
- define primary outcomes and practical thresholds in advance;
- commission independent annotation review using the procedure in the baseline and treatment protocol;
- publish a frozen protocol and analysis plan;
- maintain a separate held-out evaluation set with controlled access or a delayed public release.

## Licence

The benchmark specification, explanatory documentation, synthetic development dataset, and example prediction data are licensed under **CC BY 4.0**. The evaluator and its tests, and the prediction JSON Schema, are licensed under **Apache 2.0**. See the repository's [LICENSING.md](../LICENSING.md) for the exact file-level scope, attribution requirements, and third-party exclusions.

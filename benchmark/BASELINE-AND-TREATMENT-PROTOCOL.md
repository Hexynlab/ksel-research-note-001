# RN-008 — Baseline and Treatment Protocol

**Version:** 0.1.0  
**Status:** Proposed comparison specification; no systems have been benchmarked.

## 1. Objective

Define fair comparison conditions for evaluating whether explicit KSEL governance controls improve evidence-handling outcomes. This document does not claim that any baseline or treatment implementation currently exists.

## 2. Comparison conditions

### B0 — Task-native baseline

A capable system performs the task using its ordinary task workflow. It receives the same case content and task instruction as the treatment system but is not required to emit KSEL-specific governance records. Its answer is converted to the common prediction contract by a documented adapter.

This condition must not be deliberately weakened. The selected system, model version, prompt, tools and adapter must be recorded.

### B1 — Basic source-metadata baseline

The system receives the same inputs plus ordinary source identifiers and available source metadata. It may cite sources and use basic timestamps, but it does not receive the full KSEL governance workflow for lineage dependencies, explicit claim-evidence records, temporal state transitions and review authorization.

This condition helps distinguish the value of basic metadata from the value of the more structured KSEL controls.

### K1 — KSEL governance treatment

The system uses a versioned implementation of the selected KSEL mechanisms under evaluation. The implementation must specify exactly which controls are active, how they interact, and which outputs are machine-generated versus human-authorized.

K1 is not a single immutable condition for all studies. Each experiment must identify the specific KSEL components enabled and include relevant ablations.

## 3. Fairness controls

Across conditions, hold constant or explicitly account for:

- identical case inputs and task objectives;
- model family and version, where the comparison is intended to isolate governance controls;
- system instructions and tool access, except for the governance treatment itself;
- token, context, compute and time budgets;
- retry and sampling policies;
- access to external information;
- output schema and scoring adapter;
- hardware and execution environment where material.

If a control cannot be held constant, document the difference and explain how it may affect interpretation.

## 4. Adapter and scoring controls

All conditions must emit the same prediction schema, including the optional `unresolved_pairs` state for explicit abstention. A pair omitted from all classification arrays is missing/unclassified, not an explicit abstention. The evaluator rejects duplicate/reversed pairs, self-pairs, overlapping classifications, unknown evidence IDs and predictions on unlabelled pairs. The adapter must not silently add reasoning, repair missing evidence links, infer provenance, or otherwise improve one condition's output. Adapter code must be versioned and reviewed independently from the system under test.

The deterministic evaluator scores structured predictions only. It does not determine whether the model's internal reasoning was faithful to its output.

## 5. Ablation design

Where feasible, compare:
- K1 full selected treatment;
- K1 without provenance verification;
- K1 without source-dependence tracking;
- K1 without temporal validation;
- K1 without contradiction preservation;
- K1 without review gates.

Ablations should remove one component at a time when interactions permit. If removal changes other system behaviour, document that dependency.

## 6. Outcome reporting

Report each metric separately, alongside latency, resource use and human review effort when measured. Pair-level descriptive metrics use micro (pair-pooled) aggregation across cases; confirmatory uncertainty estimates must account for clustering of pairs within cases and be specified in the preregistration. Do not select a single favourable metric as proof of overall superiority. Report false acceptance and false rejection together.

Do not claim KSEL caused an improvement unless the study design supports causal attribution. Results from the current public synthetic fixture are exploratory engineering checks only.

## 7. Independent annotation and adjudication

For confirmatory datasets with human gold labels:

1. At least two annotators independently label each relevant item before discussion.
2. Record relevant experience, training and conflicts of interest for each annotator.
3. Publish annotation instructions, operational definitions, examples and allowed labels before annotation.
4. Keep annotators blind to system condition and model outputs where feasible.
5. Preserve original labels and report disagreement; do not silently replace them with consensus.
6. Report raw agreement and an appropriate chance-corrected statistic where suitable, with its assumptions.
7. Use a separately identified adjudicator or panel for disagreements and retain the rationale.
8. Preserve ambiguous, uncertain or unresolved cases rather than forcing unsupported binary labels.
9. Clearly distinguish author-created development labels from independently reviewed confirmatory labels.

The public v0.2.0 synthetic fixture is hand-authored and has not undergone this procedure. Its labels are development annotations only.

## 8. Prerequisites for a confirmatory study

Before confirmatory runs:
1. Implement and version B0, B1 and K1.
2. Freeze prompts, adapters, tools, models and resource budgets.
3. Validate the scoring pipeline with hand-constructed fixtures.
4. Complete independent annotation and adjudication under Section 7.
5. Define sample-size rationale and primary outcomes.
6. Establish a held-out evaluation strategy.
7. Publish a completed preregistration.
8. Record the exact code and dataset commit hashes.

## 9. Current status

As of version 0.1.0, these conditions are specifications only. No baseline or KSEL treatment has been implemented or run as part of RN-008.

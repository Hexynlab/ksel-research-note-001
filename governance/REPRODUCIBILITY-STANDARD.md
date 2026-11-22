# HEXYN LAB — Reproducibility and Experimental Reporting Standard

**Applies to:** Empirical KSEL publications, prototypes and benchmark reports  
**Status:** Public standard, version 1.0  
**Effective date:** 22 November 2026

## 1. Objective

Enable readers to understand how a result was produced, identify its limitations, and reproduce or independently challenge it where access and resources permit.

## 2. Minimum experiment record

Every empirical study should document:

1. Research question and preregistered or predeclared hypotheses, where applicable.
2. Study design, task definitions and evaluation unit.
3. Inclusion, exclusion and stopping criteria.
4. Dataset or evidence-source provenance and version.
5. Data preparation, transformations and known leakage risks.
6. Systems, models, prompts, policies and configurations tested.
7. Baseline systems and rationale for selecting them.
8. Control conditions and ablation conditions.
9. Metrics, definitions, calculation procedures and direction of improvement.
10. Number of trials, random seeds and aggregation method where applicable.
11. Statistical methods and uncertainty intervals where appropriate.
12. Hardware, software and dependency versions when material.
13. Deviations, failures, exclusions and missing observations.
14. Limitations, threats to validity and known confounders.
15. Ethical, privacy, safety and disclosure considerations.

## 3. Baseline and comparison discipline

A claimed improvement requires a meaningful comparison. Define baselines before inspecting final outcomes where practical. Explain why each baseline is relevant and what it does not represent.

Avoid comparisons that change multiple factors at once without a design capable of separating their effects. Use ablations to investigate which components contribute to observed differences.

## 4. Metrics

Define metrics operationally before reporting them. Explain units, aggregation, weighting, thresholds and failure severity. Report trade-offs rather than selecting only favourable metrics.

For KSEL, candidate measures may include traceability completeness, unsupported-update rate, missed-update rate, provenance verification accuracy, false corroboration rate, uncertainty calibration, review time, decision reconstruction accuracy, regression rate and operational overhead. These are candidate measures, not validated universal metrics.

## 5. Dataset and benchmark governance

Describe dataset origin, licensing, collection period, sampling, labelling, exclusions, class balance and known representational limitations. Distinguish synthetic data from real-world observations. Document benchmark contamination and leakage checks where feasible.

Do not release personal or restricted data merely to make an experiment reproducible. Provide a safe alternative such as synthetic fixtures, aggregate statistics, controlled access or a detailed data-generation procedure.

## 6. Results reporting

Report all predefined primary outcomes, including null or adverse outcomes. Separate exploratory analyses from confirmatory analyses. Include uncertainty and sample limitations. Do not imply causality from an observational association.

## 7. Reproduction package

Where lawful and safe, provide:

- Machine-readable experiment configuration.
- Version identifiers and dependency manifests.
- Evaluation scripts and test fixtures.
- Dataset references or synthetic data-generation scripts.
- Instructions to execute the experiment.
- Expected output format and result validation procedure.
- Known environment constraints.

If any element is withheld, explain why and identify the resulting reproducibility limitation.

## 8. Independent replication

A replication report should identify the original study version, the replicated claims, deviations, environment differences, results and interpretation. A failed replication should be published with the same care as a successful one.

## 9. Claims and maturity

An experiment run is not automatically a validation. A result supports only the tested conditions and scope. Generalisation requires additional evidence. Independent replication must be distinguished from author-run repetition.

## 10. Checklist

Before labelling a study evaluated, confirm that the research question, method, baselines, metrics, data provenance, results, uncertainty, limitations and artefact versions are available to the extent permitted by safety, privacy and rights constraints.

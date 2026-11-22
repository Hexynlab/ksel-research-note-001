# RN-008 Experiment 001 — Held-Out Dataset Specification

**Study ID:** RN-008-EXP-001  
**Document status:** Proposed specification; dataset not created  
**Version:** 0.1.0-draft  
**Institution:** HEXYN LAB

---

## 1. Purpose

Specify the requirements for a held-out dataset to evaluate source-dependence classification and false-corroboration errors under RN-008 Experiment 001.

The public 15-case synthetic development fixture at `benchmark/data/dev/ksel-synthetic-dev-v0.2.jsonl` is reserved for development and evaluator checks. It must not be presented as independently adjudicated confirmatory test data.

This document does not contain a dataset, claim that data collection has occurred, or establish empirical ground truth.

## 2. Dataset objectives

The held-out dataset should permit evaluation of whether systems distinguish dependent from independent evidence pairs without treating insufficient provenance as proof of independence.

It must include sufficient variation to test:
- direct copying and republication;
- common-origin evidence;
- multi-hop derivation chains and transitive dependence;
- system-generated summaries derived from external sources;
- genuinely independent observations or measurements;
- incomplete source histories;
- conflicting lineage assertions;
- cases where apparent similarity does not establish dependence;
- cases where common publisher or organization does not establish common evidence origin.

The final composition must be justified and frozen before confirmatory runs. No fixed case or pair count is prescribed in this draft.

## 3. Data sources and construction

The dataset may use appropriately licensed public materials, controlled fictional cases, or a justified combination. The final protocol must identify the source type and document:

- provenance and acquisition date;
- licensing and redistribution permissions;
- transformations and synthetic generation, if any;
- whether examples are fictional, public, or derived from real-world records;
- privacy, confidentiality and security review;
- source-history evidence supporting each gold relationship.

Do not imply that fictional or author-generated cases establish real-world prevalence. If synthetic cases are used, report them separately from real-world cases and explain their limitations.

## 4. Pair-level labels

Each scored pair must receive one of the labels defined in the versioned annotation handbook:

- DEPENDENT;
- INDEPENDENT;
- AMBIGUOUS / INSUFFICIENT;
- CONFLICTING LINEAGE.

The dataset record must retain the supporting evidence references and annotation provenance. Binary metric denominators must include only categories explicitly defined as eligible in the frozen analysis plan. Ambiguous and conflicting pairs must not be silently converted into independent pairs.

## 5. Annotation and adjudication requirements

- At least two annotators independently label each eligible pair.
- Annotators use the frozen handbook and the same evidence packet.
- Blinding to system conditions and outputs is applied where feasible.
- Original labels and rationales are retained.
- Disagreements and agreement statistics are reported.
- A separately identified adjudicator or panel reviews disagreements.
- Unresolved cases remain explicitly unresolved.
- Annotator qualifications, training and conflicts of interest are documented.

The dataset release must distinguish raw independent labels from adjudicated labels.

## 6. Development and held-out separation

The held-out dataset must not be used to tune prompts, adapters, system rules, model selection, or treatment logic.

Before confirmatory use:
- document how development cases and held-out cases were separated;
- check for duplicate or near-duplicate cases and shared lineage patterns that could leak labels;
- record any overlap in source material;
- restrict access to gold labels during system development where feasible;
- freeze dataset version and commit before confirmatory execution.

If the dataset is used to make implementation decisions, it is no longer an untouched held-out set for the affected evaluation.

## 7. Required machine-readable record fields

The final schema should support, at minimum:

- stable case identifier;
- evidence item identifiers and descriptions;
- source identifiers and source-history records;
- direct derivation links, where supported;
- pair identifiers;
- independent annotator labels and rationale references;
- adjudicated label and rationale reference;
- ambiguity/conflict status;
- scenario family;
- dataset version and provenance metadata.

The schema must not require inventing lineage roots or derivation edges when source records do not establish them. Missing or unknown values must remain explicit.

The evaluator represents ambiguous and conflicting gold relationships using optional pair-level `ambiguous_pairs` and `conflicting_pairs` fields, and represents explicit prediction abstention using optional `unresolved_pairs`. The prediction JSON Schema defines the unresolved-pair shape; the evaluator enforces cross-array semantic constraints and rejects self-pairs, duplicate/reversed pairs, overlapping classifications, unknown evidence IDs and predictions on unlabelled pairs.

Unresolved predictions are distinct from missing predictions. An explicit unresolved prediction contributes to the unresolved-prediction numerator; a labelled pair omitted from every prediction array is unclassified and reduces coverage without being counted as an explicit unresolved prediction. Both unresolved rate and classification coverage use all explicitly labelled gold pairs as their denominator.

Binary false-independence and false-dependence metrics include only adjudicated DEPENDENT and INDEPENDENT gold pairs. AMBIGUOUS / INSUFFICIENT and CONFLICTING LINEAGE pairs are excluded from those binary denominators and reported separately. The held-out dataset must preserve these distinctions and their annotation provenance.

## 8. Quality assurance

Before freezing:
- validate record structure and unique identifiers;
- verify every pair references evidence items present in its case;
- verify pair ordering and duplicate handling;
- check for contradictory gold labels;
- verify every scored label has a traceable rationale;
- inspect distribution by scenario family;
- review source permissions and privacy constraints;
- test evaluator handling with hand-constructed edge cases;
- record validation scripts, outputs and commit identifiers.

## 9. Release and reproducibility

The preregistration must identify:
- dataset name and version;
- exact immutable commit;
- source and licensing summary;
- annotation handbook version;
- annotation and adjudication process;
- case and pair counts by label and scenario;
- exclusions and unresolved items;
- known limitations and access restrictions.

If sensitive or restricted source material cannot be redistributed, publish sufficient metadata and a reproducibility procedure without disclosing prohibited content.

## 10. Open decisions before preregistration

The following remain undecided and require documented justification:

1. Domain(s) and sampling frame.
2. Source acquisition or case-generation method.
3. Dataset size and pair counts.
4. Distribution across scenario families.
5. Statistical treatment of ambiguous and conflicting pairs.
6. Final pair counts and scenario distribution by adjudicated label.
7. Data access, licensing and release constraints.
8. Leakage-control procedure and held-out access controls.

No values or thresholds should be filled in merely to make the document appear complete.

## 11. Status

Specification only. The held-out dataset has not been created, annotated, adjudicated, validated or frozen. No confirmatory results are available.

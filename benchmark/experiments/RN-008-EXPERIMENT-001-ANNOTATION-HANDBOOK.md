# RN-008 Experiment 001 — Annotation Handbook

**Study ID:** RN-008-EXP-001  
**Document status:** Draft for review; not frozen  
**Version:** 0.1.0-draft  
**Applies to:** Human annotation of evidence-pair source relationships

---

## 1. Purpose

This handbook defines how annotators should classify the relationship between two evidence items for the source-lineage experiment. It is intended to reduce inconsistent interpretation and prevent unsupported assumptions about independence.

This draft is not an annotation record and does not establish any dataset labels.

## 2. Unit of annotation

The unit is an unordered pair of distinct evidence items, (E_a, E_b), considered in the context of the case's supplied source records, lineage statements and task-relevant documentation.

Annotators must assess only information available in the annotation packet. Do not search externally unless the frozen study protocol explicitly authorizes and records that action.

## 3. Allowed labels

Assign exactly one primary label:

### DEPENDENT

Use when the available evidence establishes that one item derives materially from the other, or both derive from a common upstream source in a way that means they are not independent corroborations of the relevant claim.

Examples:
- one report republishes or summarizes another without new independent observation;
- both reports rely on the same underlying dataset or measurement;
- a downstream summary is derived from an intermediate report, which itself derives from an original source;
- a system-generated summary repeats information from its cited source without independent verification.

A shared topic, publisher, organization, author, or conclusion alone does not establish dependence.

### INDEPENDENT

Use only when the available evidence supports distinct evidentiary origins for the relevant claim, with no material shared upstream source or derivation path established in the packet.

Examples:
- separate measurements performed independently;
- separate primary records created through distinct observation processes;
- independently collected datasets, where the packet provides sufficient support for distinct origin.

Different URLs, publishers, document IDs or source names alone do not prove independence.

### AMBIGUOUS / INSUFFICIENT

Use when the available information does not justify either DEPENDENT or INDEPENDENT.

Examples:
- a report cites a common dataset but does not disclose whether it independently reproduced the result;
- source histories are missing or incomplete;
- lineage assertions are unsupported or materially unclear;
- evidence is insufficient to determine whether apparent overlap is derivation or independent observation.

Do not convert missing information into an independence label.

### CONFLICTING LINEAGE

Use when the packet contains materially incompatible lineage assertions and the conflict cannot be resolved from the supplied evidence.

Record the competing assertions and their evidence references. Do not silently select one history.

For metric mapping, the study protocol must specify whether this label is excluded from binary pair-rate denominators, treated as a separate stratum, or adjudicated into another label. This handbook does not make that statistical decision.

## 4. Relationship reasoning rules

1. **Follow the evidence chain.** Record direct derivation and, where supported, transitive derivation.
2. **Distinguish source identity from evidence origin.** Different publishers may reproduce one origin; one publisher may host independently generated evidence.
3. **Distinguish corroboration from repetition.** Repetition of a result is not a new independent observation.
4. **Do not infer independence from silence.** Missing lineage metadata is not evidence of independent origin.
5. **Do not infer dependence from similarity alone.** Similar wording or matching values may prompt scrutiny but require supporting provenance evidence.
6. **Treat system-generated summaries as derivative** when the packet establishes that they merely restate or transform supplied evidence.
7. **Preserve uncertainty.** If the packet cannot support a defensible classification, use AMBIGUOUS / INSUFFICIENT.
8. **Preserve contradictions.** If lineage records conflict, use CONFLICTING LINEAGE and document the conflict.
9. **Assess relevance to the claim.** A relationship may be immaterial if the two items independently establish a different relevant fact; explain this in notes.
10. **Do not use external assumptions** about a publisher, institution, author or platform unless included in the packet and authorized by protocol.

## 5. Required annotation record

For every pair, record:

- case ID;
- evidence item IDs;
- primary label;
- concise rationale;
- supporting packet references (document/record IDs and page, paragraph or field where available);
- whether the relationship is direct, transitive, common-origin, uncertain or conflicting;
- confidence as an annotation aid, with a written reason for low confidence;
- annotator ID code;
- annotation handbook version;
- annotation timestamp.

Confidence is not a substitute for the categorical label and must not be interpreted as a calibrated probability.

## 6. Independent annotation and adjudication

- At least two annotators label each eligible pair independently before discussion.
- Annotators must not see system predictions or the other annotator's labels before submitting their independent record, where feasible.
- Preserve all original labels and rationales.
- Report raw agreement and an appropriate chance-corrected statistic if its assumptions fit the label structure.
- A separately identified adjudicator or panel reviews disagreements using the same packet and handbook.
- Preserve the adjudicator's decision and rationale alongside, not in place of, the original labels.
- If adjudication cannot resolve the relationship, retain it as unresolved. Do not force consensus.

Annotator qualifications, training, relevant experience and conflicts of interest must be documented separately.

## 7. Calibration and handbook revision

Before confirmatory annotation, conduct a pilot using development-only examples. Discuss disagreements, clarify ambiguous instructions and revise the handbook as needed.

After the handbook is frozen:
- assign a new version to any substantive change;
- record the reason, date and author of the change;
- assess whether already annotated items require re-annotation;
- do not change rules in response to observed confirmatory system results without declaring a protocol deviation.

## 8. Out-of-scope decisions

This handbook does not determine:
- sample size;
- sampling strategy;
- statistical treatment of conflicting or ambiguous pairs;
- primary metric calculation;
- practical significance thresholds;
- whether an experiment is confirmatory.

Those decisions belong in the frozen experiment protocol and preregistration.

## 9. Status

Draft for review only. It is not frozen, and no confirmatory annotations are claimed.

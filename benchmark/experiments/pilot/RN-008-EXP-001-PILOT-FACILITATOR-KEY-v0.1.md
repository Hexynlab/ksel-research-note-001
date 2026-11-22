# RN-008 Experiment 001 — Pilot Facilitator Key

**Study ID:** RN-008-EXP-001  
**Packet ID/version:** RN-008-EXP-001-PILOT-01 / 0.1.0  
**Key version:** 0.1.0  
**Status:** Training-only expected classifications; not confirmatory gold labels.

> **Access restriction:** Facilitators must not share this key with annotators until all independent pilot records have been submitted and locked. This key is a calibration reference, not a substitute for adjudication. If annotators identify a defensible ambiguity or a flaw in the packet, record it rather than forcing agreement with this key.

## Expected classifications

| Pair | Expected label | Relationship | Core supporting records | Rationale |
|---|---|---|---|---|
| P01: E1–E2 | DEPENDENT | Direct derivation / republication | P01-R1, P01-R2 | E2 explicitly identifies E1 as its source and states no separate test was conducted. |
| P02: E1–E3 | DEPENDENT | Transitive derivation | P02-R1, P02-R2, P02-R3 | E2 transcribes E1; E3 is generated from E2. The supplied chain establishes a supported transitive path from E1 to E3. |
| P03: E1–E2 | INDEPENDENT | Distinct observations | P03-R1, P03-R2 | Separate sensors, raw files, calibration chains, teams, and sealed records support distinct origins for the same claim. |
| P04: E1–E2 | AMBIGUOUS / INSUFFICIENT | Uncertain shared-origin relationship | P04-R1, P04-R2 | Both cite D-44, but the packet does not establish whether they copied, independently reprocessed, or used separate derived extracts. |
| P05: E1–E2 | INDEPENDENT | Distinct observations | P05-R1, P05-R2 | Separate signed measurement sheets, instruments, teams, and no pre-filing exchange support distinct origins. Similar wording and matching values alone do not prove dependence. |
| P06: E1–E2 | CONFLICTING LINEAGE | Conflicting assertions | P06-R1, P06-R2 | Signed declarations assert opposite derivation directions and the packet lacks transfer logs to resolve the conflict. Preserve the conflict; do not silently select a direction. |

## Calibration discussion prompts

Use these only after independent records are locked.

1. **P01:** Which exact statement establishes derivation rather than mere similarity?
2. **P02:** What supports the transitive E1-to-E3 relationship? Would the answer change if E2's production log were missing?
3. **P03:** Which packet details support independent origin, beyond different issuers?
4. **P04:** Why is a shared dataset citation insufficient to decide dependence or independence in this packet?
5. **P05:** Why should matching text and values not override the separate measurement records?
6. **P06:** Why is this not merely AMBIGUOUS / INSUFFICIENT? What makes the packet a genuine conflict rather than simply missing information?

## Pilot evaluation worksheet

For each pair, compare annotator 1 and annotator 2 before adjudication:

| Pair | Annotator 1 | Annotator 2 | Exact agreement? | Evidence-reference agreement? | Disagreement note |
|---|---|---|---|---|---|
| P01 | | | | | |
| P02 | | | | | |
| P03 | | | | | |
| P04 | | | | | |
| P05 | | | | | |
| P06 | | | | | |

Report:
- number of pairs with exact label agreement;
- raw agreement proportion (agreement count / 6);
- per-label agreement and disagreement patterns;
- whether both annotators cited the decisive records;
- whether either annotator inferred facts not in the packet;
- adjudication outcomes and unresolved disagreements;
- handbook wording that caused confusion;
- proposed handbook changes, with exact section references.

With only six deliberately selected training cases, do not treat a chance-corrected statistic or the raw agreement proportion as a reliable estimate of confirmatory annotation reliability. The pilot is for detecting instruction and packet problems, not estimating population-level annotator performance.

## Expected limitations

- All cases are fictional and author-constructed.
- The examples are intentionally small and do not represent a sampling frame.
- Each case contains one pair; the pilot does not test complex overlapping pair networks.
- P06 intentionally preserves contradictory records; it does not determine which source history is factually correct.
- The expected classifications are authored for training and are not independent ground truth.

**End of facilitator key.**

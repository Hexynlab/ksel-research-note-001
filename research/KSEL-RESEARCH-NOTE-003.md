# KSEL Research Note 003
## Evidence Integrity, Provenance Verification, and Adversarial Resilience

**Publication series:** H3XYN LAB — Technical Research Notes  
**Document identifier:** KSEL-RN-003  
**Version:** 0.1.0  
**Status:** Preliminary research framework  
**Date:** 22 November 2026  
**Maintained by:** H3XYN LAB  
**Research area:** Evidence integrity, provenance, information security, adversarial resilience, intelligent-system governance

---

## Abstract

An evidence-governance system can maintain detailed records and still reach an unreliable conclusion if the evidence entering that system has been fabricated, altered, misattributed, selectively presented, or generated through a compromised process. Provenance metadata may be incomplete or deceptive; cryptographic integrity checks may prove that a file has not changed since a recorded event without proving that its contents were true; and multiple apparently independent sources may repeat a single manipulated origin.

This note proposes an integrity and adversarial-resilience layer for the KSEL evidence lifecycle. It distinguishes content integrity, source authenticity, provenance continuity, contextual validity, corroboration independence, and substantive truth. It introduces a threat model, evidence lineage records, verification levels, tamper-evident event histories, adversarial-content handling, and procedures for containment, reassessment, and disclosure.

The proposal treats retrieved material as untrusted data rather than executable instruction. In particular, content that attempts to redirect an intelligent system, alter its policies, suppress disclosure, or exfiltrate information must be isolated from governing instructions and handled as a security signal. The note also examines limitations of hashes, signatures, timestamps, trusted registries, and automated detection.

Five falsifiable research hypotheses and a proposed evaluation programme are provided. No experimental results, security certification, or validated detection performance are claimed.

**Keywords:** evidence integrity; provenance; authenticity; chain of custody; tamper evidence; adversarial resilience; prompt injection; source independence; information security; intelligent systems

---

## 1. Introduction

KSEL Research Note 001 proposed a governance foundation for traceable claims, inspectable uncertainty, contradiction handling, and auditable review. Research Note 002 developed decision-centred evidence acquisition, cost-aware prioritization, and adaptive review. This third note addresses a prerequisite that cuts across both: whether evidence and its history can be trusted sufficiently for the intended decision.

A well-structured evidence record is not necessarily a reliable evidence record. A source can impersonate an authority. A document can be altered before ingestion. A timestamp can be misleading. A signed statement can be authentic but false. Several sources can appear to corroborate a claim while all depending on the same compromised origin. A retrieved document can contain instructions designed to manipulate the system processing it.

These cases expose a critical distinction:

**The integrity of the record describing evidence is not the same as the truth of the claim supported by that evidence.**

An integrity layer must therefore answer several different questions:
- Has the content changed since a known point in time?
- Is the source or signer who it claims to be?
- Can the evidence's origin and transformations be reconstructed?
- Is the evidence appropriate to the claim, time, scope, and context?
- Are corroborating sources genuinely independent?
- Has the evidence or its processing path been exposed to adversarial manipulation?
- What remains unknown, and what action is justified?

No single technical mechanism answers all of these questions.

### 1.1 Research question

How can KSEL represent, verify, and govern evidence integrity and provenance in intelligent systems exposed to fabricated, manipulated, misattributed, correlated, or adversarial information?

### 1.2 Intended contribution

This note proposes:
1. A threat model for evidence and provenance attacks.
2. A layered integrity model that separates distinct verification properties.
3. An evidence-lineage and chain-of-custody record.
4. Verification levels with explicit limits.
5. Tamper-evident event-history practices.
6. Controls for hostile or instruction-bearing retrieved content.
7. A response procedure for suspected evidence compromise.
8. Testable hypotheses and an evaluation programme.

These are research and design proposals. They do not establish that any implementation is secure.

## 2. Scope and relationship to the KSEL series

RN-001 defines the evidence-governance foundation. RN-002 addresses how evidence acquisition and review effort may be prioritized. RN-003 addresses the integrity of the evidence, source, and processing history on which those activities depend.

| KSEL layer | Primary question |
|---|---|
| RN-001 — Evidence governance | What claims, evidence, uncertainty, and review states must be recorded? |
| RN-002 — Cost-aware selection | Which evidence actions are worth pursuing, and when is review sufficient? |
| RN-003 — Integrity and resilience | Can the evidence and its provenance be verified, and how should compromise be handled? |

The proposed integrity layer should integrate with existing evidence IDs, claim mappings, uncertainty registers, review records, and reassessment triggers. It should not silently replace or rewrite earlier evidence records. Corrections and supersession should be represented as new, linked events.

This note focuses on digital evidence and intelligent-system workflows. The concepts may also inform physical records and human processes, but those require additional controls such as physical custody, witness procedures, and specialist forensic methods.

## 3. Integrity properties: what is being verified?

The term *trustworthy evidence* is too broad to serve as a single technical status. KSEL should represent distinct properties independently.

### 3.1 Content integrity

Content integrity concerns whether the bytes or defined representation of an evidence object have changed relative to a recorded reference.

A cryptographic digest can help detect changes when the digest itself is protected and the comparison is performed correctly. It does not prove that the original content was accurate, complete, lawful, or honestly created.

### 3.2 Source authenticity

Authenticity concerns whether an asserted source, publisher, signer, device, or organization is genuinely associated with the evidence.

Authentication may rely on verified signatures, authenticated channels, trusted identity systems, or direct confirmation through an independently obtained contact path. Each method has assumptions and failure modes.

A valid signature can establish that a particular key signed particular content. It does not automatically establish that the key holder was authorized for the claim, that the key was uncompromised, or that the signed statement was true.

### 3.3 Provenance continuity

Provenance continuity concerns whether the origin, custody, transfers, transformations, and handling history of an evidence object can be reconstructed with adequate confidence.

A gap in provenance does not always make evidence unusable, but the gap must be visible and its consequences assessed. An undocumented transformation can change meaning even when the resulting file is internally intact.

### 3.4 Contextual validity

Contextual validity concerns whether evidence applies to the claim being evaluated, including the correct subject, time, location, version, scope, units, and operating conditions.

A genuine record can be irrelevant or misleading when detached from its original context. A valid photograph, for example, does not establish when or where it was taken unless those facts are independently supported.

### 3.5 Corroboration independence

Independence concerns whether sources provide distinct information paths rather than repeating a shared origin.

Different websites, documents, or model outputs may all derive from one press release, database, dataset, witness, or compromised account. Counting them as independent confirmations can produce false confidence.

### 3.6 Substantive reliability and truth

Substantive reliability concerns whether the content is accurate for the claim and intended use. It may require domain expertise, measurement validation, replication, contextual analysis, or independent investigation.

Truth is not established merely by integrity, authenticity, or provenance. These properties can strengthen an assessment but cannot substitute for evaluating the claim itself.

## 4. Threat model

### 4.1 Assets to protect

The threat model includes:
- Evidence objects and their original representations.
- Source identities, credentials, keys, and authority records.
- Provenance and custody events.
- Claim-to-evidence relationships.
- Transformation and extraction pipelines.
- Review decisions, approvals, and exceptions.
- System instructions, policy boundaries, and access credentials.
- Audit histories and previously issued outputs.

### 4.2 Adversaries and failure sources

Potential threats include malicious external actors, compromised legitimate accounts, deceptive publishers, insiders, automated content farms, manipulated data providers, compromised retrieval or processing services, and accidental operational failures.

The model must also account for non-malicious causes: synchronization errors, software defects, clock drift, undocumented file conversion, mistaken attribution, incomplete logging, and human misinterpretation.

An observed integrity anomaly does not by itself establish malicious intent.

### 4.3 Attack classes

| Attack class | Example | Potential consequence |
|---|---|---|
| Fabrication | Invented document, dataset, quotation, or event | False claim appears evidence-backed |
| Source impersonation | Lookalike domain, forged identity, spoofed sender | Authority is incorrectly attributed |
| Content alteration | Evidence modified before or after ingestion | Meaning or measurements change |
| Selective presentation | Relevant context or contrary records omitted | Misleading partial account |
| Provenance laundering | Repeated copies presented as independent sources | False corroboration |
| Replay or staleness | Old valid evidence reused as current | Time-sensitive decision is wrong |
| Metadata manipulation | Altered timestamps, authorship, or location fields | False context or custody history |
| Transformation attack | Parsing, OCR, transcription, or conversion changes content | Material details are lost or introduced |
| Pipeline compromise | Retrieval, storage, indexing, or processing service is altered | Evidence record becomes unreliable |
| Prompt injection | Retrieved content attempts to override system behavior | Model or agent follows hostile instructions |
| Audit tampering | Events deleted, reordered, or rewritten | Compromise becomes harder to detect |
| Insider misuse | Authorized actor changes records or bypasses review | Governance controls are undermined |

### 4.4 Trust boundaries

KSEL should identify trust boundaries between external sources, ingestion services, parsing and extraction components, storage, retrieval indexes, model context, decision logic, human reviewers, and output consumers.

Each boundary should specify:
- What data crosses it.
- Which identity or service is responsible.
- What validation occurs.
- Which permissions apply.
- What events are recorded.
- What happens when validation fails or cannot be completed.

Trust must not be inherited automatically across a boundary. A file retrieved from an authenticated storage service can still contain untrusted content.

### 4.5 Security assumptions

An implementation must document assumptions about cryptographic algorithms, key custody, identity providers, time sources, storage administrators, logging infrastructure, software dependencies, and reviewer access.

If an assumption is not tested or independently controlled, it should be recorded as an assumption rather than described as a guarantee.

## 5. Proposed KSEL integrity model

KSEL should represent integrity as a set of independently assessed dimensions, not as one universal trust score.

| Dimension | Assessment question | Example evidence |
|---|---|---|
| Content integrity | Does the object match its recorded digest or reference? | Digest comparison, signed manifest |
| Source authenticity | Is the asserted origin or signer verified? | Signature validation, independent identity check |
| Provenance continuity | Is handling history sufficiently reconstructable? | Custody events, transformation records |
| Contextual validity | Does the object apply to this claim and scope? | Date, version, subject, units, context |
| Independence | Is corroboration independent of other sources? | Lineage graph, common-origin analysis |
| Processing integrity | Are extraction and transformation steps accounted for? | Tool version, configuration, output linkage |
| Substantive assessment | Is the content reliable for the claim? | Expert review, replication, independent measurement |

A dimension may be verified, partially verified, unverified, contradicted, or not applicable. The meaning of each state must be defined by policy and accompanied by the method and time of assessment.

The system should avoid collapsing these dimensions into a numerical score unless the aggregation method is justified, calibrated, and tested. Even then, mandatory constraints and critical failures should remain visible rather than being averaged away.

## 6. Evidence lineage and chain of custody

### 6.1 Evidence object identity

Each evidence object should have a stable identifier and a versioned representation. Where possible, the record should preserve:
- Original bytes or a controlled reference to them.
- A cryptographic digest and algorithm identifier.
- Media type and size.
- Source identity as asserted and as independently verified.
- Acquisition time and the basis for that time.
- Claimed creation time, if available, clearly distinguished from acquisition time.
- Scope, subject, and contextual metadata.
- Access classification and retention requirements.

Sensitive originals may need restricted storage. A digest or metadata record should not expose personal or confidential content unnecessarily.

### 6.2 Lineage graph

Evidence lineage is better represented as a graph than as a single source field.

Nodes may represent original objects, copies, extracts, translations, OCR outputs, transcriptions, summaries, derived datasets, claims, and decisions. Edges should describe relationships such as copied-from, extracted-from, transformed-by, translated-from, corroborates, contradicts, supersedes, or relied-upon-by.

A derived object should link to its parent object or objects and identify the transformation that produced it. If the parent is unavailable, that limitation should be explicit.

### 6.3 Chain-of-custody event

A custody event should record the handling action, not merely the current custodian.

| Field | Description |
|---|---|
| Event ID | Stable event identifier |
| Evidence ID and version | Object affected |
| Event type | Acquired, transferred, accessed, copied, transformed, verified, restricted, or disposed |
| Actor or service | Authenticated person, system, or service identity |
| Event time | Timestamp and time-source basis |
| Previous and resulting references | Digests or version identifiers where applicable |
| Action and purpose | What occurred and why |
| Location or storage reference | Controlled location identifier |
| Authorization | Relevant permission, ticket, or approval |
| Result | Success, failure, partial, or exception |
| Integrity linkage | Link to prior and subsequent events |

A chain-of-custody record is only as reliable as the event capture, identity controls, time source, and protection of the event history.

### 6.4 Transformations are new evidence events

OCR, parsing, normalization, translation, transcription, compression, redaction, format conversion, and summarization can alter content or omit information.

KSEL should preserve the original where lawful and practical, record the transformation method and version, link the derived output to its inputs, and identify known limitations. A model-generated summary is a derived representation, not a replacement for the source.

Where a transformation is nondeterministic, the record should include the model or service identifier, relevant configuration, execution time, and available reproducibility information. Exact reproducibility may not be possible and must not be implied.

## 7. Verification levels and evidence status

### 7.1 Proposed verification levels

The following levels are a proposed vocabulary for communicating what has actually been checked. They are not certifications and do not form a universal ranking of truth.

| Level | Label | Minimum meaning |
|---|---|---|
| V0 | Unassessed | No integrity or provenance verification has been recorded |
| V1 | Recorded | Object, asserted source, acquisition details, and available metadata are registered |
| V2 | Integrity checked | Content matches a protected reference or recorded digest |
| V3 | Origin corroborated | Source identity or origin has been checked using a documented method |
| V4 | Lineage reviewed | Material custody and transformation history has been reviewed for relevant gaps |
| V5 | Context and claim assessed | Scope, relevance, contradictions, and substantive support have received appropriate assessment |

A higher level does not automatically mean that every lower-level check is perfect, nor does V5 mean that a claim is proven. The system should store the individual checks, results, and limitations rather than only the level label.

### 7.2 Verification record

A verification record should include the property assessed, object and version, method, tool and version, verifier identity, time, result, reference material, limitations, and any follow-up required.

Verification should be scoped. A source may be authentic for one publication but not authoritative for a different claim. A digest comparison may verify one file version without verifying the correctness of its content.

### 7.3 Unknown is not failed

KSEL should distinguish:
- **Verified:** The defined check passed within its stated scope.
- **Partially verified:** Some elements passed, while material limitations remain.
- **Unverified:** The check has not been completed or cannot be completed.
- **Failed:** The defined check did not pass.
- **Contradicted:** Available evidence conflicts with the asserted property.
- **Not applicable:** The property does not apply to this object or use.

An unavailable verification method should not be silently represented as a pass or a failure.

## 8. Cryptographic integrity and its limits

### 8.1 Hashes and manifests

A cryptographic hash can provide a compact reference to a particular byte sequence. Comparing a newly calculated digest with a protected recorded digest can reveal whether the bytes differ.

A hash alone does not establish:
- Who created the object.
- When it was created.
- Whether the original was accurate.
- Whether the recorded digest was substituted.
- Whether the object was complete before hashing.
- Whether the evidence is relevant to the claim.

Manifests should therefore include algorithm identifiers, object identifiers, versioning, and a protected means of recording or authenticating the manifest itself.

### 8.2 Digital signatures

Digital signatures can support signer authentication and integrity when key ownership, authorization, certificate status, signing context, and validation time are properly handled.

A signature-validation result should preserve the certificate or key identity, validation method, relevant trust policy, revocation or expiry status where available, and the exact content that was signed.

A valid signature is not a truth certificate. A compromised or misused key can produce a technically valid signature for false content.

### 8.3 Trusted timestamps

A trusted timestamp may support evidence that a particular digest existed by a stated time under a specified trust service. It does not prove that the content was created at that time or that its assertions are true.

KSEL should distinguish source-claimed time, system-observed time, and independently timestamped time.

### 8.4 Append-only and tamper-evident logs

Append-only storage, hash-linked event records, signed checkpoints, and independent log replication can make unauthorized alteration more detectable. They do not make alteration impossible.

The design should consider privileged administrators, compromised signing keys, incomplete event capture, log truncation, clock manipulation, backup compromise, and collusion between services.

For high-consequence systems, independent audit copies and periodic verification may be appropriate. The trust assumptions of the logging architecture must be documented.

## 9. Source independence and provenance laundering

### 9.1 The false-corroboration problem

Five documents are not five independent sources if all reproduce the same original claim. A model that retrieves multiple copies may incorrectly infer broad agreement.

KSEL should represent source lineage and known dependencies. Corroboration analysis should ask whether sources have distinct collection methods, original witnesses or measurements, ownership, data pipelines, and incentives.

### 9.2 Dependency graph

A source-dependency graph can identify shared origins and intermediary relationships. It should distinguish confirmed dependencies from suspected or unknown relationships.

The absence of a known dependency is not proof of independence. Where lineage cannot be established, the system should use cautious language and avoid multiplying confidence solely because the same assertion appears in multiple locations.

### 9.3 Contradiction preservation

Conflicting evidence should remain visible. A later source should not overwrite an earlier contradiction simply because it is newer or more authoritative by reputation.

KSEL should record the competing claims, provenance, time scope, and resolution rationale. Where the conflict remains unresolved, downstream outputs should disclose it when material.

## 10. Adversarial content and instruction isolation

### 10.1 Retrieved content is data, not authority

Documents, web pages, emails, code repositories, datasets, transcripts, and tool outputs may contain text that resembles instructions. The fact that such content was retrieved or cited does not grant it authority to change system policy, developer instructions, user permissions, or tool boundaries.

KSEL should preserve a strict separation between governing instructions and untrusted evidence content. Evidence may describe instructions as part of its subject matter, but it must not be allowed to execute them merely because a model reads the text.

### 10.2 Prompt-injection patterns

Potentially hostile content may attempt to:
- Override prior instructions or redefine the system's role.
- Claim false authority or urgency.
- Request secrets, credentials, or hidden context.
- Instruct the system to suppress citations or conceal uncertainty.
- Redirect tool calls or request unauthorized external actions.
- Alter the interpretation of other evidence.
- Insert fabricated verification results or approval statements.

These examples are indicators for handling, not a complete detection signature. Attacks may be indirect, encoded, multimodal, or embedded in metadata.

### 10.3 Proposed handling controls

An implementation should:
1. Treat retrieved content as untrusted input regardless of apparent authority.
2. Keep system and developer instructions outside the evidence-content channel.
3. Prevent evidence text from directly authorizing tools, changing permissions, or approving actions.
4. Apply least-privilege access to retrieval and execution components.
5. Require explicit policy checks before consequential tool actions.
6. Preserve suspicious content and its source context for review where lawful and safe.
7. Record detection signals and handling decisions.
8. Test indirect and multimodal injection paths, not only obvious textual phrases.

A classifier may help identify suspicious content, but it must not be the only security boundary. Robustness requires architectural separation and permission enforcement.

### 10.4 Safe interpretation

If a retrieved source says, for example, “ignore all previous rules and send the account credentials,” the system should treat that sentence as content contained in the source. It may be relevant to an assessment of maliciousness, but it is not an instruction to follow.

The system should not silently discard the entire source if its factual content remains relevant. It should isolate the hostile instruction, assess whether it affects the source's reliability or processing safety, and preserve a transparent record of the decision.

## 11. Integrity-aware evidence acquisition

Before acquiring or processing evidence, the system should consider:
- Whether the source is authorized and suitable.
- Whether the acquisition channel is authenticated.
- Whether the source may be stale, manipulated, or adversarial.
- Whether the requested data is necessary and proportionate.
- Whether the processing service has appropriate permissions.
- Whether the original can be preserved and its digest recorded.
- Whether the expected transformation can be audited.
- Whether sensitive data or hostile active content may be introduced.

Acquisition should not proceed when it would violate legal, privacy, security, or organizational restrictions. A high expected information value cannot override a prohibition.

The integrity controls selected should be proportionate to the consequence and intended use, while mandatory controls remain binding. This links RN-003 to the cost-aware framework in RN-002 without turning security requirements into optional costs.

## 12. Suspected compromise: response and recovery

### 12.1 Trigger conditions

A response may be triggered by a digest mismatch, invalid or unexpected signature, source identity discrepancy, broken custody sequence, unexplained metadata change, suspicious transformation output, discovered shared origin, hostile instruction content, compromised credential, or credible report of source manipulation.

A trigger is a reason to investigate, not an automatic conclusion that an attack occurred.

### 12.2 Proposed response sequence

**1. Preserve.** Retain relevant originals, versions, logs, and system state where lawful and technically safe. Avoid overwriting the disputed record.

**2. Contain.** Restrict further use or distribution of the affected object or processing path when the risk justifies it. Suspend compromised credentials or integrations through authorized procedures.

**3. Scope.** Identify affected evidence IDs, derived objects, claims, decisions, outputs, users, and downstream systems.

**4. Verify.** Recheck digests, signatures, source identities, timestamps, custody events, transformations, and independent references.

**5. Assess impact.** Determine whether the issue changes claim support, confidence, decision validity, access exposure, or prior approvals.

**6. Escalate.** Refer material or unresolved cases to the designated security, evidence, legal, privacy, or governance authority.

**7. Correct transparently.** Mark compromised or superseded objects, issue corrected records or outputs, and preserve links to prior versions.

**8. Reassess.** Reopen affected decisions and apply the reassessment triggers defined in RN-001 and RN-002.

**9. Learn.** Record root causes, control failures, detection gaps, and corrective actions without overstating certainty about attribution.

### 12.3 Output status

Where compromise may affect a prior output, KSEL should support statuses such as:
- **Unchanged:** Investigation found no material effect within the reviewed scope.
- **Qualified:** Output remains usable only with explicit limitations.
- **Under review:** Reliability is unresolved; reliance may need restriction.
- **Withdrawn:** Output should no longer be relied upon.
- **Superseded:** A corrected or updated output replaces the earlier version.

The authority to assign these statuses must be defined by organizational governance. A model should not independently declare a high-consequence output safe after a security incident.

## 13. Governance, accountability, and privacy

### 13.1 Responsibilities

An implementation should define who may register evidence, verify source identities, manage keys, approve trust anchors, alter retention rules, investigate anomalies, authorize exceptions, and withdraw affected outputs.

The same actor should not automatically control evidence creation, verification, approval, and audit history in high-consequence workflows.

### 13.2 Privacy and data minimization

Integrity mechanisms can create additional sensitive records, including identity metadata, access logs, source relationships, and copies of original content.

The system should minimize collection, restrict access, apply retention and deletion policies, and avoid exposing personal data through public manifests or immutable logs. Where deletion obligations conflict with audit needs, the organization requires a lawful and documented retention design; this note does not prescribe a universal solution.

### 13.3 Incident transparency

Reports should distinguish confirmed facts, plausible explanations, unresolved hypotheses, and attribution claims. A detected anomaly should not be described as a state-sponsored attack, insider action, or deliberate fraud without adequate evidence.

## 14. Evaluation programme

The framework requires empirical testing across benign errors, accidental corruption, and adversarial scenarios. Evaluation should include both security outcomes and operational costs.

### 14.1 Falsifiable hypotheses

**H1 — Provenance reconstruction:** Structured lineage and custody records improve the accuracy and completeness of independent reviewers' reconstruction of evidence history compared with workflows that record only a source URL or filename.

**H2 — False-corroboration resistance:** Explicit source-dependency representation reduces the rate at which systems treat copied or commonly derived sources as independent corroboration.

**H3 — Integrity anomaly detection:** Layered verification controls detect a greater proportion of seeded content and metadata alterations than digest-only checks, under a defined threat model.

**H4 — Instruction isolation:** Architectural separation of governing instructions from retrieved evidence reduces successful prompt-injection outcomes compared with a baseline retrieval workflow, without unacceptable loss of task utility.

**H5 — Recovery effectiveness:** A documented preserve-contain-scope-verify-reassess process reduces time to identify affected claims and outputs after a seeded evidence-compromise event.

These hypotheses have not been tested in this publication.

### 14.2 Proposed experimental conditions

A study may compare:
- **Baseline:** Existing source logging and ordinary retrieval safeguards.
- **Integrity condition:** Evidence identity, digest checks, source verification, and lineage records.
- **Resilience condition:** Integrity condition plus source-dependency analysis, instruction isolation, anomaly handling, and incident reassessment.

Comparisons should use matched tasks and controlled evidence sets. Where possible, task assignment should be randomized or counterbalanced and evaluation should be performed by reviewers who do not know the condition.

### 14.3 Test scenarios

The test corpus should include:
- Unmodified authoritative records.
- Accidental file corruption.
- Deliberate post-ingestion modification.
- Forged or lookalike source identities.
- Validly signed but substantively false content.
- Stale records presented as current.
- Multiple copies with one common origin.
- Conflicting independent measurements.
- Missing custody events.
- OCR or transcription errors.
- Prompt injection in visible text, metadata, and indirect retrieved content.
- Compromised service credentials.
- Log truncation or unauthorized event modification.
- Benign anomalies that should not be classified as attacks.

Tests should be conducted in isolated environments using synthetic or authorized data. No live third-party system should be probed without permission.

### 14.4 Outcome measures

| Measure | Definition |
|---|---|
| Integrity detection rate | Proportion of seeded integrity changes detected |
| False-positive rate | Benign cases incorrectly flagged as compromise |
| Source-authentication accuracy | Correct classification of source identity under the test protocol |
| Provenance reconstruction accuracy | Correctly recovered custody and transformation relationships |
| Dependency detection | Shared-origin relationships correctly identified |
| False-corroboration rate | Dependent sources incorrectly treated as independent |
| Injection success rate | Proportion of adversarial cases that cause prohibited behavior |
| Instruction-isolation utility | Legitimate task performance retained while hostile instructions are ignored |
| Impact-scoping completeness | Affected evidence, claims, and outputs correctly identified |
| Recovery latency | Time from trigger to documented containment and reassessment |
| Operational overhead | Storage, compute, reviewer time, and acquisition delay |

Results should include uncertainty intervals, scenario definitions, baselines, sample sizes, tool versions, and error analysis. A single aggregate score may conceal serious weaknesses and should not replace per-threat reporting.

### 14.5 Ablation studies

Ablations should examine the contribution of source authentication, digest verification, signed manifests, custody events, lineage graphs, dependency analysis, instruction isolation, least-privilege controls, and incident response procedures.

A control should not be credited with preventing an attack merely because no attack occurred in a small or poorly specified test set.

## 15. Limitations and open questions

The proposed framework has significant limitations:
1. Authenticity is difficult to establish when identity infrastructure or trust anchors are compromised.
2. Provenance records can be incomplete, fabricated, or manipulated before ingestion.
3. Hashes and signatures establish technical properties, not substantive truth.
4. Source independence is often difficult to infer from public information.
5. Automated prompt-injection detection may miss novel, indirect, or multimodal attacks.
6. Strict isolation can reduce utility if systems cannot distinguish quoted instructions from relevant subject matter.
7. Immutable or append-only records can create privacy, correction, and retention challenges.
8. High-integrity controls introduce cost, latency, operational complexity, and key-management burden.
9. A compromised trusted service may produce internally consistent but false records.
10. Human reviewers may over-trust verification labels or misunderstand their scope.

Open research questions include how to represent uncertainty in provenance itself, how to reason about partial trust, how to detect hidden source dependencies, how to evaluate multimodal injection, and how to design privacy-preserving auditability.

## 16. Conclusion

Evidence governance must examine not only what a source claims, but also how the evidence originated, how it was handled, what transformations occurred, and what can genuinely be verified.

KSEL Research Note 003 proposes a layered integrity model that separates content integrity, source authenticity, provenance continuity, contextual validity, independence, processing integrity, and substantive assessment. It adds lineage and custody records, verification levels, cryptographic controls with explicit limitations, instruction isolation for retrieved content, and a structured response to suspected compromise.

The central principle is:

**Integrity mechanisms can make evidence history more inspectable; they cannot, by themselves, make evidence true.**

A robust KSEL implementation should preserve this distinction, disclose unknowns, prevent untrusted content from acquiring authority, and reopen decisions when material evidence integrity is called into question.

The framework remains preliminary. Its security value and operational trade-offs must be established through controlled testing, transparent reporting, and independent scrutiny.

---

## Appendix A — Evidence integrity record worksheet

For each evidence object, record:
- Evidence ID and version.
- Original object reference and digest algorithm.
- Asserted source and independently verified identity, if any.
- Acquisition method, time, and time-source basis.
- Claimed creation time, if available.
- Context, scope, subject, and intended claim.
- Custody events and known gaps.
- Transformations, tools, versions, and derived objects.
- Verification properties, methods, results, and limitations.
- Known source dependencies and contradictions.
- Security or privacy restrictions.
- Reassessment triggers and responsible owner.

## Appendix B — Integrity review checklist

- [ ] Original or controlled source reference is preserved where lawful and practical.
- [ ] Object identity and version are explicit.
- [ ] Digest or equivalent integrity reference is recorded where appropriate.
- [ ] Source authenticity is assessed separately from content truth.
- [ ] Acquisition and custody history are documented.
- [ ] Transformations are linked to their inputs and tool versions.
- [ ] Context, time, scope, and relevance are checked.
- [ ] Source dependencies and possible common origins are assessed.
- [ ] Contradictory evidence remains visible.
- [ ] Retrieved instructions are isolated from governing instructions.
- [ ] Access, privacy, and retention requirements are satisfied.
- [ ] Verification limitations and unresolved gaps are disclosed.
- [ ] Incident and reassessment procedures are defined.

## Appendix C — Suggested event types

An implementation may define events such as:
- evidence_registered
- evidence_digest_created
- source_identity_checked
- signature_validation_completed
- custody_event_recorded
- evidence_copied
- evidence_transformed
- lineage_relationship_added
- source_dependency_suspected
- source_dependency_confirmed
- integrity_check_failed
- provenance_gap_identified
- adversarial_content_flagged
- evidence_quarantined
- incident_scope_assessed
- evidence_superseded
- output_reassessment_triggered
- output_withdrawn
- incident_closed

Event names are illustrative. Production schemas should define stable identifiers, authenticated actors, timestamps, object versions, authorization context, and integrity protections.

## Appendix D — Terminology

**Content integrity:** Assurance, within a defined method and scope, that an object matches a recorded representation or reference.

**Source authenticity:** Assessment that an asserted source, signer, publisher, or device is genuinely associated with an evidence object.

**Provenance:** Information describing the origin, custody, transformations, and handling history of an evidence object.

**Chain of custody:** A sequence of recorded handling and transfer events for an evidence object.

**Contextual validity:** Assessment that evidence applies to the subject, time, scope, and conditions relevant to a claim.

**Source independence:** The degree to which sources provide distinct information paths rather than deriving from a common origin.

**Prompt injection:** Adversarial content intended to manipulate an AI system's behavior by presenting instructions through data or retrieved material.

**Tamper-evident log:** A record design in which unauthorized changes are intended to be detectable under stated technical and operational assumptions.

**Verification level:** A concise label summarizing which defined checks have been completed; not a universal measure of truth.

---

## Publication and integrity statement

This document presents a preliminary research framework. It does not report completed experiments, establish a security certification, guarantee detection of adversarial content, prove the truth of any evidence object, or claim compliance with an external standard. Cryptographic mechanisms provide only the properties supported by their implementation and trust assumptions. All proposed controls require threat-specific design, authorized testing, and independent evaluation before consequential deployment.

**Suggested citation**

H3XYN LAB. (2026). *KSEL Research Note 003: Evidence Integrity, Provenance Verification, and Adversarial Resilience* (Version 0.1.0). H3XYN LAB Technical Research Notes. https://github.com/nofuxgvnwiring-source/ksel-research-note-001

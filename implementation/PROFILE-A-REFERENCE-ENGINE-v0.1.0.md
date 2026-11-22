# KSEL Profile A — Reference Engine (experimental)

**Version:** 0.1.0  
**Status:** Experimental reference implementation; not a standard, certification, or production security control.

## Capabilities

The reference engine demonstrates:

- JSON Schema Draft 2020-12 validation for Profile A records.
- Cross-record ID existence and record-type checks, including duplicate evidence-link rejection.
- Acyclic source-derivation lineage validation.
- Review target and evidence-snapshot version checks.
- Controlled claim-state transitions with caller-supplied role policy.
- Review-decision matching for approval, qualification, and rejection.
- An in-memory SHA-256 hash-linked audit ledger.
- Audit-chain verification, globally unique non-empty event IDs, and deterministic claim-state replay that rejects disallowed state transitions.
- Implementation-focused adversarial tests for dangling references, wrong reference types, duplicate IDs, version mismatches, unauthorized/invalid transitions, event tampering, and replay inconsistencies.\n- A separate black-box conformance module is documented in `PROFILE-A-CONFORMANCE-TEST-SUITE-v0.1.0.md`.

## Run

From the repository root:

\`\`\`bash
python -m pip install -r implementation/requirements-dev.txt
python -m unittest discover -s implementation/tests -p "test_*.py" -v
\`\`\`

## Security and validity boundaries

This is a reference implementation for review and experimentation. It does **not** provide:

- Authentication or proof that a declared actor identity is genuine.
- A trusted role directory, policy administration, or separation-of-duties enforcement.
- Durable append-only storage, external anchoring, signing, or protection against an attacker who can rewrite the ledger and all hashes.
- Concurrency control, distributed consistency, transactional persistence, or recovery guarantees.
- Proof that evidence is true, independent, representative, or actually supports a claim.
- Empirical evidence that KSEL improves system outcomes.

The hash chain detects modification relative to a trusted retained chain head; it is not, by itself, immutable storage. The role supplied to \`transition_claim\` is a policy input, not an authenticated credential. The engine's in-memory interfaces are intentionally small and must not be treated as a production deployment architecture.

The examples remain fictional. Passing tests establishes only the tested behaviours of this implementation. The black-box suite is separate from the implementation-focused tests but is maintained in the same repository; it is not independent third-party replication. The engine rejects schema-invalid record sets before cross-record traversal and treats an explicitly supplied empty role policy as deny-all. The suites cover malformed record shapes, dangling and mistyped references, duplicate IDs and evidence links, cyclic source lineage, review-version mismatch, role-policy boundaries, event tampering, and replay inconsistencies.

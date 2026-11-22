# KSEL Profile A — Reference Engine (experimental)

**Version:** 0.1.0  
**Status:** Experimental reference implementation; not a standard, certification, or production security control.

## Capabilities

The reference engine demonstrates:

- JSON Schema Draft 2020-12 validation for Profile A records.
- Cross-record ID existence and record-type checks.
- Review target and evidence-snapshot version checks.
- Controlled claim-state transitions with caller-supplied role policy.
- Review-decision matching for approval, qualification, and rejection.
- An in-memory SHA-256 hash-linked audit ledger.
- Audit-chain verification and deterministic claim-state replay.
- Adversarial tests for dangling references, wrong reference types, duplicate IDs, version mismatches, unauthorized/invalid transitions, event tampering, and replay inconsistencies.

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

The examples remain fictional. Passing the test suite establishes only the tested behaviours of this implementation.

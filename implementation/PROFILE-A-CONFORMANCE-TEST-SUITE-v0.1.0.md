# KSEL Profile A — Conformance Test Suite

**Version:** 0.1.0  
**Status:** Experimental test specification; not a standard or certification  
**Target:** KSEL Profile A reference API v0.1.0  
**Institution:** HEXYN LAB

## Purpose

This suite adds a black-box conformance layer alongside the reference engine's implementation-focused unit tests. It exercises documented public functions using the synthetic ExampleLib fixture and controlled invalid inputs.

The suite is intentionally maintained as a separate test module so that the expected public behaviour is stated independently of the engine's internal helper structure.

## Coverage

The v0.1.0 suite covers:

- acceptance of the complete synthetic fixture;
- rejection of malformed record shapes and non-mapping records;
- source-lineage, uncertainty-reference, and evidence-snapshot integrity;
- explicit custom role-policy enforcement, including an empty deny-all policy;
- clean rejection of invalid actor identity types;
- audit-ledger copy isolation from caller and reader mutation;
- contiguous, allowed state-transition replay.

The existing schema and engine tests remain in place. CI discovers both modules through the existing unittest discovery command.

## Run

From the repository root:

```bash
python -m pip install -r implementation/requirements-dev.txt
python -m unittest discover -s implementation/tests -p "test_*.py" -v
```

## Interpretation and limits

A passing suite establishes only that this particular reference implementation passes the listed test cases under the tested runtime. It does not establish complete Profile A conformance, correctness for all inputs, security, durability, production readiness, empirical effectiveness, or independent third-party replication.

The suite is not a substitute for an independently authored implementation, external review, property-based testing, fuzzing, persistence/concurrency tests, or evaluation under RN-008. The ExampleLib fixture is fictional and is not evidence about any real product or vulnerability.

## Planned extensions

Future versions should consider property-based and fuzz testing, canonicalization edge cases, Unicode and timestamp semantics, policy-composition tests, state-machine coverage, cross-version migration behaviour, and persistent-store adapters. These remain future work until implemented and reported.

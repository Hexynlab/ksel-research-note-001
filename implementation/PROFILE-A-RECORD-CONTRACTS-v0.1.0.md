# KSEL Profile A — Record Contracts

**Contract bundle:** 0.1.0  
**Status:** Proposed executable schema; not a standard or certification  
**Scope:** Core evidence governance records defined by KSEL-IEF-001.

## Included record types

The JSON Schema bundle defines six record types:

1. `source` — origin and source-level metadata.
2. `evidence` — a located evidence item derived from a source.
3. `claim` — a proposition with typed evidence relationships and review state.
4. `uncertainty` — a dimensioned uncertainty attached to one or more records.
5. `review` — a scoped review decision against a specific target version and evidence snapshot.
6. `audit_event` — an event describing a material action or state change.

All records use stable IDs, an explicit schema version, a positive record version, and a creation timestamp. Unknown properties are rejected to make contract drift visible.

## Files

- `schemas/profile-a.schema.json` — JSON Schema Draft 2020-12 bundle.
- `examples/profile-a-examplelib.jsonl` — six fictional linked example records.
- `tests/test_profile_a_schema.py` — schema and fixture contract tests.
- `requirements-dev.txt` — test dependency.

## Validate

From the repository root, using Python 3.10+:

```bash
python -m pip install -r implementation/requirements-dev.txt
python -m unittest discover -s implementation/tests -p "test_*.py" -v
```

## Important boundaries

JSON Schema validates an individual record's shape and local constraints. It does **not** by itself validate:

- whether referenced IDs exist;
- whether a referenced record has the expected type;
- whether source/evidence lineage is truthful or independent;
- whether record versions are sequential or immutable;
- whether review authority is genuine;
- whether a state transition is permitted;
- whether audit events are append-only or tamper-evident;
- whether timestamps are chronologically or semantically consistent;
- whether evidence actually supports a claim.

Those are cross-record, workflow, security, and operational invariants. They require application-level validation, authorization controls, storage guarantees, and adversarial tests in the reference implementation.

The examples are synthetic and use the reserved `.invalid` domain or fixture URIs. They are not evidence about a real product or vulnerability.

## Versioning

The schema version is separate from each record's `record_version`. A schema change that alters validation semantics requires a new version and migration note. Do not silently rewrite historical records to fit a newer schema.

## Research integrity

Passing these tests means only that the fixtures conform to this schema bundle and that selected invalid shapes are rejected. It does not establish KSEL effectiveness, security, production readiness, or empirical validity.

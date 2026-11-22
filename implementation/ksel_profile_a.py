"""KSEL Profile A reference engine (experimental, in-memory reference implementation).

This module demonstrates record validation, cross-record integrity checks,
controlled claim-state transitions, and a hash-linked audit ledger.
It is not a production security boundary or a persistent audit store.
"""
from __future__ import annotations

import hashlib
import json
from copy import deepcopy
from pathlib import Path
from typing import Any, Iterable, Mapping

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parent
SCHEMA_PATH = ROOT / "schemas" / "profile-a.schema.json"

ALLOWED_TRANSITIONS = {
    "draft": {"evidence_linked"},
    "evidence_linked": {"review_required"},
    "review_required": {"qualified", "approved", "rejected"},
    "qualified": {"review_required", "approved", "rejected", "superseded"},
    "approved": {"review_required", "superseded"},
    "rejected": {"review_required", "superseded"},
    "superseded": set(),
}
DECISION_STATE = {
    "approve": "approved",
    "qualify": "qualified",
    "reject": "rejected",
    "defer": "review_required",
    "escalate": "review_required",
}
DEFAULT_REQUIRED_ROLES = {
    "approved": {"approver"},
    "qualified": {"approver"},
    "rejected": {"approver"},
    "superseded": {"owner", "maintainer"},
    "evidence_linked": {"analyst", "reviewer", "owner", "maintainer"},
    "review_required": {"analyst", "reviewer", "approver", "owner", "maintainer"},
}


class KSELValidationError(ValueError):
    """Raised when a record set violates Profile A structural or relational rules."""


class KSELTransitionError(ValueError):
    """Raised when a requested claim-state transition is not permitted."""


def _canonical(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def validate_records(records: Iterable[Mapping[str, Any]],
                     schema_path: Path | str = SCHEMA_PATH) -> dict[str, dict]:
    """Validate schema shape and cross-record references; return records keyed by ID."""
    schema = json.loads(Path(schema_path).read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    indexed: dict[str, dict] = {}
    errors: list[str] = []

    for position, raw in enumerate(records):
        record = deepcopy(dict(raw))
        for error in validator.iter_errors(record):
            location = ".".join(str(part) for part in error.absolute_path) or "<root>"
            errors.append(f"record[{position}] {location}: {error.message}")
        record_id = record.get("id")
        if isinstance(record_id, str):
            if record_id in indexed:
                errors.append(f"duplicate record id: {record_id}")
            else:
                indexed[record_id] = record

    def require_ref(owner: str, field: str, target: Any,
                    expected_type: str | None = None) -> None:
        if not isinstance(target, str):
            return
        found = indexed.get(target)
        if found is None:
            errors.append(f"{owner}.{field} references missing id {target}")
        elif expected_type and found.get("record_type") != expected_type:
            errors.append(
                f"{owner}.{field} expects {expected_type}, got "
                f"{found.get('record_type')} ({target})"
            )

    for rid, record in indexed.items():
        kind = record.get("record_type")
        if kind == "source":
            for ref in record.get("derived_from", []):
                require_ref(rid, "derived_from", ref, "source")
        elif kind == "evidence":
            require_ref(rid, "source_id", record.get("source_id"), "source")
            for ref in record.get("lineage_source_ids", []):
                require_ref(rid, "lineage_source_ids", ref, "source")
        elif kind == "claim":
            for link in record.get("evidence_links", []):
                require_ref(rid, "evidence_links", link.get("evidence_id"), "evidence")
            for ref in record.get("uncertainty_ids", []):
                require_ref(rid, "uncertainty_ids", ref, "uncertainty")
        elif kind == "uncertainty":
            for ref in record.get("affected_record_ids", []):
                require_ref(rid, "affected_record_ids", ref)
        elif kind == "review":
            target = record.get("target_id")
            require_ref(rid, "target_id", target)
            if isinstance(target, str) and target in indexed:
                if indexed[target].get("record_version") != record.get("target_version"):
                    errors.append(f"{rid}.target_version does not match {target}")
            for item in record.get("evidence_snapshot", []):
                ref = item.get("id")
                require_ref(rid, "evidence_snapshot", ref)
                if isinstance(ref, str) and ref in indexed:
                    if indexed[ref].get("record_version") != item.get("version"):
                        errors.append(f"{rid}.evidence_snapshot version mismatch for {ref}")
        elif kind == "audit_event":
            require_ref(rid, "target_id", record.get("target_id"))
            for ref in record.get("related_record_ids", []):
                require_ref(rid, "related_record_ids", ref)

    if errors:
        raise KSELValidationError("Profile A validation failed:\n- " + "\n- ".join(errors))
    return indexed


def transition_claim(claim: Mapping[str, Any], new_state: str, *,
                     actor: str, actor_role: str,
                     required_roles: Mapping[str, set[str]] | None = None,
                     review: Mapping[str, Any] | None = None) -> dict:
    """Return a new claim with an authorized, policy-allowed state transition.

    Roles are caller-supplied policy assertions. This function does not authenticate
    identities or prove that a caller genuinely holds the declared role.
    """
    updated = deepcopy(dict(claim))
    if updated.get("record_type") != "claim":
        raise KSELTransitionError("target record is not a claim")
    current = updated.get("review_state")
    if new_state not in ALLOWED_TRANSITIONS.get(current, set()):
        raise KSELTransitionError(f"transition {current!r} -> {new_state!r} is not allowed")
    role_policy = required_roles or DEFAULT_REQUIRED_ROLES
    permitted = role_policy.get(new_state, set())
    if actor_role not in permitted:
        raise KSELTransitionError(
            f"role {actor_role!r} is not permitted to set state {new_state!r}"
        )
    if not actor or not actor.strip():
        raise KSELTransitionError("actor identity must be non-empty")

    if new_state in {"approved", "qualified", "rejected"}:
        if review is None:
            raise KSELTransitionError("a review record is required for this decision")
        expected = {"approved": "approve", "qualified": "qualify", "rejected": "reject"}[new_state]
        if review.get("record_type") != "review" or review.get("target_id") != updated.get("id"):
            raise KSELTransitionError("review does not target this claim")
        if review.get("target_version") != updated.get("record_version"):
            raise KSELTransitionError("review target version does not match claim version")
        if review.get("decision") != expected:
            raise KSELTransitionError(f"review decision must be {expected!r}")
        reviewer = review.get("reviewer", {})
        if reviewer.get("identity") != actor:
            raise KSELTransitionError("transition actor must match review identity")

    updated["review_state"] = new_state
    updated["record_version"] = int(updated.get("record_version", 0)) + 1
    return updated


class HashChainAuditLedger:
    """In-memory append-only-by-interface hash chain for tamper-evidence demonstration."""

    GENESIS = "0" * 64

    def __init__(self) -> None:
        self._entries: list[dict] = []

    @property
    def entries(self) -> tuple[dict, ...]:
        return tuple(deepcopy(self._entries))

    def append(self, event: Mapping[str, Any]) -> dict:
        if not isinstance(event, Mapping):
            raise TypeError("event must be a mapping")
        if self._entries and event.get("id") == self._entries[-1]["event"].get("id"):
            raise ValueError("duplicate consecutive audit event id")
        previous = self._entries[-1]["hash"] if self._entries else self.GENESIS
        payload = {"previous_hash": previous, "event": deepcopy(dict(event))}
        digest = hashlib.sha256(_canonical(payload)).hexdigest()
        entry = {**payload, "hash": digest}
        self._entries.append(entry)
        return deepcopy(entry)

    def verify(self) -> bool:
        previous = self.GENESIS
        for entry in self._entries:
            if entry.get("previous_hash") != previous:
                return False
            payload = {
                "previous_hash": entry.get("previous_hash"),
                "event": entry.get("event"),
            }
            expected = hashlib.sha256(_canonical(payload)).hexdigest()
            if entry.get("hash") != expected:
                return False
            previous = expected
        return True

    def reconstruct_claim_states(self, initial: Mapping[str, str]) -> dict[str, str]:
        """Replay state_transition events in append order over supplied initial states."""
        if not self.verify():
            raise KSELValidationError("audit chain verification failed")
        states = dict(initial)
        for entry in self._entries:
            event = entry["event"]
            if event.get("event_type") != "state_transition":
                continue
            target = event.get("target_id")
            prior = event.get("prior_state")
            resulting = event.get("resulting_state")
            if target not in states or states[target] != prior:
                raise KSELValidationError(
                    f"cannot replay transition for {target}: expected prior state {states.get(target)!r}, got {prior!r}"
                )
            states[target] = resulting
        return states

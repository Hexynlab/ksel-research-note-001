#!/usr/bin/env python3
"""Deterministic evaluator for the KSEL synthetic development fixture.

This tool scores submitted structural predictions against a transparent gold
annotation set. It does not evaluate general truth, reasoning quality, or
real-world system safety.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from typing import Any


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_no}: invalid JSON: {exc}") from exc
            if not isinstance(value, dict):
                raise ValueError(f"{path}:{line_no}: each JSONL row must be an object")
            rows.append(value)
    return rows


def pair_set(values: list[Any], key_a: str | None = None, key_b: str | None = None) -> set[tuple[str, str]]:
    result = set()
    for value in values:
        if isinstance(value, dict):
            a = value.get(key_a or "a")
            b = value.get(key_b or "b")
        elif isinstance(value, (list, tuple)) and len(value) == 2:
            a, b = value
        else:
            raise ValueError(f"Invalid pair: {value!r}")
        if not isinstance(a, str) or not isinstance(b, str):
            raise ValueError(f"Pair members must be strings: {value!r}")
        pair = tuple(sorted((a, b)))
        if pair[0] == pair[1]:
            raise ValueError(f"Pair members must be different: {value!r}")
        if pair in result:
            raise ValueError(f"Duplicate pair: {value!r}")
        result.add(pair)
    return result


def prf(predicted: set[Any], expected: set[Any]) -> dict[str, float | int]:
    tp = len(predicted & expected)
    fp = len(predicted - expected)
    fn = len(expected - predicted)
    precision = tp / (tp + fp) if tp + fp else (1.0 if not expected else 0.0)
    recall = tp / (tp + fn) if tp + fn else (1.0 if not predicted else 0.0)
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {"tp": tp, "fp": fp, "fn": fn, "precision": precision, "recall": recall, "f1": f1}


def rate(numerator: int, denominator: int) -> float | None:
    return numerator / denominator if denominator else None


def evaluate(dataset: list[dict[str, Any]], predictions: list[dict[str, Any]]) -> dict[str, Any]:
    gold_by_id = {row["case_id"]: row for row in dataset}
    if len(gold_by_id) != len(dataset):
        raise ValueError("Dataset contains duplicate case_id values")
    pred_by_id = {row.get("case_id"): row for row in predictions}
    if len(pred_by_id) != len(predictions):
        raise ValueError("Predictions contain duplicate case_id values")
    unknown = sorted(set(pred_by_id) - set(gold_by_id))
    missing = sorted(set(gold_by_id) - set(pred_by_id))
    if unknown:
        raise ValueError(f"Predictions contain unknown case IDs: {unknown}")
    if missing:
        raise ValueError(f"Predictions missing cases: {missing}")

    totals = {
        "traceability": {"tp": 0, "fp": 0, "fn": 0},
        "invalid_detection": {"tp": 0, "fp": 0, "fn": 0},
        "valid_retention": {"retained": 0, "total": 0},
        "false_acceptance": {"accepted_invalid": 0, "invalid_total": 0},
        "stale_detection": {"detected": 0, "total": 0},
        "source_dependence": {
            "dependent_pairs": {"tp": 0, "fp": 0, "fn": 0},
            "independent_pairs": {"tp": 0, "fp": 0, "fn": 0},
            "false_independent": 0,
            "dependent_total": 0,
            "false_dependent": 0,
            "independent_total": 0,
        },
        "contradiction": {"tp": 0, "fp": 0, "fn": 0},
        "review": {"compliant": 0, "required": 0},
        "decision": {"correct": 0, "total": 0},
    }
    per_case = []
    for case_id, gold_row in gold_by_id.items():
        gold = gold_row["gold"]
        pred = pred_by_id[case_id]
        expected_links = {(x[0], x[1]) for x in gold["required_links"]}
        predicted_links = {(x["claim_id"], x["evidence_id"]) for x in pred.get("traceability_links", [])}
        link = prf(predicted_links, expected_links)
        for key in ("tp", "fp", "fn"):
            totals["traceability"][key] += link[key]

        invalid = set(gold["invalid_evidence_ids"])
        valid = set(gold["valid_evidence_ids"])
        flagged = set(pred.get("flagged_evidence_ids", []))
        accepted = set(pred.get("accepted_evidence_ids", []))
        detection = prf(flagged, invalid)
        for key in ("tp", "fp", "fn"):
            totals["invalid_detection"][key] += detection[key]
        totals["valid_retention"]["retained"] += len(accepted & valid)
        totals["valid_retention"]["total"] += len(valid)
        totals["false_acceptance"]["accepted_invalid"] += len(accepted & invalid)
        totals["false_acceptance"]["invalid_total"] += len(invalid)

        stale = set(gold["stale_evidence_ids"])
        totals["stale_detection"]["detected"] += len(flagged & stale)
        totals["stale_detection"]["total"] += len(stale)

        dependent = pair_set(gold["dependent_pairs"])
        independent = pair_set(gold.get("independent_pairs", []))
        predicted_dependent = pair_set(pred.get("dependent_pairs", []), "evidence_a", "evidence_b")
        predicted_independent = pair_set(pred.get("independent_pairs", []), "evidence_a", "evidence_b")
        overlap = predicted_dependent & predicted_independent
        if overlap:
            raise ValueError(f"Pairs cannot be classified as both dependent and independent: {sorted(overlap)}")
        known_pairs = dependent | independent
        for pair in predicted_dependent | predicted_independent:
            if not set(pair).issubset({item["evidence_id"] for item in gold_row.get("evidence", [])}):
                raise ValueError(f"Source-dependence prediction references unknown evidence pair: {pair}")
        dependence = prf(predicted_dependent, dependent)
        independence = prf(predicted_independent, independent)
        for key in ("tp", "fp", "fn"):
            totals["source_dependence"]["dependent_pairs"][key] += dependence[key]
            totals["source_dependence"]["independent_pairs"][key] += independence[key]
        totals["source_dependence"]["false_independent"] += len(dependent & predicted_independent)
        totals["source_dependence"]["dependent_total"] += len(dependent)
        totals["source_dependence"]["false_dependent"] += len(independent & predicted_dependent)
        totals["source_dependence"]["independent_total"] += len(independent)

        expected_conflicts = pair_set(gold["contradiction_pairs"])
        predicted_conflicts = pair_set(pred.get("contradiction_pairs", []), "evidence_a", "evidence_b")
        conflict = prf(predicted_conflicts, expected_conflicts)
        for key in ("tp", "fp", "fn"):
            totals["contradiction"][key] += conflict[key]

        expected_status = gold.get("expected_decision_status")
        if expected_status is not None:
            totals["decision"]["total"] += 1
            totals["decision"]["correct"] += int(pred.get("decision_status") == expected_status)

        if gold["review_required"]:
            totals["review"]["required"] += 1
            compliant = bool(pred.get("review_completed")) and bool(pred.get("authorization_valid"))
            totals["review"]["compliant"] += int(compliant)

        per_case.append({
            "case_id": case_id,
            "traceability_f1": link["f1"],
            "invalid_detection_recall": detection["recall"],
            "valid_evidence_retention": rate(len(accepted & valid), len(valid)),
            "review_required": bool(gold["review_required"]),
        })

    def aggregate_prf(item: dict[str, int]) -> dict[str, float | int]:
        return prf_from_counts(item["tp"], item["fp"], item["fn"])

    metrics = {
        "traceability": aggregate_prf(totals["traceability"]),
        "invalid_evidence_detection": aggregate_prf(totals["invalid_detection"]),
        "valid_evidence_retention": rate(totals["valid_retention"]["retained"], totals["valid_retention"]["total"]),
        "false_acceptance_rate": rate(totals["false_acceptance"]["accepted_invalid"], totals["false_acceptance"]["invalid_total"]),
        "stale_evidence_detection_recall": rate(totals["stale_detection"]["detected"], totals["stale_detection"]["total"]),
        "dependent_pair_detection": aggregate_prf(totals["source_dependence"]["dependent_pairs"]),
        "independent_pair_detection": aggregate_prf(totals["source_dependence"]["independent_pairs"]),
        "false_independence_rate": rate(totals["source_dependence"]["false_independent"], totals["source_dependence"]["dependent_total"]),
        "false_dependence_rate": rate(totals["source_dependence"]["false_dependent"], totals["source_dependence"]["independent_total"]),
        "contradiction_preservation": aggregate_prf(totals["contradiction"]),
        "review_and_authorization_compliance": rate(totals["review"]["compliant"], totals["review"]["required"]),
        "decision_status_accuracy": rate(totals["decision"]["correct"], totals["decision"]["total"]),
    }
    return {
        "benchmark": "KSEL synthetic development fixture",
        "dataset_version": "0.1.0",
        "cases": len(dataset),
        "metrics": metrics,
        "counts": totals,
        "per_case": per_case,
        "interpretation_warning": "Synthetic development results are not evidence of real-world effectiveness or independent validation. Source-dependence metrics are calculated only over explicitly annotated gold pairs; unlabelled pairs are not assumed independent.",
    }


def prf_from_counts(tp: int, fp: int, fn: int) -> dict[str, float | int]:
    precision = tp / (tp + fp) if tp + fp else (1.0 if fn == 0 else 0.0)
    recall = tp / (tp + fn) if tp + fn else (1.0 if fp == 0 else 0.0)
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {"tp": tp, "fp": fp, "fn": fn, "precision": precision, "recall": recall, "f1": f1}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", required=True, type=Path)
    parser.add_argument("--predictions", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = evaluate(read_jsonl(args.dataset), read_jsonl(args.predictions))
    rendered = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()

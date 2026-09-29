"""SC-09 · ETL / ELT & Data Quality Pipeline

MAIN EXECUTION FILE

This file is the clearest end-to-end public execution path for the project.
It intentionally keeps the major steps in one place so a reviewer can see
how input becomes a business output without navigating the whole codebase.
Supporting modules under src/, sql/, workflows/ and infra/ provide the deeper
implementation details.
"""
from __future__ import annotations

import json
from pathlib import Path

TECHNICAL = Path(__file__).resolve().parent
PROJECT = TECHNICAL.parent
EXAMPLES = PROJECT / "examples"

def raw_records() -> list[dict]:
    return [
        {"record_id": "A1", "signal_a": 18, "signal_b": 0.42, "priority": "medium"},
        {"record_id": "A2", "signal_a": 31, "signal_b": 0.67, "priority": "high"},
        {"record_id": "A3", "signal_a": 12, "signal_b": 0.21, "priority": "low"},
    ]

def quality_gate(rows: list[dict]) -> dict:
    checks = {
        "unique_record_id": len({x["record_id"] for x in rows}) == len(rows),
        "signal_a_non_negative": all(x["signal_a"] >= 0 for x in rows),
        "signal_b_range": all(0 <= x["signal_b"] <= 1 for x in rows),
        "priority_domain": all(x["priority"] in {"low", "medium", "high"} for x in rows),
    }
    if not all(checks.values()):
        raise ValueError(f"quality gate failed: {checks}")
    return checks

def build_mart(rows: list[dict]) -> list[dict]:
    return [
        {**x, "weighted_signal": round(x["signal_a"] * (0.5 + x["signal_b"]), 3)}
        for x in rows
    ]

def main() -> dict:
    rows = raw_records()
    checks = quality_gate(rows)
    mart = build_mart(rows)
    result = {"quality_checks": checks, "rows_published": len(mart), "mart": mart}
    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    main()

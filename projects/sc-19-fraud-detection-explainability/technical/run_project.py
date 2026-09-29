"""SC-19 · Fraud Detection & Explainability System

MAIN EXECUTION FILE

This file is the clearest end-to-end public execution path for the project.
It keeps the major steps in one place so a reviewer can see how the project
runs without navigating the entire repository.
"""
from __future__ import annotations

import json
from pathlib import Path

TECHNICAL = Path(__file__).resolve().parent
PROJECT = TECHNICAL.parent
EXAMPLES = PROJECT / "examples"

TRANSACTIONS = [
    {"id": "T1", "score": 0.09, "amount": 48, "velocity": 1},
    {"id": "T2", "score": 0.87, "amount": 920, "velocity": 8},
    {"id": "T3", "score": 0.64, "amount": 310, "velocity": 5},
    {"id": "T4", "score": 0.96, "amount": 1800, "velocity": 11},
]

def expected_review_cost(score: float, threshold: float, amount: float) -> float:
    review_cost = 4.0 if score >= threshold else 0.0
    missed_loss = amount * score if score < threshold else 0.0
    return round(review_cost + missed_loss, 2)

def select_threshold(candidates: list[float]) -> dict:
    rows = []
    for threshold in candidates:
        cost = sum(expected_review_cost(x["score"], threshold, x["amount"]) for x in TRANSACTIONS)
        rows.append({"threshold": threshold, "expected_cost": round(cost, 2)})
    return min(rows, key=lambda x: x["expected_cost"])

def explain(tx: dict) -> list[str]:
    reasons = []
    if tx["velocity"] >= 7: reasons.append("high transaction velocity")
    if tx["amount"] >= 800: reasons.append("large transaction amount")
    if tx["score"] >= 0.80: reasons.append("high model probability")
    return reasons

def main() -> dict:
    chosen = select_threshold([0.50, 0.60, 0.70, 0.80])
    cases = [{**x, "review": x["score"] >= chosen["threshold"], "reasons": explain(x)} for x in TRANSACTIONS]
    result = {"threshold_selection": chosen, "cases": cases}
    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    main()

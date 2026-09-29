"""SC-18 · Credit Risk & Profit Optimization Engine

MAIN EXECUTION FILE

This file is the clearest end-to-end public execution path for the project.
It keeps the major steps in one place so a reviewer can see how the project
runs without navigating the entire repository.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT.parent / "examples"

APPLICATIONS = [
    {"id": "A1", "amount": 18000, "rate": 0.12, "pd": 0.045, "lgd": 0.45, "funding": 0.035},
    {"id": "A2", "amount": 26000, "rate": 0.14, "pd": 0.095, "lgd": 0.45, "funding": 0.035},
    {"id": "A3", "amount": 15000, "rate": 0.16, "pd": 0.145, "lgd": 0.50, "funding": 0.035},
]

def expected_contribution(app: dict) -> float:
    revenue = app["amount"] * app["rate"]
    expected_loss = app["amount"] * app["pd"] * app["lgd"]
    funding_cost = app["amount"] * app["funding"]
    return round(revenue - expected_loss - funding_cost, 2)

def decision(app: dict, contribution: float) -> str:
    if app["pd"] > 0.12:
        return "review"
    if contribution <= 0:
        return "decline"
    return "approve"

def main() -> dict:
    rows = []
    for app in APPLICATIONS:
        contribution = expected_contribution(app)
        rows.append({**app, "expected_contribution": contribution, "decision": decision(app, contribution)})
    result = {"decisions": rows, "approved": sum(x["decision"] == "approve" for x in rows)}
    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    main()

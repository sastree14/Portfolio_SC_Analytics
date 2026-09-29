"""SC-17 · Customer Intelligence: Churn, CLV & Segmentation

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

CUSTOMERS = [
    {"id": "C1", "churn": 0.78, "clv": 8400, "months_to_event": 2.8},
    {"id": "C2", "churn": 0.42, "clv": 12500, "months_to_event": 7.1},
    {"id": "C3", "churn": 0.65, "clv": 4300, "months_to_event": 4.2},
    {"id": "C4", "churn": 0.21, "clv": 18200, "months_to_event": 11.5},
]

def priority(customer: dict) -> float:
    urgency = 1 / max(customer["months_to_event"], 1)
    return round(customer["churn"] * customer["clv"] * urgency, 2)

def segment(customer: dict) -> str:
    if customer["churn"] >= 0.60 and customer["clv"] >= 7000:
        return "protect-now"
    if customer["churn"] >= 0.60:
        return "automated-retention"
    if customer["clv"] >= 10000:
        return "grow"
    return "monitor"

def main() -> dict:
    scored = [{**x, "priority": priority(x), "segment": segment(x)} for x in CUSTOMERS]
    scored.sort(key=lambda x: x["priority"], reverse=True)
    result = {"customers": scored}
    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    main()

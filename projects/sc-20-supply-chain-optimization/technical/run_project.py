"""SC-20 · Supply Chain & Marketplace Optimization

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

LOCATIONS = [
    {"id": "L1", "demand": 34, "margin": 12, "service_weight": 1.2},
    {"id": "L2", "demand": 28, "margin": 9, "service_weight": 1.0},
    {"id": "L3", "demand": 19, "margin": 15, "service_weight": 1.4},
    {"id": "L4", "demand": 41, "margin": 8, "service_weight": 0.9},
]
CAPACITY = 85

def optimize() -> list[dict]:
    remaining = CAPACITY
    result = []
    ordered = sorted(LOCATIONS, key=lambda x: x["margin"] * x["service_weight"], reverse=True)
    for location in ordered:
        allocation = min(location["demand"], remaining)
        result.append({**location, "allocation": allocation})
        remaining -= allocation
    return result

def main() -> dict:
    allocation = optimize()
    value = sum(x["allocation"] * x["margin"] for x in allocation)
    service = sum(x["allocation"] for x in allocation) / sum(x["demand"] for x in allocation)
    result = {"capacity": CAPACITY, "allocation": allocation, "objective_value": value, "service_ratio": round(service, 3)}
    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    main()

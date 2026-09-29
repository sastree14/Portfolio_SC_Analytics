"""SC-21 · Pricing & Revenue Optimization Engine

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

BASE_DEMAND = 1000
BASE_PRICE = 100
UNIT_COST = 52
ELASTICITY = -1.4

def expected_demand(price: float) -> float:
    return BASE_DEMAND * (price / BASE_PRICE) ** ELASTICITY

def evaluate_price(price: float) -> dict:
    demand = expected_demand(price)
    revenue = price * demand
    contribution = (price - UNIT_COST) * demand
    return {
        "price": price,
        "expected_demand": round(demand, 1),
        "revenue": round(revenue, 2),
        "contribution": round(contribution, 2),
    }

def main() -> dict:
    candidates = [80, 90, 100, 110, 120, 130]
    rows = [evaluate_price(price) for price in candidates]
    feasible = [x for x in rows if x["price"] >= 85 and (x["price"] - UNIT_COST) / x["price"] >= 0.35]
    best = max(feasible, key=lambda x: x["contribution"])
    result = {"assumptions": {"elasticity": ELASTICITY, "unit_cost": UNIT_COST}, "candidates": rows, "recommended": best}
    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    main()

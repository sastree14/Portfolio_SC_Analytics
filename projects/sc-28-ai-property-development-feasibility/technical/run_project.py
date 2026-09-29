"""SC-28 · AI Property Development Feasibility & Operations System

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

def feasibility(name: str, gdv: float, land: float, build: float, fees: float, finance: float) -> dict:
    total_cost = land + build + fees + finance
    profit = gdv - total_cost
    return {
        "scenario": name,
        "gdv": gdv,
        "total_cost": total_cost,
        "profit": profit,
        "development_margin": round(profit / gdv, 4),
    }

def investment_gate(scenario: dict) -> str:
    if scenario["development_margin"] >= 0.18:
        return "proceed-to-review"
    if scenario["development_margin"] >= 0.12:
        return "conditional-review"
    return "do-not-progress"

def main() -> dict:
    scenarios = [
        feasibility("downside", 7_600_000, 1_500_000, 4_300_000, 420_000, 380_000),
        feasibility("base", 8_400_000, 1_500_000, 4_200_000, 420_000, 360_000),
        feasibility("upside", 9_100_000, 1_500_000, 4_100_000, 420_000, 340_000),
    ]
    for scenario in scenarios:
        scenario["gate"] = investment_gate(scenario)
    result = {"scenarios": scenarios}
    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    main()

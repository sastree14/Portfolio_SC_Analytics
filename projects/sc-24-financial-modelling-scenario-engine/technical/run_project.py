"""SC-24 · Financial Modelling & Scenario Engine

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

def project_scenario(name: str, growth: float, margin: float, opex_growth: float) -> dict:
    revenue = 120000.0
    opex = 52000.0
    cash = 150000.0
    rows = []
    for month in range(1, 13):
        revenue *= (1 + growth) ** (1 / 12)
        opex *= (1 + opex_growth) ** (1 / 12)
        gross_profit = revenue * margin
        free_cash_flow = gross_profit - opex
        cash += free_cash_flow
        rows.append({
            "month": month,
            "revenue": round(revenue, 2),
            "gross_profit": round(gross_profit, 2),
            "opex": round(opex, 2),
            "free_cash_flow": round(free_cash_flow, 2),
            "cash": round(cash, 2),
        })
    return {"name": name, "ending_cash": rows[-1]["cash"], "months": rows}

def main() -> dict:
    scenarios = [
        project_scenario("downside", -0.04, 0.50, 0.08),
        project_scenario("base", 0.12, 0.58, 0.06),
        project_scenario("upside", 0.22, 0.61, 0.07),
    ]
    result = {"scenarios": scenarios}
    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({"ending_cash": {x["name"]: x["ending_cash"] for x in scenarios}}, indent=2))
    return result

if __name__ == "__main__":
    main()

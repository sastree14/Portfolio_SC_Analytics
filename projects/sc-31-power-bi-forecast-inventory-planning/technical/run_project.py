"""SC-31 · Power BI Forecast & Inventory Planning Dashboard

MAIN EXECUTION FILE
"""
from __future__ import annotations

import json
from pathlib import Path

TECHNICAL = Path(__file__).resolve().parent
PROJECT = TECHNICAL.parent
EXAMPLES = PROJECT / "examples"

ROWS = [
    {"horizon_months": 1, "actual": 100.0, "forecast": 94.0, "stock_units": 1420, "daily_demand": 37.4},
    {"horizon_months": 3, "actual": 320.0, "forecast": 300.0, "stock_units": 4180, "daily_demand": 111.0},
    {"horizon_months": 6, "actual": 650.0, "forecast": 610.0, "stock_units": 8120, "daily_demand": 218.0},
    {"horizon_months": 9, "actual": 980.0, "forecast": 900.0, "stock_units": 11950, "daily_demand": 326.0},
]

def metrics(rows: list[dict]) -> dict:
    abs_error = sum(abs(r["actual"] - r["forecast"]) for r in rows)
    actual = sum(r["actual"] for r in rows)
    bias = sum(r["forecast"] - r["actual"] for r in rows) / actual
    wape = abs_error / actual
    coverage_days = rows[0]["stock_units"] / rows[0]["daily_demand"]
    return {
        "wape": round(wape, 4),
        "forecast_bias": round(bias, 4),
        "stock_coverage_days": round(coverage_days, 1),
        "supported_horizons_months": [r["horizon_months"] for r in rows],
        "planning_action": "maintain buy plan" if coverage_days >= 30 else "review replenishment",
        "visual_evidence": "sanitized Power BI-style reconstruction based on genuine design references",
    }

def main() -> dict:
    result = metrics(ROWS)
    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    main()

"""SC-12 · Multi-Horizon Demand Forecasting & Inventory Planning

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

from statistics import mean

HISTORY = [84, 88, 93, 90, 98, 104, 101, 110, 116, 114, 121, 125]

def moving_average(values: list[float], window: int) -> float:
    return round(mean(values[-window:]), 2)

def forecast_horizon(values: list[float], horizon: int) -> list[float]:
    base = moving_average(values, min(4, len(values)))
    slope = (values[-1] - values[-4]) / 3
    return [round(base + slope * (i + 1), 2) for i in range(horizon)]

def backtest(values: list[float]) -> dict:
    errors = []
    for idx in range(6, len(values)):
        pred = mean(values[idx-3:idx])
        actual = values[idx]
        errors.append(abs(actual - pred) / max(actual, 1))
    return {"wape_proxy": round(mean(errors), 4), "observations": len(errors)}

def main() -> dict:
    horizons = {f"H{h}": forecast_horizon(HISTORY, h) for h in (1, 3, 6, 9)}
    result = {"history": HISTORY, "backtest": backtest(HISTORY), "forecasts": horizons}
    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    main()

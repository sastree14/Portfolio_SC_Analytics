"""SC-26 · Portfolio Risk & Capital Allocation Engine

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

import math

ASSETS = ["Equity", "Credit", "Bonds"]
RETURNS = [0.105, 0.072, 0.041]
VOL = [0.19, 0.11, 0.06]

def evaluate(weights: list[float]) -> dict:
    expected = sum(w * r for w, r in zip(weights, RETURNS))
    risk = math.sqrt(sum((w * v) ** 2 for w, v in zip(weights, VOL)))
    return {
        "weights": dict(zip(ASSETS, weights)),
        "expected_return": round(expected, 4),
        "volatility_proxy": round(risk, 4),
        "return_to_risk": round(expected / risk, 3),
    }

def main() -> dict:
    candidates = [
        [0.33, 0.33, 0.34],
        [0.50, 0.20, 0.30],
        [0.25, 0.25, 0.50],
        [0.40, 0.10, 0.50],
    ]
    rows = [evaluate(x) for x in candidates]
    best = max(rows, key=lambda x: x["return_to_risk"])
    result = {"candidates": rows, "selected": best}
    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    main()

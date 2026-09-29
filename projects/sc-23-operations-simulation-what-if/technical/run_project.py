"""SC-23 · Operations Simulation & What-If Engine

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

import random
from statistics import mean

def simulate(capacity: int, arrivals: int = 250, seed: int = 11) -> dict:
    random.seed(seed)
    waits = []
    utilization_samples = []
    for _ in range(arrivals):
        demand = random.expovariate(1 / 2.7)
        effective_load = demand / max(capacity, 1)
        wait = max(0.0, (effective_load - 0.65) * 18)
        waits.append(wait)
        utilization_samples.append(min(effective_load, 1.0))
    waits_sorted = sorted(waits)
    return {
        "capacity": capacity,
        "average_wait": round(mean(waits), 2),
        "p95_wait": round(waits_sorted[int(len(waits_sorted) * 0.95) - 1], 2),
        "utilization": round(mean(utilization_samples), 3),
    }

def main() -> dict:
    scenarios = [simulate(capacity) for capacity in (2, 3, 4, 5)]
    result = {"scenarios": scenarios, "recommended_capacity": min(scenarios, key=lambda x: (x["p95_wait"] > 8, x["capacity"]))["capacity"]}
    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    main()

"""SC-11 · ML / AI Evaluation & Monitoring Platform

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

REFERENCE = {"quality": 0.81, "drift": 0.08, "latency_ms": 48}
CANDIDATES = [
    {"name": "candidate-a", "quality": 0.84, "drift": 0.12, "latency_ms": 54},
    {"name": "candidate-b", "quality": 0.87, "drift": 0.27, "latency_ms": 61},
]

def evaluate(candidate: dict) -> dict:
    checks = {
        "quality": candidate["quality"] >= REFERENCE["quality"],
        "drift": candidate["drift"] <= 0.20,
        "latency": candidate["latency_ms"] <= 75,
    }
    return {**candidate, "checks": checks, "release": all(checks.values())}

def main() -> dict:
    evaluations = [evaluate(x) for x in CANDIDATES]
    promoted = next((x["name"] for x in evaluations if x["release"]), None)
    result = {"reference": REFERENCE, "evaluations": evaluations, "promoted": promoted}
    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    main()

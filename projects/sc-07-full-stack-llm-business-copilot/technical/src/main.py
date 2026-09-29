"""SC-07 - Full-Stack LLM Business Copilot

Deterministic local example. External connectors are configured separately.
"""
from __future__ import annotations
import json
from pathlib import Path

VALUES = [22,49,73,91]
LABELS = ["Question","Context","Tool use","Action"]
METRICS = ["task completion rate","tool-use success rate","time to answer","user corrections","actions completed from the copilot"]


def run_example() -> dict:
    peak = max(VALUES)
    average = round(sum(VALUES) / len(VALUES), 2)
    return {
        "project": "SC-07",
        "title": "Full-Stack LLM Business Copilot",
        "status": "completed",
        "summary": {
            "average_example_metric": average,
            "peak_example_metric": peak,
            "stages": dict(zip(LABELS, VALUES)),
        },
        "monitored_kpis": METRICS,
    }


if __name__ == "__main__":
    result = run_example()
    print(json.dumps(result, indent=2))

"""SC-06 - AI Workflow Automation Hub

Deterministic local example. External connectors are configured separately.
"""
from __future__ import annotations
import json
from pathlib import Path

VALUES = [14,33,58,76]
LABELS = ["Manual","Rules","AI step","Automated"]
METRICS = ["automated runs","manual exceptions","retry rate","average processing time","systems touched per workflow"]


def run_example() -> dict:
    peak = max(VALUES)
    average = round(sum(VALUES) / len(VALUES), 2)
    return {
        "project": "SC-06",
        "title": "AI Workflow Automation Hub",
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

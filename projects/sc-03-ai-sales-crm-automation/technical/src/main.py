"""SC-03 - AI Sales & CRM Automation System

Deterministic local example. External connectors are configured separately.
"""
from __future__ import annotations
import json
from pathlib import Path

VALUES = [18,42,67,81]
LABELS = ["Raw leads","Scored","Prioritized","Action ready"]
METRICS = ["qualified lead response time","manual touches per lead","follow-up completion rate","salesperson approval rate","pipeline coverage"]


def run_example() -> dict:
    peak = max(VALUES)
    average = round(sum(VALUES) / len(VALUES), 2)
    return {
        "project": "SC-03",
        "title": "AI Sales & CRM Automation System",
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

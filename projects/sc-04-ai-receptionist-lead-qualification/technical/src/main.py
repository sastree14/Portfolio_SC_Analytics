"""SC-04 - AI Receptionist & Lead Qualification

Deterministic local example. External connectors are configured separately.
"""
from __future__ import annotations
import json
from pathlib import Path

VALUES = [100,82,63,39]
LABELS = ["Inbound","Qualified","Routed","Booked"]
METRICS = ["time to first response","qualification completion rate","appointments created","human escalations","abandoned enquiries"]


def run_example() -> dict:
    peak = max(VALUES)
    average = round(sum(VALUES) / len(VALUES), 2)
    return {
        "project": "SC-04",
        "title": "AI Receptionist & Lead Qualification",
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

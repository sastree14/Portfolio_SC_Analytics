"""SC-08 - Enterprise Data Integration & API Platform

Deterministic local example. External connectors are configured separately.
"""
from __future__ import annotations
import json
from pathlib import Path

VALUES = [28,51,77,94]
LABELS = ["Extract","Validate","Load","Serve"]
METRICS = ["pipeline freshness","rows processed","failed loads","data-quality failures","API response time"]


def run_example() -> dict:
    peak = max(VALUES)
    average = round(sum(VALUES) / len(VALUES), 2)
    return {
        "project": "SC-08",
        "title": "Enterprise Data Integration & API Platform",
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

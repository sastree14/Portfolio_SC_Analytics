"""SC-09 - ETL / ELT & Data Quality Pipeline

Deterministic local example. External connectors are configured separately.
"""
from __future__ import annotations
import json
from pathlib import Path

VALUES = [65,78,91,98]
LABELS = ["Raw quality","Staging","Business tests","Publish"]
METRICS = ["test pass rate","freshness SLA","invalid rows","build duration","models rebuilt"]


def run_example() -> dict:
    peak = max(VALUES)
    average = round(sum(VALUES) / len(VALUES), 2)
    return {
        "project": "SC-09",
        "title": "ETL / ELT & Data Quality Pipeline",
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

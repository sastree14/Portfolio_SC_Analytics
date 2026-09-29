"""SC-05 - Document Intelligence & Due Diligence Agent

Deterministic local example. External connectors are configured separately.
"""
from __future__ import annotations
import json
from pathlib import Path

VALUES = [12,37,71,92]
LABELS = ["Ingest","Extract","Retrieve","Evidence"]
METRICS = ["documents processed per hour","retrieval hit rate","findings with source evidence","manual review time","extraction exceptions"]


def run_example() -> dict:
    peak = max(VALUES)
    average = round(sum(VALUES) / len(VALUES), 2)
    return {
        "project": "SC-05",
        "title": "Document Intelligence & Due Diligence Agent",
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

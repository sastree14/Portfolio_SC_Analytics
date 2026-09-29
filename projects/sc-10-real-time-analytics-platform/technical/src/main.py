"""SC-10 - Real-Time Analytics & Monitoring Platform

Deterministic local example. External connectors are configured separately.
"""
from __future__ import annotations
import json
from pathlib import Path

VALUES = [140,310,620,980]
LABELS = ["Ingest/s","Persist/s","Query/s","Peak/s"]
METRICS = ["event-to-query latency","events per second","consumer lag","failed events","dashboard freshness"]


def run_example() -> dict:
    peak = max(VALUES)
    average = round(sum(VALUES) / len(VALUES), 2)
    return {
        "project": "SC-10",
        "title": "Real-Time Analytics & Monitoring Platform",
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

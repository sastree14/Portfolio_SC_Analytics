"""SC-10 · Real-Time Analytics & Monitoring Platform

MAIN EXECUTION FILE

This file is the clearest end-to-end public execution path for the project.
It intentionally keeps the major steps in one place so a reviewer can see
how input becomes a business output without navigating the whole codebase.
Supporting modules under src/, sql/, workflows/ and infra/ provide the deeper
implementation details.
"""
from __future__ import annotations

import json
from pathlib import Path

TECHNICAL = Path(__file__).resolve().parent
PROJECT = TECHNICAL.parent
EXAMPLES = PROJECT / "examples"

from collections import defaultdict, deque

def event_stream() -> list[dict]:
    return [
        {"ts": 1, "type": "order", "value": 120},
        {"ts": 2, "type": "order", "value": 95},
        {"ts": 3, "type": "refund", "value": -30},
        {"ts": 4, "type": "order", "value": 180},
        {"ts": 5, "type": "order", "value": 140},
    ]

def consume(events: list[dict]) -> dict:
    totals = defaultdict(float)
    window = deque(maxlen=3)
    snapshots = []
    for event in events:
        totals[event["type"]] += event["value"]
        window.append(event["value"])
        snapshots.append({
            "ts": event["ts"],
            "rolling_3_event_value": round(sum(window), 2),
            "net_value": round(sum(totals.values()), 2),
        })
    return {"totals": dict(totals), "snapshots": snapshots, "consumer_lag": 0}

def main() -> dict:
    events = event_stream()
    result = consume(events)
    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({"events": events, **result}, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    main()

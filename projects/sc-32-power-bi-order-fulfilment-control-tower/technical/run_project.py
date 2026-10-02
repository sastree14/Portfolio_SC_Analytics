"""SC-32 · Power BI Order Fulfilment & Service Control Tower

MAIN EXECUTION FILE
"""
from __future__ import annotations

import json
from pathlib import Path

TECHNICAL = Path(__file__).resolve().parent
PROJECT = TECHNICAL.parent
EXAMPLES = PROJECT / "examples"

ORDERS = [
    {"order": "A-100", "promised_day": 10, "delivered_day": 9, "status": "closed"},
    {"order": "A-101", "promised_day": 12, "delivered_day": 14, "status": "closed"},
    {"order": "A-102", "promised_day": 15, "delivered_day": 15, "status": "closed"},
    {"order": "A-103", "promised_day": 18, "delivered_day": None, "status": "open_exception"},
]

def metrics(rows: list[dict]) -> dict:
    closed = [r for r in rows if r["delivered_day"] is not None]
    on_time = [r for r in closed if r["delivered_day"] <= r["promised_day"]]
    exceptions = [r for r in rows if r["status"] == "open_exception"]
    delays = [max(0, r["delivered_day"] - r["promised_day"]) for r in closed]
    return {
        "service_level": round(len(on_time) / len(closed), 4) if closed else 0,
        "closed_orders": len(closed),
        "open_exceptions": len(exceptions),
        "average_delay_days": round(sum(delays) / len(delays), 2) if delays else 0,
        "visual_evidence": "sanitized Power BI-style reconstruction based on genuine design references",
    }

def main() -> dict:
    result = metrics(ORDERS)
    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    main()

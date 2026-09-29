"""SC-08 · Enterprise Data Integration & API Platform

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

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT.parent / "examples"

from dataclasses import dataclass, asdict
from datetime import datetime, timezone

@dataclass
class Order:
    order_id: str
    customer_id: str
    amount: float
    status: str

def extract() -> list[Order]:
    return [
        Order("O-1001", "C-10", 1250.0, "paid"),
        Order("O-1002", "C-11", 860.0, "paid"),
        Order("O-1003", "C-12", 430.0, "cancelled"),
    ]

def validate(rows: list[Order]) -> list[Order]:
    if len({x.order_id for x in rows}) != len(rows):
        raise ValueError("duplicate order_id")
    if any(x.amount < 0 for x in rows):
        raise ValueError("negative amount")
    return rows

def transform(rows: list[Order]) -> list[dict]:
    return [
        {**asdict(x), "is_revenue": x.status == "paid", "loaded_at": datetime.now(timezone.utc).isoformat()}
        for x in rows
    ]

def publish(rows: list[dict]) -> dict:
    paid = [x for x in rows if x["is_revenue"]]
    return {
        "rows_loaded": len(rows),
        "revenue_rows": len(paid),
        "revenue": round(sum(x["amount"] for x in paid), 2),
        "targets": ["object-storage", "clickhouse", "downstream-api"],
    }

def main() -> dict:
    extracted = extract()
    validated = validate(extracted)
    curated = transform(validated)
    result = publish(curated)
    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({"result": result, "sample": curated}, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    main()

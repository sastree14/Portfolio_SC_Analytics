"""SC-15 · Tableau Commercial Analytics & Drill-Down

MAIN EXECUTION FILE

This file is the clearest end-to-end public execution path for the project.
It keeps the major steps in one place so a reviewer can see how the project
runs without navigating the entire repository.
"""
from __future__ import annotations

import json
from pathlib import Path

TECHNICAL = Path(__file__).resolve().parent
PROJECT = TECHNICAL.parent
EXAMPLES = PROJECT / "examples"

import csv
from collections import defaultdict

DATA = TECHNICAL / "data"

def load_commercial() -> list[dict]:
    with (DATA / "commercial.csv").open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))

def aggregate_by_segment(rows: list[dict]) -> dict:
    result = defaultdict(lambda: {"revenue": 0.0, "cost": 0.0, "accounts": set()})
    for row in rows:
        bucket = result[row["segment"]]
        bucket["revenue"] += float(row["revenue"])
        bucket["cost"] += float(row["cost"])
        bucket["accounts"].add(row["account_id"])
    return {
        key: {
            "revenue": round(value["revenue"], 2),
            "gross_margin": round(value["revenue"] - value["cost"], 2),
            "accounts": len(value["accounts"]),
        }
        for key, value in result.items()
    }

def main() -> dict:
    rows = load_commercial()
    result = {
        "segments": aggregate_by_segment(rows),
        "rows": len(rows),
        "native_visual_layer": "pending Tableau screenshot reference",
    }
    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    main()

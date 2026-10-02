"""SC-14 · Power BI Executive Decision System

MAIN EXECUTION FILE

This file is the clearest end-to-end public execution path for the project.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

TECHNICAL = Path(__file__).resolve().parent
PROJECT = TECHNICAL.parent
EXAMPLES = PROJECT / "examples"
DATA = TECHNICAL / "data"

def read_csv(name: str) -> list[dict]:
    with (DATA / name).open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))

def summarize_sales(rows: list[dict]) -> dict:
    revenue = sum(float(x["Revenue"]) for x in rows)
    cost = sum(float(x["Cost"]) for x in rows)
    margin = revenue - cost
    return {
        "revenue": round(revenue, 2),
        "gross_margin": round(margin, 2),
        "gross_margin_pct": round(margin / revenue, 4) if revenue else 0,
    }

def main() -> dict:
    sales = read_csv("fact_sales.csv")
    pipeline = read_csv("fact_pipeline.csv")
    targets = read_csv("fact_targets.csv")
    result = {
        "sales": summarize_sales(sales),
        "pipeline_rows": len(pipeline),
        "target_rows": len(targets),
        "visual_layer": "sanitized Power BI reconstruction based on genuine design references",
    }
    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    main()

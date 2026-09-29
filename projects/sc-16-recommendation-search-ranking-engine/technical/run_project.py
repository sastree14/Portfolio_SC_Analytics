"""SC-16 · Recommendation, Search & Ranking Engine

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

ITEMS = [
    {"id": "I1", "semantic": 0.93, "behaviour": 0.62, "margin": 0.55, "available": True},
    {"id": "I2", "semantic": 0.81, "behaviour": 0.88, "margin": 0.42, "available": True},
    {"id": "I3", "semantic": 0.89, "behaviour": 0.41, "margin": 0.61, "available": False},
    {"id": "I4", "semantic": 0.72, "behaviour": 0.76, "margin": 0.67, "available": True},
]

def candidate_generation(items: list[dict]) -> list[dict]:
    return [x for x in items if x["semantic"] >= 0.70 and x["available"]]

def rank(items: list[dict]) -> list[dict]:
    ranked = []
    for item in items:
        score = 0.45 * item["semantic"] + 0.40 * item["behaviour"] + 0.15 * item["margin"]
        ranked.append({**item, "ranking_score": round(score, 4)})
    return sorted(ranked, key=lambda x: x["ranking_score"], reverse=True)

def main() -> dict:
    candidates = candidate_generation(ITEMS)
    ranked = rank(candidates)
    result = {"candidate_count": len(candidates), "top_k": ranked[:3]}
    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    main()

"""SC-02 · Multi-Agent Operations Orchestrator

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

def planner(request: str) -> list[str]:
    return [
        f"clarify objective: {request}",
        "collect operational context",
        "delegate specialist analysis",
        "review proposed action",
        "execute only after review",
    ]

def specialist(step: str) -> dict:
    return {"step": step, "finding": f"specialist assessment for '{step}'", "confidence": 0.86}

def reviewer(findings: list[dict]) -> dict:
    confidence = sum(x["confidence"] for x in findings) / len(findings)
    return {"approved": confidence >= 0.80, "mean_confidence": round(confidence, 3)}

def execute(review: dict) -> dict:
    return {"executed": review["approved"], "action": "public-example operation"}

def main() -> dict:
    request = "Resolve a customer escalation with policy and account checks"
    plan = planner(request)
    findings = [specialist(step) for step in plan[1:4]]
    review = reviewer(findings)
    result = {"request": request, "plan": plan, "findings": findings, "review": review, "execution": execute(review)}
    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    main()

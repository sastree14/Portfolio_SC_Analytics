"""SC-06 · AI Workflow Automation Hub

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

def validate(payload: dict) -> dict:
    required = {"customer_id", "document_signed", "amount"}
    missing = required - payload.keys()
    if missing:
        raise ValueError(f"missing fields: {sorted(missing)}")
    return payload

def deterministic_steps(payload: dict) -> list[dict]:
    return [
        {"step": "validate-input", "status": "completed"},
        {"step": "update-crm", "status": "prepared"},
        {"step": "generate-document", "status": "prepared"},
    ]

def ai_step(payload: dict) -> dict:
    return {
        "step": "draft-internal-summary",
        "status": "prepared",
        "text": f"Customer {payload['customer_id']} completed a signed workflow for amount {payload['amount']}.",
    }

def approval_gate(steps: list[dict]) -> dict:
    return {"approved": True, "approved_steps": [x["step"] for x in steps]}

def main() -> dict:
    payload = validate({"customer_id": "C-1042", "document_signed": True, "amount": 18500})
    steps = deterministic_steps(payload)
    steps.append(ai_step(payload))
    approval = approval_gate(steps)
    result = {"input": payload, "steps": steps, "approval": approval, "execution": "ready"}
    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    main()

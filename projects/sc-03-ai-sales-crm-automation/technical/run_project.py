"""SC-03 · AI Sales & CRM Automation System

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

def lead_score(company_size: int, intent: int, engagement: int) -> float:
    raw = 0.35 * min(company_size / 250, 1) + 0.40 * (intent / 100) + 0.25 * (engagement / 100)
    return round(raw * 100, 1)

def next_action(score: float) -> str:
    if score >= 75:
        return "sales-call"
    if score >= 55:
        return "personalized-follow-up"
    return "nurture"

def prepare_follow_up(lead: dict, action: str) -> dict:
    return {
        "channel": "email",
        "subject": f"Next step for {lead['company']}",
        "body": f"Prepared follow-up for {lead['contact']} based on action: {action}.",
        "requires_approval": True,
    }

def main() -> dict:
    lead = {"company": "Northwind Labs", "contact": "Marta", "company_size": 140, "intent": 92, "engagement": 80}
    score = lead_score(lead["company_size"], lead["intent"], lead["engagement"])
    action = next_action(score)
    draft = prepare_follow_up(lead, action)
    result = {"lead": lead, "score": score, "next_action": action, "draft": draft, "crm_write": "pending-approval"}
    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    main()

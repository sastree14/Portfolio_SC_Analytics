"""SC-01 · Long-Running AI Agent Platform

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

def create_run(goal: str) -> dict:
    return {
        "goal": goal,
        "status": "QUEUED",
        "plan": None,
        "approved": False,
        "events": ["run_created"],
    }

def plan(run: dict) -> dict:
    run["status"] = "RUNNING"
    run["events"].append("worker_started")
    run["plan"] = [
        "validate objective and required context",
        "prepare the external action",
        "wait for approval before execution",
        "persist the final outcome",
    ]
    run["events"].extend(["plan_generated", "approval_required"])
    run["status"] = "WAITING_APPROVAL"
    return run

def approve_and_execute(run: dict) -> dict:
    if run["status"] != "WAITING_APPROVAL":
        raise RuntimeError("run is not waiting for approval")
    run["approved"] = True
    run["events"].append("approval_received")
    run["status"] = "RUNNING"
    run["result"] = {"executed": False, "reason": "public example has no external endpoint"}
    run["events"].extend(["external_action_skipped", "run_completed"])
    run["status"] = "COMPLETED"
    return run

def main() -> dict:
    run = create_run("Prepare an approved CRM follow-up for a qualified lead")
    run = plan(run)
    run = approve_and_execute(run)
    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(run, indent=2), encoding="utf-8")
    print(json.dumps(run, indent=2))
    return run

if __name__ == "__main__":
    main()

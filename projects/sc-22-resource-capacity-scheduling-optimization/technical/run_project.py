"""SC-22 · Resource, Capacity & Scheduling Optimization

MAIN EXECUTION FILE

This file is the clearest end-to-end public execution path for the project.
It keeps the major steps in one place so a reviewer can see how the project
runs without navigating the entire repository.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT.parent / "examples"

JOBS = [
    {"id": "J1", "hours": 4, "value": 9, "skill": "A"},
    {"id": "J2", "hours": 6, "value": 14, "skill": "B"},
    {"id": "J3", "hours": 3, "value": 8, "skill": "A"},
    {"id": "J4", "hours": 5, "value": 11, "skill": "B"},
]
RESOURCES = [
    {"id": "R1", "capacity": 8, "skills": {"A", "B"}},
    {"id": "R2", "capacity": 7, "skills": {"A"}},
]

def schedule() -> list[dict]:
    remaining = {r["id"]: r["capacity"] for r in RESOURCES}
    assignments = []
    for job in sorted(JOBS, key=lambda x: x["value"] / x["hours"], reverse=True):
        options = [r for r in RESOURCES if job["skill"] in r["skills"] and remaining[r["id"]] >= job["hours"]]
        if not options:
            assignments.append({"job": job["id"], "resource": None, "status": "unassigned"})
            continue
        selected = max(options, key=lambda r: remaining[r["id"]])
        remaining[selected["id"]] -= job["hours"]
        assignments.append({"job": job["id"], "resource": selected["id"], "status": "assigned"})
    return assignments

def main() -> dict:
    assignments = schedule()
    result = {
        "assignments": assignments,
        "assigned_jobs": sum(x["status"] == "assigned" for x in assignments),
        "unassigned_jobs": sum(x["status"] != "assigned" for x in assignments),
    }
    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    main()

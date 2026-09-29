import json
import os
import sys
from pathlib import Path

from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "technical" / "src"
sys.path.insert(0, str(SRC))

os.environ["DATABASE_URL"] = f"sqlite:///{ROOT / 'example_agent_platform.db'}"
os.environ["TASK_BACKEND"] = "inline"

from app.db import Base, engine
from app.main import app

OUT = ROOT / "examples" / "outputs"
LOG = ROOT / "examples" / "logs"
OUT.mkdir(parents=True, exist_ok=True)
LOG.mkdir(parents=True, exist_ok=True)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

with TestClient(app) as client:
    response = client.post(
        "/runs",
        json={
            "goal": "Prepare a CRM follow-up action for a qualified lead that requested a pricing call.",
            "provider": "mock",
            "requires_approval": True,
        },
    )
    waiting = response.json()
    (OUT / "waiting-approval.json").write_text(json.dumps(waiting, indent=2), encoding="utf-8")

    completed_response = client.post(f"/runs/{waiting['id']}/approve")
    completed = completed_response.json()
    (OUT / "completed-run.json").write_text(json.dumps(completed, indent=2), encoding="utf-8")

    lines = []
    for event in completed["events"]:
        lines.append(f"{event['created_at']} {event['event_type']} run_id={completed['id']}")
    (LOG / "approval-flow.log").write_text("\n".join(lines) + "\n", encoding="utf-8")

(ROOT / "example_agent_platform.db").unlink(missing_ok=True)
print("Generated example outputs and approval-flow log.")

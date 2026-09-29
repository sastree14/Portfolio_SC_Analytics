from fastapi.testclient import TestClient

from app.db import Base, engine
from app.main import app


def setup_module() -> None:
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def test_run_waits_for_approval_and_completes() -> None:
    with TestClient(app) as client:
        created = client.post(
            "/runs",
            json={
                "goal": "Prepare a CRM follow-up for a qualified lead.",
                "provider": "mock",
                "requires_approval": True,
            },
        )
        assert created.status_code == 202
        created_body = created.json()
        assert created_body["status"] == "WAITING_APPROVAL"
        assert created_body["plan"] is not None

        approved = client.post(f"/runs/{created_body['id']}/approve")
        assert approved.status_code == 200
        approved_body = approved.json()
        assert approved_body["status"] == "COMPLETED"
        assert approved_body["result"]["executed"] is False

        event_types = [event["event_type"] for event in approved_body["events"]]
        assert event_types == [
            "run_created",
            "worker_started",
            "plan_generated",
            "approval_required",
            "approval_received",
            "external_action_skipped",
            "run_completed",
        ]


def test_completed_run_cannot_be_approved_again() -> None:
    with TestClient(app) as client:
        created = client.post(
            "/runs",
            json={
                "goal": "Produce an internal summary without external action.",
                "provider": "mock",
                "requires_approval": False,
            },
        )
        run_id = created.json()["id"]
        response = client.post(f"/runs/{run_id}/approve")
        assert response.status_code == 409

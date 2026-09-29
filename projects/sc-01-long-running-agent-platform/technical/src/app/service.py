from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import AgentRun, RunEvent, RunStatus
from app.providers import get_provider
from app.tools import call_webhook


def add_event(session: Session, run: AgentRun, event_type: str, detail: dict | None = None) -> None:
    session.add(RunEvent(run_id=run.id, event_type=event_type, detail=detail))


def execute_planning(session: Session, run_id: str) -> AgentRun:
    run = session.scalar(select(AgentRun).where(AgentRun.id == run_id))
    if run is None:
        raise ValueError(f"Run not found: {run_id}")

    try:
        run.status = RunStatus.RUNNING
        run.error = None
        add_event(session, run, "worker_started")
        session.commit()

        provider = get_provider(run.provider)
        plan_text = provider.plan(run.goal)
        run.plan = {"provider": run.provider, "text": plan_text}
        add_event(session, run, "plan_generated", {"provider": run.provider})

        if run.requires_approval:
            run.status = RunStatus.WAITING_APPROVAL
            add_event(session, run, "approval_required")
            session.commit()
            session.refresh(run)
            return run

        return execute_action(session, run)

    except Exception as exc:
        run.status = RunStatus.FAILED
        run.error = str(exc)
        add_event(session, run, "run_failed", {"error": str(exc)})
        session.commit()
        session.refresh(run)
        raise


def execute_action(session: Session, run: AgentRun) -> AgentRun:
    if run.tool_url:
        result = {
            "executed": True,
            "webhook": call_webhook(
                run.tool_url,
                {"run_id": run.id, "goal": run.goal, "plan": run.plan},
            ),
        }
        add_event(session, run, "webhook_executed", {"url": run.tool_url})
    else:
        result = {"executed": False, "message": "No external tool URL was configured."}
        add_event(session, run, "external_action_skipped")

    run.result = result
    run.status = RunStatus.COMPLETED
    add_event(session, run, "run_completed")
    session.commit()
    session.refresh(run)
    return run


def approve_and_resume(session: Session, run_id: str) -> AgentRun:
    run = session.scalar(select(AgentRun).where(AgentRun.id == run_id))
    if run is None:
        raise ValueError(f"Run not found: {run_id}")
    if run.status != RunStatus.WAITING_APPROVAL:
        raise RuntimeError(f"Run cannot be approved from status {run.status.value}")

    add_event(session, run, "approval_received")
    run.status = RunStatus.RUNNING
    session.commit()
    return execute_action(session, run)

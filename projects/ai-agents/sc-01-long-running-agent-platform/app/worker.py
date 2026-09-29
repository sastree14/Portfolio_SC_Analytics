from celery import Celery
from sqlalchemy import select

from app.db import SessionLocal
from app.models import AgentRun, RunStatus
from app.providers import get_provider
from app.settings import get_settings
from app.tools import call_webhook

settings = get_settings()

celery_app = Celery(
    "agent_platform",
    broker=settings.celery_broker_url,
    backend=settings.celery_result_backend,
)


def _load_run(run_id: str) -> AgentRun:
    with SessionLocal() as session:
        run = session.scalar(select(AgentRun).where(AgentRun.id == run_id))
        if run is None:
            raise ValueError(f"Run not found: {run_id}")
        session.expunge(run)
        return run


def _execute_external_action(run: AgentRun) -> dict:
    if not run.tool_url:
        return {
            "executed": False,
            "message": "No external tool URL was configured.",
        }

    return {
        "executed": True,
        "webhook": call_webhook(
            run.tool_url,
            {
                "run_id": run.id,
                "goal": run.goal,
                "plan": run.plan,
            },
        ),
    }


@celery_app.task(
    bind=True,
    autoretry_for=(httpx.HTTPError,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 3},
)
def execute_run(self, run_id: str) -> None:
    del self

    with SessionLocal() as session:
        run = session.scalar(select(AgentRun).where(AgentRun.id == run_id))
        if run is None:
            return

        try:
            run.status = RunStatus.RUNNING
            run.error = None
            session.commit()

            provider = get_provider(run.provider)
            plan_text = provider.plan(run.goal)

            run.plan = {
                "provider": run.provider,
                "text": plan_text,
            }

            if run.requires_approval:
                run.status = RunStatus.WAITING_APPROVAL
                session.commit()
                return

            run.result = _execute_external_action(run)
            run.status = RunStatus.COMPLETED
            session.commit()

        except Exception as exc:
            run.status = RunStatus.FAILED
            run.error = str(exc)
            session.commit()
            raise


@celery_app.task(
    bind=True,
    autoretry_for=(httpx.HTTPError,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 3},
)
def resume_run(self, run_id: str) -> None:
    del self

    with SessionLocal() as session:
        run = session.scalar(select(AgentRun).where(AgentRun.id == run_id))
        if run is None:
            return

        try:
            run.status = RunStatus.RUNNING
            run.error = None
            session.commit()

            run.result = _execute_external_action(run)
            run.status = RunStatus.COMPLETED
            session.commit()

        except Exception as exc:
            run.status = RunStatus.FAILED
            run.error = str(exc)
            session.commit()
            raise

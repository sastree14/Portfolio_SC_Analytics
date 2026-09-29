import httpx
from celery import Celery

from app.db import SessionLocal
from app.service import approve_and_resume, execute_planning
from app.settings import get_settings

settings = get_settings()
celery_app = Celery("agent_platform", broker=settings.celery_broker_url, backend=settings.celery_result_backend)


@celery_app.task(
    bind=True,
    autoretry_for=(httpx.HTTPError,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 3},
)
def execute_run_task(self, run_id: str) -> None:
    del self
    with SessionLocal() as session:
        execute_planning(session, run_id)


@celery_app.task(
    bind=True,
    autoretry_for=(httpx.HTTPError,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 3},
)
def resume_run_task(self, run_id: str) -> None:
    del self
    with SessionLocal() as session:
        approve_and_resume(session, run_id)

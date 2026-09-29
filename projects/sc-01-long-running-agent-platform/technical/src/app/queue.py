from app.db import SessionLocal
from app.service import approve_and_resume, execute_planning
from app.settings import get_settings


def dispatch_new_run(run_id: str) -> None:
    settings = get_settings()
    if settings.task_backend == "inline":
        with SessionLocal() as session:
            execute_planning(session, run_id)
        return

    if settings.task_backend == "celery":
        from app.worker import execute_run_task
        execute_run_task.delay(run_id)
        return

    raise ValueError(f"Unsupported TASK_BACKEND: {settings.task_backend}")


def dispatch_resume(run_id: str) -> None:
    settings = get_settings()
    if settings.task_backend == "inline":
        with SessionLocal() as session:
            approve_and_resume(session, run_id)
        return

    if settings.task_backend == "celery":
        from app.worker import resume_run_task
        resume_run_task.delay(run_id)
        return

    raise ValueError(f"Unsupported TASK_BACKEND: {settings.task_backend}")

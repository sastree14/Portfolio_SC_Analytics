import secrets
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, Header, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import Base, SessionLocal, engine
from app.models import AgentRun, RunStatus
from app.schemas import RunCreate, RunRead
from app.settings import get_settings
from app.worker import execute_run, resume_run

settings = get_settings()


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="SC-01 Long-Running AI Agent Platform",
    version="1.0.0",
    lifespan=lifespan,
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def require_api_key(x_api_key: str | None = Header(default=None)) -> None:
    if not settings.app_api_key:
        return

    if not x_api_key or not secrets.compare_digest(x_api_key, settings.app_api_key):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
        )


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post(
    "/runs",
    response_model=RunRead,
    status_code=status.HTTP_202_ACCEPTED,
    dependencies=[Depends(require_api_key)],
)
def create_run(payload: RunCreate, db: Session = Depends(get_db)) -> AgentRun:
    run = AgentRun(
        goal=payload.goal,
        provider=payload.provider,
        requires_approval=payload.requires_approval,
        tool_url=str(payload.tool_url) if payload.tool_url else None,
        status=RunStatus.QUEUED,
    )
    db.add(run)
    db.commit()
    db.refresh(run)

    execute_run.delay(run.id)
    return run


@app.get(
    "/runs/{run_id}",
    response_model=RunRead,
    dependencies=[Depends(require_api_key)],
)
def get_run(run_id: str, db: Session = Depends(get_db)) -> AgentRun:
    run = db.scalar(select(AgentRun).where(AgentRun.id == run_id))
    if run is None:
        raise HTTPException(status_code=404, detail="Run not found")
    return run


@app.post(
    "/runs/{run_id}/approve",
    response_model=RunRead,
    dependencies=[Depends(require_api_key)],
)
def approve_run(run_id: str, db: Session = Depends(get_db)) -> AgentRun:
    run = db.scalar(select(AgentRun).where(AgentRun.id == run_id))
    if run is None:
        raise HTTPException(status_code=404, detail="Run not found")

    if run.status != RunStatus.WAITING_APPROVAL:
        raise HTTPException(
            status_code=409,
            detail=f"Run cannot be approved from status {run.status.value}",
        )

    run.status = RunStatus.QUEUED
    db.commit()
    db.refresh(run)

    resume_run.delay(run.id)
    return run

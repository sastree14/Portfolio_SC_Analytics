import secrets
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, Header, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.db import Base, SessionLocal, engine
from app.models import AgentRun, RunEvent, RunStatus
from app.queue import dispatch_new_run, dispatch_resume
from app.schemas import RunCreate, RunRead
from app.settings import get_settings

settings = get_settings()


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="SC-01 Long-Running AI Agent Platform", version="1.1.0", lifespan=lifespan)


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
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API key")


def _get_run(db: Session, run_id: str) -> AgentRun:
    run = db.scalar(
        select(AgentRun)
        .options(selectinload(AgentRun.events))
        .where(AgentRun.id == run_id)
    )
    if run is None:
        raise HTTPException(status_code=404, detail="Run not found")
    return run


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "sc-01-agent-platform"}


@app.post("/runs", response_model=RunRead, status_code=status.HTTP_202_ACCEPTED, dependencies=[Depends(require_api_key)])
def create_run(payload: RunCreate, db: Session = Depends(get_db)) -> AgentRun:
    run = AgentRun(
        goal=payload.goal,
        provider=payload.provider,
        requires_approval=payload.requires_approval,
        tool_url=str(payload.tool_url) if payload.tool_url else None,
        status=RunStatus.QUEUED,
    )
    db.add(run)
    db.flush()
    db.add(RunEvent(run_id=run.id, event_type="run_created", detail={"provider": run.provider}))
    db.commit()

    dispatch_new_run(run.id)
    db.expire_all()
    return _get_run(db, run.id)


@app.get("/runs/{run_id}", response_model=RunRead, dependencies=[Depends(require_api_key)])
def get_run(run_id: str, db: Session = Depends(get_db)) -> AgentRun:
    return _get_run(db, run_id)


@app.post("/runs/{run_id}/approve", response_model=RunRead, dependencies=[Depends(require_api_key)])
def approve_run(run_id: str, db: Session = Depends(get_db)) -> AgentRun:
    run = _get_run(db, run_id)
    if run.status != RunStatus.WAITING_APPROVAL:
        raise HTTPException(status_code=409, detail=f"Run cannot be approved from status {run.status.value}")

    dispatch_resume(run.id)
    db.expire_all()
    return _get_run(db, run.id)

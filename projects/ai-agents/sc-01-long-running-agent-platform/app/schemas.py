from datetime import datetime

from pydantic import BaseModel, Field, HttpUrl

from app.models import RunStatus


class RunCreate(BaseModel):
    goal: str = Field(min_length=5, max_length=5000)
    provider: str = Field(default="mock", pattern="^(mock|openai|anthropic)$")
    requires_approval: bool = True
    tool_url: HttpUrl | None = None


class RunRead(BaseModel):
    id: str
    goal: str
    provider: str
    tool_url: str | None
    requires_approval: bool
    status: RunStatus
    plan: dict | None
    result: dict | None
    error: str | None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}

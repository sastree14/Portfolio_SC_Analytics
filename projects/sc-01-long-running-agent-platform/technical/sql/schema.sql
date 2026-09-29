CREATE TABLE agent_runs (
    id VARCHAR(36) PRIMARY KEY,
    goal TEXT NOT NULL,
    provider VARCHAR(32) NOT NULL,
    tool_url TEXT,
    requires_approval BOOLEAN NOT NULL DEFAULT TRUE,
    status VARCHAR(32) NOT NULL,
    plan JSON,
    result JSON,
    error TEXT,
    created_at TIMESTAMPTZ NOT NULL,
    updated_at TIMESTAMPTZ NOT NULL
);

CREATE TABLE run_events (
    id VARCHAR(36) PRIMARY KEY,
    run_id VARCHAR(36) NOT NULL REFERENCES agent_runs(id) ON DELETE CASCADE,
    event_type VARCHAR(64) NOT NULL,
    detail JSON,
    created_at TIMESTAMPTZ NOT NULL
);

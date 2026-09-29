CREATE INDEX idx_agent_runs_status_created_at
    ON agent_runs(status, created_at DESC);

CREATE INDEX idx_run_events_run_created_at
    ON run_events(run_id, created_at ASC);

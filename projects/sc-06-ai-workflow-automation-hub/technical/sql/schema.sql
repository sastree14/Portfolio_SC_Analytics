CREATE TABLE project_runs (
    run_id VARCHAR(36) PRIMARY KEY,
    project_id VARCHAR(16) NOT NULL DEFAULT 'SC-06',
    status VARCHAR(32) NOT NULL,
    input_payload JSON,
    output_payload JSON,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMPTZ
);

CREATE TABLE project_events (
    event_id VARCHAR(36) PRIMARY KEY,
    run_id VARCHAR(36) NOT NULL REFERENCES project_runs(run_id) ON DELETE CASCADE,
    event_type VARCHAR(64) NOT NULL,
    detail JSON,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

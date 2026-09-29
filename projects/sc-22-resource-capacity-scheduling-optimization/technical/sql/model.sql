CREATE TABLE project_results (
  result_id VARCHAR(36) PRIMARY KEY,
  project_id VARCHAR(16) NOT NULL DEFAULT 'SC-22',
  scenario VARCHAR(64) NOT NULL,
  metric VARCHAR(64) NOT NULL,
  value NUMERIC NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

SELECT scenario, metric, value
FROM project_results
WHERE project_id='SC-22'
ORDER BY scenario, metric;

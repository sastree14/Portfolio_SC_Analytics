CREATE TABLE project_metrics (
  project_id VARCHAR(16) NOT NULL,
  period DATE NOT NULL,
  metric VARCHAR(64) NOT NULL,
  value NUMERIC NOT NULL,
  PRIMARY KEY (project_id, period, metric)
);

-- Example KPI extract
SELECT period, metric, value
FROM project_metrics
WHERE project_id='SC-19'
ORDER BY period, metric;

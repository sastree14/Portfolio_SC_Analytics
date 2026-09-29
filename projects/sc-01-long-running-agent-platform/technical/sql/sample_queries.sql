-- Runs waiting for a human decision
SELECT id, goal, provider, created_at
FROM agent_runs
WHERE status = 'WAITING_APPROVAL'
ORDER BY created_at ASC;

-- Execution history for one run
SELECT event_type, detail, created_at
FROM run_events
WHERE run_id = :run_id
ORDER BY created_at ASC;

-- Daily completion and failure counts
SELECT
    DATE(created_at) AS run_date,
    COUNT(*) FILTER (WHERE status = 'COMPLETED') AS completed_runs,
    COUNT(*) FILTER (WHERE status = 'FAILED') AS failed_runs
FROM agent_runs
GROUP BY DATE(created_at)
ORDER BY run_date DESC;

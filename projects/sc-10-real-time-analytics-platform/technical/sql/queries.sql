-- Operational status
SELECT status, COUNT(*) AS runs
FROM project_runs
WHERE project_id = 'SC-10'
GROUP BY status
ORDER BY runs DESC;

-- Latest execution events
SELECT e.run_id, e.event_type, e.created_at
FROM project_events e
JOIN project_runs r ON r.run_id = e.run_id
WHERE r.project_id = 'SC-10'
ORDER BY e.created_at DESC
LIMIT 100;

-- Age of runs that may require operational attention
SELECT
    id,
    status,
    created_at,
    EXTRACT(EPOCH FROM (CURRENT_TIMESTAMP - updated_at))::INT AS seconds_since_update
FROM agent_runs
WHERE status IN ('RUNNING', 'WAITING_APPROVAL', 'FAILED')
ORDER BY updated_at ASC;

-- Most recent failures
SELECT id, provider, goal, error, updated_at
FROM agent_runs
WHERE status = 'FAILED'
ORDER BY updated_at DESC
LIMIT 50;

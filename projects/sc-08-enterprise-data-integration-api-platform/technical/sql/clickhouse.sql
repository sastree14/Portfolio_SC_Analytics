CREATE TABLE IF NOT EXISTS analytics.events (
    event_time DateTime,
    entity_id String,
    metric LowCardinality(String),
    value Float64
) ENGINE = MergeTree
ORDER BY (metric, event_time, entity_id);

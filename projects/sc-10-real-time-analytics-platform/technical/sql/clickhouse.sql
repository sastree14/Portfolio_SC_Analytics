CREATE TABLE events (
  ts DateTime DEFAULT now(),
  event_id UInt64,
  value Float64
) ENGINE = MergeTree ORDER BY (ts,event_id);

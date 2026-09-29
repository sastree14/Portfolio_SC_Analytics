CREATE TABLE market_events (
  ts DateTime64(3),
  symbol LowCardinality(String),
  event_type LowCardinality(String),
  price Float64,
  size Float64,
  bid Float64,
  ask Float64
) ENGINE = MergeTree ORDER BY (symbol,ts);

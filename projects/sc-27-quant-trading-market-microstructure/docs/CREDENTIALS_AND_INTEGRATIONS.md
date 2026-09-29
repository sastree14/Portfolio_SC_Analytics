# Credentials and integrations

| System | Authentication | Used by | Data exchanged | Configuration |
|---|---|---|---|---|
| Market data feed | API key / websocket token | streaming connector | Trades, quotes and order-book updates | `MARKET_DATA_TOKEN` |
| ClickHouse | service credentials | historical store | Tick and derived feature tables | `CLICKHOUSE_URL` |
| Redis | service credentials | live state cache | Latest book and derived indicators | `REDIS_URL` |
| WebSocket UI | application auth | live visualization | Streaming book and signal updates | `WS_TOKEN` |

No secrets are committed. Runtime identities should be environment-specific and least-privilege.

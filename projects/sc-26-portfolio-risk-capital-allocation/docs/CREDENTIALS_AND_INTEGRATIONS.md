# Credentials and integrations

| System | Authentication | Used by | Data exchanged | Configuration |
|---|---|---|---|---|
| Market data source | API key / file feed | return loader | Historical prices and returns | `MARKET_DATA_TOKEN` |
| FastAPI | service auth | portfolio API | Holdings, constraints and risk results | `API_KEY` |

No secrets are committed. Runtime identities should be environment-specific and least-privilege.

# Credentials and integrations

| System | Authentication | Used by | Data exchanged | Configuration |
|---|---|---|---|---|
| PostgreSQL | service credentials | historical source | Orders, inventory and product attributes | `DATABASE_URL` |
| FastAPI | API key / service auth | forecast serving | Forecast requests and scenario outputs | `FORECAST_API_KEY` |
| Object storage | service credentials | model artefacts | Backtests and trained artefacts | `MODEL_BUCKET_URL` |

Credentials are never committed. Development, staging and production should use separate identities and least-privilege access.

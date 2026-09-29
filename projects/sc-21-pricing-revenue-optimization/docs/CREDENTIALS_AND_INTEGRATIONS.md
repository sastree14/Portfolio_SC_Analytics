# Credentials and integrations

| System | Authentication | Used by | Data exchanged | Configuration |
|---|---|---|---|---|
| PostgreSQL | service credentials | historical source | Orders, prices, promotions and margin inputs | `DATABASE_URL` |
| FastAPI | service auth | pricing API | Scenario inputs and optimized price recommendations | `API_KEY` |
| CRM / commerce webhook | bearer token | activation boundary | Approved price updates or recommendations | `COMMERCE_WEBHOOK_TOKEN` |

No secrets are committed. Runtime identities should be environment-specific and least-privilege.

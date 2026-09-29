# Credentials and integrations

| System | Authentication | Used by | Data exchanged | Configuration |
|---|---|---|---|---|
| PostgreSQL | service credentials | customer source | Customer, usage, billing and activity tables | `DATABASE_URL` |
| FastAPI | service auth | scoring API | Customer context and scores | `API_KEY` |
| CRM webhook | bearer token | activation connector | Priority customers and recommended action | `CRM_WEBHOOK_TOKEN` |

Credentials are never committed. Development, staging and production should use separate identities and least-privilege access.

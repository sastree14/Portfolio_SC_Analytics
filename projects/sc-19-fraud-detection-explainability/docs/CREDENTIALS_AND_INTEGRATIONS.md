# Credentials and integrations

| System | Authentication | Used by | Data exchanged | Configuration |
|---|---|---|---|---|
| PostgreSQL | service credentials | transaction source | Transactions, entities and labels | `DATABASE_URL` |
| FastAPI | service auth | scoring API | Transaction features and fraud score | `API_KEY` |
| Case-management webhook | bearer token | investigation connector | High-priority cases and explanations | `CASE_WEBHOOK_TOKEN` |

Credentials are never committed. Development, staging and production should use separate identities and least-privilege access.

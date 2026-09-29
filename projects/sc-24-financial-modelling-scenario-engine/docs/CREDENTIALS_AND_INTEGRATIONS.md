# Credentials and integrations

| System | Authentication | Used by | Data exchanged | Configuration |
|---|---|---|---|---|
| Excel | file access | planning input/output | Assumptions and model exports | `MODEL_XLSX_PATH` |
| PostgreSQL | service credentials | actuals source | Historical revenue and operating costs | `DATABASE_URL` |
| FastAPI | service auth | scenario API | Assumptions and projected statements | `API_KEY` |

No secrets are committed. Runtime identities should be environment-specific and least-privilege.

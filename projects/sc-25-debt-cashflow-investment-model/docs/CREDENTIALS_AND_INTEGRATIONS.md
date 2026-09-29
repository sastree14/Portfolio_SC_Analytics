# Credentials and integrations

| System | Authentication | Used by | Data exchanged | Configuration |
|---|---|---|---|---|
| Excel | file access | model input/output | Debt terms, operating assumptions and schedules | `MODEL_XLSX_PATH` |
| PostgreSQL | service credentials | actuals source | Historical cash flows and balances | `DATABASE_URL` |

No secrets are committed. Runtime identities should be environment-specific and least-privilege.

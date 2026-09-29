# Credentials and integrations

| System | Authentication | Used by | Data exchanged | Configuration |
|---|---|---|---|---|
| PostgreSQL | service credentials | planning source | Demand, inventory, cost and capacity tables | `DATABASE_URL` |
| FastAPI | service auth | optimization API | Scenario assumptions and recommended plan | `API_KEY` |
| ERP export/import | file / API credentials | operational hand-off | Inventory positions and approved recommendations | `ERP_ENDPOINT / ERP_TOKEN` |

Credentials are never committed. Development, staging and production should use separate identities and least-privilege access.

# Credentials and integrations

| System | Authentication | Used by | Data exchanged | Configuration |
|---|---|---|---|---|
| CSV / database input | file / database credentials | scenario loader | Arrival, service-time and capacity assumptions | `DATA_PATH / DATABASE_URL` |
| FastAPI | service auth | simulation API | Scenario parameters and result distributions | `API_KEY` |

No secrets are committed. Runtime identities should be environment-specific and least-privilege.

# Credentials and integrations

| System | Authentication | Used by | Data exchanged | Configuration |
|---|---|---|---|---|
| PostgreSQL | service credentials | semantic-model source | Fact and dimension tables | `DATABASE_URL` |
| Excel / CSV | file access | planning inputs | Targets and mapping tables | `INPUT_PATH` |
| Power BI Service | workspace credentials | publishing and refresh | Dataset and report artefacts | `Configured in workspace` |

Credentials are never committed. Development, staging and production should use separate identities and least-privilege access.

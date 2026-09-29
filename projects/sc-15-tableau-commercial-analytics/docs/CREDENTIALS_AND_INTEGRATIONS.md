# Credentials and integrations

| System | Authentication | Used by | Data exchanged | Configuration |
|---|---|---|---|---|
| PostgreSQL | service credentials | primary data source | Commercial fact and dimension tables | `DATABASE_URL` |
| Tableau Server / Cloud | site credentials | publishing layer | Workbook and datasource refresh | `Configured in Tableau` |
| CSV | filesystem | reference mappings | Targets and segment mappings | `INPUT_PATH` |

Credentials are never committed. Development, staging and production should use separate identities and least-privilege access.

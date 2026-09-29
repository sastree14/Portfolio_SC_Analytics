# Credentials and integrations

| System | Authentication | Used by | Data exchanged | Configuration |
|---|---|---|---|---|
| PostgreSQL | service credentials | data access layer | Historical measures and scenario inputs | `DATABASE_URL` |
| Shiny Server / Posit Connect | deployment credentials | application runtime | R application bundle | `Deployment environment` |
| CSV / Parquet | filesystem / object storage | public input | Historical time series | `DATA_PATH` |

Credentials are never committed. Development, staging and production should use separate identities and least-privilege access.

# Credentials and integrations

Credentials belong to the runtime environment, not source control.

| System | Authentication | Used by | Data exchanged | Environment configuration |
|---|---|---|---|---|
| PostgreSQL | service credentials | source connector | Operational tables | `SOURCE_DATABASE_URL` |
| AWS S3 | IAM access / role | object storage connector | Extracted files and snapshots | `AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY` |
| Azure Blob Storage | connection string / managed identity | object storage connector | Extracted files and snapshots | `AZURE_STORAGE_CONNECTION_STRING` |
| ClickHouse | service credentials | analytical store | Curated analytical tables | `CLICKHOUSE_URL` |
| Airflow | connection objects | orchestration | Task schedules and connection references | `Configured in Airflow` |

## Permission principles

- use the narrowest scope compatible with the operation
- separate development, staging and production credentials
- rotate long-lived secrets
- avoid embedding tokens in workflow exports or notebooks
- record external writes when the workflow can modify a business system

## Secret storage

Suitable options include GitHub environment secrets, AWS Secrets Manager, Azure Key Vault or the deployment platform's native secret store.

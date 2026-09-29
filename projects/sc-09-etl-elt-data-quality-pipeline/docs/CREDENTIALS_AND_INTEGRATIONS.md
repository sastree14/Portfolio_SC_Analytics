# Credentials and integrations

Credentials belong to the runtime environment, not source control.

| System | Authentication | Used by | Data exchanged | Environment configuration |
|---|---|---|---|---|
| DuckDB | local file / service path | warehouse engine | Staging and mart tables | `DUCKDB_PATH` |
| Parquet | filesystem / object storage | exchange format | Raw and curated datasets | `DATA_PATH` |
| Airflow | connection objects | orchestration | Scheduled dbt and validation tasks | `Configured in Airflow` |
| GitHub Actions | repository permissions | CI | Tests and build status | `GitHub environment` |

## Permission principles

- use the narrowest scope compatible with the operation
- separate development, staging and production credentials
- rotate long-lived secrets
- avoid embedding tokens in workflow exports or notebooks
- record external writes when the workflow can modify a business system

## Secret storage

Suitable options include GitHub environment secrets, AWS Secrets Manager, Azure Key Vault or the deployment platform's native secret store.

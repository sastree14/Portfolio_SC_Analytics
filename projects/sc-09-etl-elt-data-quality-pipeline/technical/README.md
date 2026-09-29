# Technical implementation

This is the code-level entry point for **SC-09 · ETL / ELT & Data Quality Pipeline**.

## Main responsibilities

- dbt owns transformation lineage and SQL model tests.
- Pandera validates dataframe contracts before SQL transformations.
- DuckDB keeps the public example runnable locally without weakening the warehouse pattern.

## Technical map

- `README.md/` — project implementation asset
- `data/` — project implementation asset
- `dbt/` — project implementation asset
- `infra/` — project implementation asset
- `requirements.txt/` — project implementation asset
- `scripts/` — project implementation asset
- `sql/` — project implementation asset
- `src/` — project implementation asset
- `tests/` — project implementation asset

## Technology

- dbt
- DuckDB
- Python
- Pandera
- Parquet
- Apache Airflow
- SQL
- Docker
- GitHub Actions

## Validation

See [VALIDATION.md](VALIDATION.md) for the checks included with this project.

## Local execution

Use the project-specific dependency file, environment example and scripts in this directory. External credentials are not required for the deterministic public path unless the project documentation explicitly says otherwise.

## Read next

- [Architecture](../docs/ARCHITECTURE.md)
- [Technical decisions](../docs/TECHNICAL_DECISIONS.md)
- [Credentials and integrations](../docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Security and permissions](../docs/SECURITY_AND_PERMISSIONS.md)

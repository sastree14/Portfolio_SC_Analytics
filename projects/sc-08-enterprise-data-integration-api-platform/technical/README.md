# Technical implementation

This is the code-level entry point for **SC-08 · Enterprise Data Integration & API Platform**.

## Main responsibilities

- Airflow owns scheduling and dependencies, not transformation semantics.
- Object storage provides a replayable boundary between extraction and downstream processing.
- ClickHouse is used for analytical access; PostgreSQL remains suited to transactional metadata.

## Technical map

- `README.md/` — project implementation asset
- `airflow/` — project implementation asset
- `data/` — project implementation asset
- `infra/` — project implementation asset
- `requirements.txt/` — project implementation asset
- `scripts/` — project implementation asset
- `sql/` — project implementation asset
- `src/` — project implementation asset
- `tests/` — project implementation asset

## Technology

- Python
- FastAPI
- Apache Airflow
- PostgreSQL
- ClickHouse
- AWS S3
- Azure Blob Storage
- Docker
- SQL

## Validation

See [VALIDATION.md](VALIDATION.md) for the checks included with this project.

## Local execution

Use the project-specific dependency file, environment example and scripts in this directory. External credentials are not required for the deterministic public path unless the project documentation explicitly says otherwise.

## Read next

- [Architecture](../docs/ARCHITECTURE.md)
- [Technical decisions](../docs/TECHNICAL_DECISIONS.md)
- [Credentials and integrations](../docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Security and permissions](../docs/SECURITY_AND_PERMISSIONS.md)

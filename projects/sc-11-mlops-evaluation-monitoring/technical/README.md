# Technical implementation

This is the code-level entry point for **SC-11 · ML / AI Evaluation & Monitoring Platform**.

## Main responsibilities

- MLflow records experiment lineage and artefacts.
- Evidently handles explicit data/prediction monitoring reports.
- Promotion is a gated decision rather than an automatic consequence of training completion.

## Technical map

- `.github/` — project implementation asset
- `README.md/` — project implementation asset
- `data/` — project implementation asset
- `requirements.txt/` — project implementation asset
- `sql/` — project implementation asset
- `src/` — project implementation asset
- `tests/` — project implementation asset

## Technology

- Python
- MLflow
- Evidently
- FastAPI
- PostgreSQL
- Docker
- GitHub Actions
- Prometheus

## Validation

See [VALIDATION.md](VALIDATION.md) for the checks included with this project.

## Local execution

Use the project-specific dependency file, environment example and scripts in this directory. External credentials are not required for the deterministic public path unless the project documentation explicitly says otherwise.

## Read next

- [Architecture](../docs/ARCHITECTURE.md)
- [Technical decisions](../docs/TECHNICAL_DECISIONS.md)
- [Credentials and integrations](../docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Security and permissions](../docs/SECURITY_AND_PERMISSIONS.md)

# Technical implementation

This is the code-level entry point for **SC-10 · Real-Time Analytics & Monitoring Platform**.

## Main responsibilities

- Kafka-compatible transport decouples producers and consumers.
- ClickHouse is chosen for high-rate analytical inserts and queries.
- Grafana reads operational metrics; it is not the system of record.

## Technical map

- `README.md/` — project implementation asset
- `data/` — project implementation asset
- `grafana/` — project implementation asset
- `infra/` — project implementation asset
- `requirements.txt/` — project implementation asset
- `scripts/` — project implementation asset
- `sql/` — project implementation asset
- `src/` — project implementation asset
- `streaming/` — project implementation asset
- `tests/` — project implementation asset

## Technology

- Redpanda / Kafka
- ClickHouse
- Python
- FastAPI
- WebSockets
- Grafana
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

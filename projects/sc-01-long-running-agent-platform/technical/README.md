# Technical implementation

This is the code-level entry point for **SC-01 · Long-Running AI Agent Platform**.

## Main responsibilities

- PostgreSQL is the source of truth; Redis is transport, not business state.
- Provider adapters keep orchestration independent from one model vendor.
- Human approval is a first-class state transition rather than a prompt instruction.

## Technical map

- `README.md/` — project implementation asset
- `infra/` — project implementation asset
- `requirements.txt/` — project implementation asset
- `scripts/` — project implementation asset
- `sql/` — project implementation asset
- `src/` — project implementation asset
- `tests/` — project implementation asset

## Technology

- Python
- FastAPI
- PostgreSQL
- Redis
- Celery
- Docker
- OpenAI
- Anthropic
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

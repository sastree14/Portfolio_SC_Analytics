# Technical implementation

This is the code-level entry point for **SC-06 · AI Workflow Automation Hub**.

## Main responsibilities

- n8n is used for orchestration rather than as the place where domain logic is hidden.
- Webhook adapters make Zapier and Make optional edges rather than hard dependencies.
- Run state is persisted outside the workflow tool for auditability.

## Technical map

- `README.md/` — project implementation asset
- `connectors/` — project implementation asset
- `data/` — project implementation asset
- `infra/` — project implementation asset
- `requirements.txt/` — project implementation asset
- `scripts/` — project implementation asset
- `sql/` — project implementation asset
- `src/` — project implementation asset
- `tests/` — project implementation asset
- `workflows/` — project implementation asset

## Technology

- n8n
- Python
- FastAPI
- PostgreSQL
- Redis
- Webhooks
- Zapier Webhooks
- Make Webhooks
- Docker

## Validation

See [VALIDATION.md](VALIDATION.md) for the checks included with this project.

## Local execution

Use the project-specific dependency file, environment example and scripts in this directory. External credentials are not required for the deterministic public path unless the project documentation explicitly says otherwise.

## Read next

- [Architecture](../docs/ARCHITECTURE.md)
- [Technical decisions](../docs/TECHNICAL_DECISIONS.md)
- [Credentials and integrations](../docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Security and permissions](../docs/SECURITY_AND_PERMISSIONS.md)

# Technical implementation

This is the code-level entry point for **SC-03 · AI Sales & CRM Automation System**.

## Main responsibilities

- HubSpot remains the operational system of record while the application owns scoring and proposed actions.
- n8n handles cross-system workflow steps; model logic stays outside the workflow canvas.
- Outbound writes are gated so a generated message cannot silently mutate CRM state.

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

- Python
- FastAPI
- PostgreSQL
- n8n
- HubSpot API
- Webhooks
- OpenAI
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

# Technical implementation

This is the code-level entry point for **SC-04 · AI Receptionist & Lead Qualification**.

## Main responsibilities

- Fastify keeps the webhook boundary small and explicit.
- Twilio and Calendly are isolated behind provider-specific connectors.
- Qualification fields are structured before routing so downstream systems do not depend on free-form text.

## Technical map

- `README.md/` — project implementation asset
- `app/` — project implementation asset
- `data/` — project implementation asset
- `infra/` — project implementation asset
- `requirements.txt/` — project implementation asset
- `scripts/` — project implementation asset
- `sql/` — project implementation asset
- `src/` — project implementation asset
- `tests/` — project implementation asset

## Technology

- TypeScript
- Node.js
- Fastify
- Twilio
- Calendly
- OpenAI
- PostgreSQL
- Docker
- Webhooks

## Validation

See [VALIDATION.md](VALIDATION.md) for the checks included with this project.

## Local execution

Use the project-specific dependency file, environment example and scripts in this directory. External credentials are not required for the deterministic public path unless the project documentation explicitly says otherwise.

## Read next

- [Architecture](../docs/ARCHITECTURE.md)
- [Technical decisions](../docs/TECHNICAL_DECISIONS.md)
- [Credentials and integrations](../docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Security and permissions](../docs/SECURITY_AND_PERMISSIONS.md)

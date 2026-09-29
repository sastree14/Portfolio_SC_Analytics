# Technical implementation

This is the code-level entry point for **SC-02 · Multi-Agent Operations Orchestrator**.

## Main responsibilities

- LangGraph makes control flow explicit instead of relying on recursive prompting.
- Pydantic contracts constrain inter-agent payloads.
- Execution is separated from review so the reviewing agent cannot silently perform the action.

## Technical map

- `README.md/` — project implementation asset
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
- LangGraph
- PostgreSQL
- Redis
- Docker
- OpenAI
- Anthropic
- Pydantic

## Validation

See [VALIDATION.md](VALIDATION.md) for the checks included with this project.

## Local execution

Use the project-specific dependency file, environment example and scripts in this directory. External credentials are not required for the deterministic public path unless the project documentation explicitly says otherwise.

## Read next

- [Architecture](../docs/ARCHITECTURE.md)
- [Technical decisions](../docs/TECHNICAL_DECISIONS.md)
- [Credentials and integrations](../docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Security and permissions](../docs/SECURITY_AND_PERMISSIONS.md)

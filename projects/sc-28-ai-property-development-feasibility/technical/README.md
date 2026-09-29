# Technical implementation

This is the code-level entry point for **SC-28 · AI Property Development Feasibility & Operations System**.

## Main responsibilities

- Financial feasibility remains deterministic even when AI extracts inputs from documents.
- GeoPandas handles spatial context without making geospatial enrichment a hidden black box.
- n8n coordinates review steps while the financial model remains version-controlled code.

## Technical map

- `README.md/` — project implementation asset
- `data/` — project implementation asset
- `requirements.txt/` — project implementation asset
- `sql/` — project implementation asset
- `src/` — project implementation asset
- `tests/` — project implementation asset
- `workflows/` — project implementation asset

## Technology

- Python
- FastAPI
- PostgreSQL
- Pandas
- GeoPandas
- OpenAI
- n8n
- Docker
- Plotly

## Validation

See [VALIDATION.md](VALIDATION.md) for the checks included with this project.

## Local execution

Use the project-specific dependency file, environment example and scripts in this directory. External credentials are not required for the deterministic public path unless the project documentation explicitly says otherwise.

## Read next

- [Architecture](../docs/ARCHITECTURE.md)
- [Technical decisions](../docs/TECHNICAL_DECISIONS.md)
- [Credentials and integrations](../docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Security and permissions](../docs/SECURITY_AND_PERMISSIONS.md)

# Technical implementation

This is the code-level entry point for **SC-24 · Financial Modelling & Scenario Engine**.

## Main responsibilities

- The model is driver-based so assumptions remain visible.
- Python performs the calculation while Excel remains an accessible exchange/output format.
- Actuals and forecast scenarios are kept separate to preserve model traceability.

## Technical map

- `README.md/` — project implementation asset
- `data/` — project implementation asset
- `requirements.txt/` — project implementation asset
- `sql/` — project implementation asset
- `src/` — project implementation asset
- `tests/` — project implementation asset

## Technology

- Python
- Pandas
- NumPy
- OpenPyXL
- Plotly
- FastAPI
- PostgreSQL
- Excel

## Validation

See [VALIDATION.md](VALIDATION.md) for the checks included with this project.

## Local execution

Use the project-specific dependency file, environment example and scripts in this directory. External credentials are not required for the deterministic public path unless the project documentation explicitly says otherwise.

## Read next

- [Architecture](../docs/ARCHITECTURE.md)
- [Technical decisions](../docs/TECHNICAL_DECISIONS.md)
- [Credentials and integrations](../docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Security and permissions](../docs/SECURITY_AND_PERMISSIONS.md)

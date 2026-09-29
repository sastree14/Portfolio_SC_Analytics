# Technical implementation

This is the code-level entry point for **SC-27 · Quantitative Trading & Market Microstructure System**.

## Main responsibilities

- ClickHouse retains high-frequency event history while Redis keeps current live state.
- Research and execution are deliberately separated; the public project does not route orders.
- Transaction costs are part of backtest evaluation rather than an afterthought.

## Technical map

- `README.md/` — project implementation asset
- `data/` — project implementation asset
- `requirements.txt/` — project implementation asset
- `sql/` — project implementation asset
- `src/` — project implementation asset
- `tests/` — project implementation asset
- `ui/` — project implementation asset

## Technology

- Python
- TypeScript
- WebSockets
- ClickHouse
- Redis
- Pandas
- NumPy
- Plotly
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

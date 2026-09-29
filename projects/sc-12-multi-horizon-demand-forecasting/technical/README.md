# Technical implementation

This is the code-level entry point for **SC-12 · Multi-Horizon Demand Forecasting & Inventory Planning**.

## Main responsibilities

- Horizon-level backtesting prevents one aggregate metric from hiding weak long-range performance.
- Statistical baselines remain mandatory reference points.
- Model selection is based on out-of-sample performance, not in-sample fit.

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
- Statsmodels
- XGBoost
- LightGBM
- Plotly
- FastAPI
- PostgreSQL

## Validation

See [VALIDATION.md](VALIDATION.md) for the checks included with this project.

## Local execution

Use the project-specific dependency file, environment example and scripts in this directory. External credentials are not required for the deterministic public path unless the project documentation explicitly says otherwise.

## Read next

- [Architecture](../docs/ARCHITECTURE.md)
- [Technical decisions](../docs/TECHNICAL_DECISIONS.md)
- [Credentials and integrations](../docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Security and permissions](../docs/SECURITY_AND_PERMISSIONS.md)

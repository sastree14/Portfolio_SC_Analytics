# Technical implementation

This is the code-level entry point for **SC-18 · Credit Risk & Profit Optimization Engine**.

## Main responsibilities

- Risk prediction and economic decision logic are separated so policy can change without retraining the model.
- Calibration matters because probabilities feed expected-loss calculations.
- Optimization is constrained by risk appetite rather than maximizing approvals.

## Technical map

- `README.md/` — project implementation asset
- `data/` — project implementation asset
- `requirements.txt/` — project implementation asset
- `sql/` — project implementation asset
- `src/` — project implementation asset
- `tests/` — project implementation asset

## Technology

- Python
- XGBoost
- SHAP
- Scikit-learn
- Optuna
- FastAPI
- PostgreSQL
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

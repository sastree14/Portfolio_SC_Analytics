# Technical implementation

This is the code-level entry point for **SC-19 · Fraud Detection & Explainability System**.

## Main responsibilities

- PR-oriented evaluation is preferred because fraud is imbalanced.
- Thresholds are optimized against review capacity and cost.
- Explanation output is stored with the scored transaction for investigator review.

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
- Imbalanced-learn
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

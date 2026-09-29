# SC-19 · Fraud Detection & Explainability System

**A cost-sensitive fraud scoring system with threshold optimization, explainability and investigation prioritization.**

Designed for **Payments · banking · insurance · marketplaces · transaction monitoring**.

## Business impact

- Prioritize the transactions most worth reviewing
- Balance fraud capture against false-positive customer friction
- Explain why a transaction was scored as suspicious
- Tune decision thresholds using business cost rather than accuracy alone

[Business impact in detail →](docs/BUSINESS_IMPACT.md)

## Example use case

A transaction receives a fraud probability and explanation. The threshold is selected based on review capacity and expected loss, then high-priority cases are sent to investigation.

## Technology at a glance

**Python · XGBoost · SHAP · Scikit-learn · Imbalanced-learn · FastAPI · PostgreSQL · Plotly**

## What a reviewer can inspect

- [Architecture](docs/ARCHITECTURE.md)
- [Credentials and integrations](docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Environments](docs/ENVIRONMENTS.md)
- [Limitations](docs/LIMITATIONS.md)
- [Example output](examples/outputs/result.json)
- [Execution log](examples/logs/example.log)
- [Generated analytical visual](examples/visuals/result.svg)
- [Technical implementation](technical/README.md)

## Run locally

See [technical/README.md](technical/README.md) for the project-specific execution path.

## Technology and business are separated deliberately

A non-technical reviewer can understand the decision and impact from this page. A technical reviewer can enter the implementation, SQL, model logic, tests and environment configuration directly.

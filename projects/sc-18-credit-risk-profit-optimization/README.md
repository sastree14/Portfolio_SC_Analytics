# SC-18 · Credit Risk & Profit Optimization Engine

**A lending decision engine that combines probability of default, expected loss, pricing and constrained profit optimization.**

Designed for **Banks · lenders · fintech · credit teams · risk analytics**.

## Business impact

- Move beyond a probability-of-default score to a complete lending decision
- Balance expected revenue against expected loss
- Make approval thresholds and risk appetite explicit
- Explain important risk drivers for each application

[Business impact in detail →](docs/BUSINESS_IMPACT.md)

## Example use case

For each application the engine estimates default risk, expected loss and expected contribution, then recommends approve, decline or review under a defined risk appetite.

## Technology at a glance

**Python · XGBoost · SHAP · Scikit-learn · Optuna · FastAPI · PostgreSQL · Plotly**

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

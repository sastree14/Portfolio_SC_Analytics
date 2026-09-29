# SC-17 · Customer Intelligence: Churn, CLV & Segmentation

**A customer analytics system combining churn probability, lifetime value, segmentation and time-to-event analysis.**

Designed for **Subscription businesses · SaaS · telecom · retail · customer success**.

## Business impact

- Prioritize retention effort using both risk and customer value
- Separate who may churn from when churn is likely
- Create interpretable customer segments for commercial action
- Combine model outputs into one next-best-action layer

[Business impact in detail →](docs/BUSINESS_IMPACT.md)

## Example use case

A customer-success team receives a prioritized list that combines churn risk, expected value and predicted time-to-event instead of treating every high-risk customer equally.

## Technology at a glance

**Python · Scikit-learn · XGBoost · Lifelines · SHAP · Pandas · FastAPI · PostgreSQL**

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

# SC-19 · Fraud Detection & Explainability System

**A cost-sensitive fraud scoring system with threshold optimization, explanations and investigation prioritization.**

**Designed for:** Payments · banking · insurance · marketplaces

## Why this project matters

- Prioritize limited investigation capacity
- Balance fraud capture against false positives
- Explain suspicious scores
- Choose thresholds using cost rather than accuracy

A business reviewer can stay on this page. A technical reviewer can move directly to the [technical implementation](technical/README.md).

## Example operating flow

```text
Transaction
    ↓\n    Feature layer
        ↓\n        Fraud model
            ↓\n            Probability calibration
                ↓\n                SHAP explanation
                    ↓\n                    Cost-aware threshold
                        ↓\n                        Review queue
```

## Technology at a glance

**Python · XGBoost · SHAP · Scikit-learn · Imbalanced-learn · FastAPI · PostgreSQL · Plotly**

The stack is shown early because technical fit matters. The project is still explained in business terms first.

## What is included

- [Business impact and KPIs](docs/BUSINESS_IMPACT.md)
- [Example results and how to read them](docs/RESULTS.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Technical decisions](docs/TECHNICAL_DECISIONS.md)
- [Data and public sample structure](docs/DATA.md)
- [Security and permissions](docs/SECURITY_AND_PERMISSIONS.md)
- [Credentials and integrations](docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Environments](docs/ENVIRONMENTS.md)
- [Limitations](docs/LIMITATIONS.md)
- [Example inputs, outputs and logs](examples/README.md)
- [Technical implementation, SQL and tests](technical/README.md)

## What the example data represents

Representative transaction and entity features, imbalanced labels, fraud probabilities, explanations and review decisions.

The repository does not contain client credentials or confidential records.

## Local review

The public implementation is designed so that the core example can be inspected locally without production credentials. Tool-specific connectors are configured through environment variables and are documented separately.

[Open the technical implementation →](technical/README.md)

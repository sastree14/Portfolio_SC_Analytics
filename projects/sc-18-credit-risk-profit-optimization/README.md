# SC-18 · Credit Risk & Profit Optimization Engine

**A lending decision engine combining default risk, expected loss, pricing and constrained contribution optimization.**

**Designed for:** Banks · lenders · fintech · credit teams

## Why this project matters

- Move beyond a probability score to a lending decision
- Balance revenue against expected loss
- Make risk appetite explicit
- Explain material risk drivers

A business reviewer can stay on this page. A technical reviewer can move directly to the [technical implementation](technical/README.md).

## Example operating flow

```text
Application
    ↓\n    Feature validation
        ↓\n        PD model
            ↓\n            Calibration + explainability
                ↓\n                Expected loss
                    ↓\n                    Contribution model
                        ↓\n                        Approve / review / decline
```

## Technology at a glance

**Python · XGBoost · SHAP · Scikit-learn · Optuna · FastAPI · PostgreSQL · Plotly**

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

Representative applicant features, outcomes, risk scores, explanations, expected-loss calculations and decision outputs.

The repository does not contain client credentials or confidential records.

## Local review

The public implementation is designed so that the core example can be inspected locally without production credentials. Tool-specific connectors are configured through environment variables and are documented separately.

[Open the technical implementation →](technical/README.md)

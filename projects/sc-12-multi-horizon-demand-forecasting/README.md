# SC-12 · Multi-Horizon Demand Forecasting & Inventory Planning

**A forecasting system that compares baselines and machine-learning models across multiple planning horizons.**

**Designed for:** E-commerce · retail · inventory planning · finance

## Why this project matters

- Measure forecast quality by horizon
- Expose forecast bias as well as absolute error
- Translate predictions into planning decisions
- Benchmark complex models against simple baselines

A business reviewer can stay on this page. A technical reviewer can move directly to the [technical implementation](technical/README.md).

## Example operating flow

```text
Orders + inventory
    ↓\n    Feature engineering
        ↓\n        Baseline models
            ↓\n            ML candidates
                ↓\n                Backtesting by horizon
                    ↓\n                    Forecast selection
                        ↓\n                        Planning output
```

## Technology at a glance

**Python · Pandas · Statsmodels · XGBoost · LightGBM · Plotly · FastAPI · PostgreSQL**

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

Representative SKU history, calendar features, backtest folds, horizon-level metrics, forecasts and prediction intervals.

The repository does not contain client credentials or confidential records.

## Local review

The public implementation is designed so that the core example can be inspected locally without production credentials. Tool-specific connectors are configured through environment variables and are documented separately.

[Open the technical implementation →](technical/README.md)

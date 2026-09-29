# SC-12 · Multi-Horizon Demand Forecasting & Inventory Planning

**A forecasting system that compares baselines and machine-learning models across multiple planning horizons.**

Designed for **E-commerce · retail · inventory planning · finance · operations**.

## Business impact

- Measure forecast quality separately by planning horizon
- Expose bias as well as absolute forecast error
- Translate forecasts into inventory and purchasing decisions
- Compare complex models against simple operational baselines

[Business impact in detail →](docs/BUSINESS_IMPACT.md)

## Example use case

Daily SKU demand is forecast at H1, H3, H6 and H9. The system backtests each horizon, compares baseline and ML approaches, then exposes the selected forecast with prediction intervals.

## Technology at a glance

**Python · Pandas · Statsmodels · XGBoost · LightGBM · Plotly · FastAPI · PostgreSQL**

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

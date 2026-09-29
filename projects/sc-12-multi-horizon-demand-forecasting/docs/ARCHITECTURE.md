# Architecture

## Objective

A forecasting system that compares baselines and machine-learning models across multiple planning horizons.

```text
Source data / user input
          ↓
Validation and feature layer
          ↓
Multi-Horizon Demand Forecasting & Inventory Planning
          ↓
Decision / analytical output
          ↓
Integration or user interface
          ↓
Monitoring and review
```

## Technology responsibilities

- **Python** — part of the implemented analytical or serving path.
- **Pandas** — part of the implemented analytical or serving path.
- **Statsmodels** — part of the implemented analytical or serving path.
- **XGBoost** — part of the implemented analytical or serving path.
- **LightGBM** — part of the implemented analytical or serving path.
- **Plotly** — part of the implemented analytical or serving path.
- **FastAPI** — part of the implemented analytical or serving path.
- **PostgreSQL** — part of the implemented analytical or serving path.

## Integration boundaries

- **PostgreSQL** — historical source; exchanges orders, inventory and product attributes.
- **FastAPI** — forecast serving; exchanges forecast requests and scenario outputs.
- **Object storage** — model artefacts; exchanges backtests and trained artefacts.

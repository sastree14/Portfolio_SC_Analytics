# Technical decisions

The stack is not a list of logos. Each technology has to earn its place in the architecture.

## Key decisions

1. Horizon-level backtesting prevents one aggregate metric from hiding weak long-range performance.
2. Statistical baselines remain mandatory reference points.
3. Model selection is based on out-of-sample performance, not in-sample fit.

## Technology footprint

- **Python**
- **Pandas**
- **Statsmodels**
- **XGBoost**
- **LightGBM**
- **Plotly**
- **FastAPI**
- **PostgreSQL**

## Decision rule

If a simpler component can meet the same operational requirement with lower maintenance cost, it should be preferred. The public implementation keeps boundaries explicit so individual tools can be replaced without redesigning the whole project.

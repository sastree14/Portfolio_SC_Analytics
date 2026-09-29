# Technical decisions

The stack is not a list of logos. Each technology has to earn its place in the architecture.

## Key decisions

1. Elasticity estimation is kept separate from the optimizer so demand assumptions can be challenged.
2. Hard commercial constraints prevent mathematically optimal but unusable prices.
3. Scenario outputs expose demand and margin trade-offs rather than only one chosen price.

## Technology footprint

- **Python**
- **Pandas**
- **NumPy**
- **SciPy**
- **Statsmodels**
- **XGBoost**
- **Optuna**
- **FastAPI**
- **Plotly**

## Decision rule

If a simpler component can meet the same operational requirement with lower maintenance cost, it should be preferred. The public implementation keeps boundaries explicit so individual tools can be replaced without redesigning the whole project.

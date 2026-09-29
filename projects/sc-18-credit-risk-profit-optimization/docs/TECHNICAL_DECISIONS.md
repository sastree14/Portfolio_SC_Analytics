# Technical decisions

The stack is not a list of logos. Each technology has to earn its place in the architecture.

## Key decisions

1. Risk prediction and economic decision logic are separated so policy can change without retraining the model.
2. Calibration matters because probabilities feed expected-loss calculations.
3. Optimization is constrained by risk appetite rather than maximizing approvals.

## Technology footprint

- **Python**
- **XGBoost**
- **SHAP**
- **Scikit-learn**
- **Optuna**
- **FastAPI**
- **PostgreSQL**
- **Plotly**

## Decision rule

If a simpler component can meet the same operational requirement with lower maintenance cost, it should be preferred. The public implementation keeps boundaries explicit so individual tools can be replaced without redesigning the whole project.

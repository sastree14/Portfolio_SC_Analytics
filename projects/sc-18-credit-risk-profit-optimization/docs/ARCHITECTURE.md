# Architecture

## Objective

A lending decision engine that combines probability of default, expected loss, pricing and constrained profit optimization.

```text
Source data / user input
          ↓
Validation and feature layer
          ↓
Credit Risk & Profit Optimization Engine
          ↓
Decision / analytical output
          ↓
Integration or user interface
          ↓
Monitoring and review
```

## Technology responsibilities

- **Python** — part of the implemented analytical or serving path.
- **XGBoost** — part of the implemented analytical or serving path.
- **SHAP** — part of the implemented analytical or serving path.
- **Scikit-learn** — part of the implemented analytical or serving path.
- **Optuna** — part of the implemented analytical or serving path.
- **FastAPI** — part of the implemented analytical or serving path.
- **PostgreSQL** — part of the implemented analytical or serving path.
- **Plotly** — part of the implemented analytical or serving path.

## Integration boundaries

- **PostgreSQL** — application source; exchanges applicant, behavioural and outcome data.
- **FastAPI** — decision API; exchanges application features and decision output.
- **Model artefact store** — model registry; exchanges trained model and calibration artefacts.

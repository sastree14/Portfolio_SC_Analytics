# Architecture

## Objective

A cost-sensitive fraud scoring system with threshold optimization, explainability and investigation prioritization.

```text
Source data / user input
          ↓
Validation and feature layer
          ↓
Fraud Detection & Explainability System
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
- **Imbalanced-learn** — part of the implemented analytical or serving path.
- **FastAPI** — part of the implemented analytical or serving path.
- **PostgreSQL** — part of the implemented analytical or serving path.
- **Plotly** — part of the implemented analytical or serving path.

## Integration boundaries

- **PostgreSQL** — transaction source; exchanges transactions, entities and labels.
- **FastAPI** — scoring API; exchanges transaction features and fraud score.
- **Case-management webhook** — investigation connector; exchanges high-priority cases and explanations.

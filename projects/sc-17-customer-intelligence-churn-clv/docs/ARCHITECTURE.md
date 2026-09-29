# Architecture

## Objective

A customer analytics system combining churn probability, lifetime value, segmentation and time-to-event analysis.

```text
Source data / user input
          ↓
Validation and feature layer
          ↓
Customer Intelligence: Churn, CLV & Segmentation
          ↓
Decision / analytical output
          ↓
Integration or user interface
          ↓
Monitoring and review
```

## Technology responsibilities

- **Python** — part of the implemented analytical or serving path.
- **Scikit-learn** — part of the implemented analytical or serving path.
- **XGBoost** — part of the implemented analytical or serving path.
- **Lifelines** — part of the implemented analytical or serving path.
- **SHAP** — part of the implemented analytical or serving path.
- **Pandas** — part of the implemented analytical or serving path.
- **FastAPI** — part of the implemented analytical or serving path.
- **PostgreSQL** — part of the implemented analytical or serving path.

## Integration boundaries

- **PostgreSQL** — customer source; exchanges customer, usage, billing and activity tables.
- **FastAPI** — scoring API; exchanges customer context and scores.
- **CRM webhook** — activation connector; exchanges priority customers and recommended action.

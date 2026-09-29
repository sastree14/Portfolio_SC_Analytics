# Technical decisions

The stack is not a list of logos. Each technology has to earn its place in the architecture.

## Key decisions

1. PR-oriented evaluation is preferred because fraud is imbalanced.
2. Thresholds are optimized against review capacity and cost.
3. Explanation output is stored with the scored transaction for investigator review.

## Technology footprint

- **Python**
- **XGBoost**
- **SHAP**
- **Scikit-learn**
- **Imbalanced-learn**
- **FastAPI**
- **PostgreSQL**
- **Plotly**

## Decision rule

If a simpler component can meet the same operational requirement with lower maintenance cost, it should be preferred. The public implementation keeps boundaries explicit so individual tools can be replaced without redesigning the whole project.

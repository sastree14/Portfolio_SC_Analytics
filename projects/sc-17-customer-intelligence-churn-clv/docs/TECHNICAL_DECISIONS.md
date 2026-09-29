# Technical decisions

The stack is not a list of logos. Each technology has to earn its place in the architecture.

## Key decisions

1. Classification and survival models answer different operational questions and remain separate.
2. CLV is combined with risk only after each component is validated.
3. SHAP explanations support review but do not replace business rules or fairness checks.

## Technology footprint

- **Python**
- **Scikit-learn**
- **XGBoost**
- **Lifelines**
- **SHAP**
- **Pandas**
- **FastAPI**
- **PostgreSQL**

## Decision rule

If a simpler component can meet the same operational requirement with lower maintenance cost, it should be preferred. The public implementation keeps boundaries explicit so individual tools can be replaced without redesigning the whole project.

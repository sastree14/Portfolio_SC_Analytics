# Technical decisions

The stack is not a list of logos. Each technology has to earn its place in the architecture.

## Key decisions

1. FAISS is responsible for candidate retrieval, not final business ranking.
2. LightGBM combines behavioural and retrieval features for the ranking stage.
3. Redis caches online features and recent results to keep serving latency predictable.

## Technology footprint

- **Python**
- **Scikit-learn**
- **LightGBM**
- **Sentence Transformers**
- **FAISS**
- **FastAPI**
- **PostgreSQL**
- **Redis**

## Decision rule

If a simpler component can meet the same operational requirement with lower maintenance cost, it should be preferred. The public implementation keeps boundaries explicit so individual tools can be replaced without redesigning the whole project.

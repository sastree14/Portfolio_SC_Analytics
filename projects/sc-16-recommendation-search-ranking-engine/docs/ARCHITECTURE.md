# Architecture

## Objective

A hybrid recommendation and ranking system combining behavioural signals, content similarity and business rules.

```text
Source data / user input
          ↓
Validation and feature layer
          ↓
Recommendation, Search & Ranking Engine
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
- **LightGBM** — part of the implemented analytical or serving path.
- **Sentence Transformers** — part of the implemented analytical or serving path.
- **FAISS** — part of the implemented analytical or serving path.
- **FastAPI** — part of the implemented analytical or serving path.
- **PostgreSQL** — part of the implemented analytical or serving path.
- **Redis** — part of the implemented analytical or serving path.

## Integration boundaries

- **PostgreSQL** — behaviour source; exchanges users, items and interactions.
- **FAISS** — vector index; exchanges item embeddings.
- **Redis** — online cache; exchanges recent rankings and item features.
- **FastAPI** — serving API; exchanges user context and ranked items.

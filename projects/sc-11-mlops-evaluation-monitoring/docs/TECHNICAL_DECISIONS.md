# Technical decisions

The stack is not a list of logos. Each technology has to earn its place in the architecture.

## Key decisions

1. MLflow records experiment lineage and artefacts.
2. Evidently handles explicit data/prediction monitoring reports.
3. Promotion is a gated decision rather than an automatic consequence of training completion.

## Technology footprint

- **Python**
- **MLflow**
- **Evidently**
- **FastAPI**
- **PostgreSQL**
- **Docker**
- **GitHub Actions**
- **Prometheus**

## Decision rule

If a simpler component can meet the same operational requirement with lower maintenance cost, it should be preferred. The public implementation keeps boundaries explicit so individual tools can be replaced without redesigning the whole project.

# Technical decisions

The stack is not a list of logos. Each technology has to earn its place in the architecture.

## Key decisions

1. Airflow owns scheduling and dependencies, not transformation semantics.
2. Object storage provides a replayable boundary between extraction and downstream processing.
3. ClickHouse is used for analytical access; PostgreSQL remains suited to transactional metadata.

## Technology footprint

- **Python**
- **FastAPI**
- **Apache Airflow**
- **PostgreSQL**
- **ClickHouse**
- **AWS S3**
- **Azure Blob Storage**
- **Docker**
- **SQL**

## Decision rule

If a simpler component can meet the same operational requirement with lower maintenance cost, it should be preferred. The public implementation keeps boundaries explicit so individual tools can be replaced without redesigning the whole project.

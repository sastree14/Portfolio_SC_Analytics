# Technical decisions

The stack is not a list of logos. Each technology has to earn its place in the architecture.

## Key decisions

1. Object storage holds source artefacts while PostgreSQL stores document and job metadata.
2. Qdrant is responsible only for retrieval; findings remain persisted separately.
3. Evidence is carried into the finding record so synthesis can be audited.

## Technology footprint

- **Python**
- **FastAPI**
- **Qdrant**
- **PostgreSQL**
- **PyMuPDF**
- **OpenAI**
- **S3 / MinIO**
- **Docker**
- **Pydantic**

## Decision rule

If a simpler component can meet the same operational requirement with lower maintenance cost, it should be preferred. The public implementation keeps boundaries explicit so individual tools can be replaced without redesigning the whole project.

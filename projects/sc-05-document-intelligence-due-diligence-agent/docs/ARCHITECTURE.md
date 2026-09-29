# Architecture

## Objective

A document-analysis system that extracts evidence, retrieves supporting passages and produces reviewable findings.

## Logical flow

```text
Sources / request
      ↓
Input validation
      ↓
Document Intelligence & Due Diligence Agent
      ↓
Decision / processing layer
      ↓
External integrations
      ↓
Persisted output + monitoring
```

## Responsibilities

The implementation separates input handling, domain logic, integrations and persistence so each concern can be tested and changed independently.

## Technology choices

- **Python** — used where it has a clear responsibility in the implementation.
- **FastAPI** — used where it has a clear responsibility in the implementation.
- **Qdrant** — used where it has a clear responsibility in the implementation.
- **PostgreSQL** — used where it has a clear responsibility in the implementation.
- **PyMuPDF** — used where it has a clear responsibility in the implementation.
- **OpenAI** — used where it has a clear responsibility in the implementation.
- **S3 / MinIO** — used where it has a clear responsibility in the implementation.
- **Docker** — used where it has a clear responsibility in the implementation.
- **Pydantic** — used where it has a clear responsibility in the implementation.

## Integration boundaries

- **S3-compatible storage** — document store; exchanges source files and extracted artefacts.
- **Qdrant** — retrieval service; exchanges embeddings and document chunks.
- **OpenAI** — extraction / synthesis; exchanges selected chunks and structured prompts.
- **PostgreSQL** — application; exchanges document metadata, jobs and findings.

## Reliability

The technical layer includes deterministic local execution, example outputs, explicit failure logging and tests. Production deployments should add environment-specific monitoring, alerting and access controls.

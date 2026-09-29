# Technical implementation

This is the code-level entry point for **SC-16 · Recommendation, Search & Ranking Engine**.

## Main responsibilities

- FAISS is responsible for candidate retrieval, not final business ranking.
- LightGBM combines behavioural and retrieval features for the ranking stage.
- Redis caches online features and recent results to keep serving latency predictable.

## Technical map

- `README.md/` — project implementation asset
- `data/` — project implementation asset
- `requirements.txt/` — project implementation asset
- `sql/` — project implementation asset
- `src/` — project implementation asset
- `tests/` — project implementation asset

## Technology

- Python
- Scikit-learn
- LightGBM
- Sentence Transformers
- FAISS
- FastAPI
- PostgreSQL
- Redis

## Validation

See [VALIDATION.md](VALIDATION.md) for the checks included with this project.

## Local execution

Use the project-specific dependency file, environment example and scripts in this directory. External credentials are not required for the deterministic public path unless the project documentation explicitly says otherwise.

## Read next

- [Architecture](../docs/ARCHITECTURE.md)
- [Technical decisions](../docs/TECHNICAL_DECISIONS.md)
- [Credentials and integrations](../docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Security and permissions](../docs/SECURITY_AND_PERMISSIONS.md)

# Technical implementation

This directory contains the implementation behind **SC-02 · Multi-Agent Operations Orchestrator**.

## Map

- `src/` — executable domain example
- `tests/` — deterministic smoke tests
- `sql/` — persistence and operational queries
- `infra/` — local container configuration
- `scripts/` — example-output generation
- `data/` — representative input structure

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/main.py
pytest -q
```

## Stack

- Python
- FastAPI
- LangGraph
- PostgreSQL
- Redis
- Docker
- OpenAI
- Anthropic
- Pydantic

The project root README is intentionally business-first. This file is the entry point for code-level review.

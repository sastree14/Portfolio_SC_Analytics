# Technical implementation

This directory contains the implementation behind **SC-06 · AI Workflow Automation Hub**.

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

- n8n
- Python
- FastAPI
- PostgreSQL
- Redis
- Webhooks
- Zapier Webhooks
- Make Webhooks
- Docker

The project root README is intentionally business-first. This file is the entry point for code-level review.

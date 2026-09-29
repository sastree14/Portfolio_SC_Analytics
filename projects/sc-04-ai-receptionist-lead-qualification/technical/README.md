# Technical implementation

This directory contains the implementation behind **SC-04 · AI Receptionist & Lead Qualification**.

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

- TypeScript
- Node.js
- Fastify
- Twilio
- Calendly
- OpenAI
- PostgreSQL
- Docker
- Webhooks

The project root README is intentionally business-first. This file is the entry point for code-level review.

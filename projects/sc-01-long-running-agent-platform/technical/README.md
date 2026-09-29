# Technical implementation

This section contains the implementation behind SC-01.

The executive README at the project root explains the business problem and operating impact. This directory is intended for engineers who want to inspect how the platform is built.

## Repository map

- `src/app/` — API, persistence, orchestration and provider adapters
- `sql/` — schema, indexes, operational queries and monitoring queries
- `tests/` — unit and integration tests
- `infra/` — Docker image and local multi-service environment
- `scripts/` — utilities used to reproduce public examples

## Execution model

The platform separates durable business state from task delivery.

PostgreSQL stores the authoritative run and audit trail. Redis/Celery handles asynchronous task delivery in the Docker environment. A synchronous `inline` backend exists for deterministic local tests and example generation.

## Run tests

From `technical/`:

```bash
PYTHONPATH=src pytest -q
```

The test suite covers:

- API health
- complete approval flow
- event ordering
- invalid re-approval
- provider behaviour

## Generate public examples

```bash
python scripts/generate_examples.py
```

The script runs the actual application using the mock provider and writes inspectable JSON outputs and an execution log under `examples/`.

## Docker environment

From the project root:

```bash
cp .env.example .env
docker compose -f technical/infra/docker-compose.yml up --build
```

The Docker environment switches `TASK_BACKEND` to `celery` and starts API, worker, PostgreSQL and Redis as separate services.

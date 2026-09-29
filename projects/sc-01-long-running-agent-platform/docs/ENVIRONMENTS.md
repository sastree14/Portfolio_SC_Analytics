# Environments

## Local

Two local modes are supported.

**Deterministic mode** uses SQLite and the inline task backend. It is useful for tests and example generation.

**Service mode** uses Docker Compose with PostgreSQL, Redis, FastAPI and a Celery worker.

## Development

A shared development environment should use isolated non-production credentials, synthetic or approved data, lower model spending limits and non-production webhook endpoints.

## Testing

Tests use the mock model provider and do not require production APIs.

Important paths include:

- successful approval flow
- invalid state transitions
- provider output
- API health

## Staging

Staging should reproduce the production topology closely enough to validate database migrations, queue behaviour, external contracts, authorization, retries and worker restarts.

## Production considerations

A production deployment would normally separate:

- API service
- worker service
- managed PostgreSQL
- managed Redis
- secret storage
- centralized logs
- metrics and traces
- ingress/API gateway

Controls should include TLS, network restrictions, service identities, backups, rollback, alerting and model/API cost limits.

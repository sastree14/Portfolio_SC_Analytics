# Environments

## Local

Docker Compose starts:

- FastAPI
- Celery worker
- PostgreSQL
- Redis

The local environment is intended for development and inspection.

The default project configuration also supports SQLite when the application is run outside Docker and no `DATABASE_URL` is supplied.

## Development

A shared development environment should use separate non-production credentials and databases.

Recommended controls:

- non-production model keys
- isolated webhook endpoints
- lower model spending limits
- verbose application logs
- synthetic or approved test data

## Testing

Unit and integration tests should not depend on production APIs.

The included health test uses the local application directly.

Additional tests should use:

- mock model providers
- test database fixtures
- stubbed outbound HTTP responses
- deterministic approval flows

## Staging

A staging environment should reproduce the production topology closely enough to test:

- queue behaviour
- database migrations
- external integration contracts
- authorization
- retries
- worker restarts
- observability

## Production considerations

A production deployment should separate the application components into independently scalable services.

Typical responsibilities are:

```text
API service
Worker service
Managed PostgreSQL
Managed Redis
Secret manager
Centralized logs
Metrics / traces
Ingress / API gateway
```

Important controls include:

- TLS
- network restrictions
- service identities
- secret rotation
- database backups
- health checks
- autoscaling policy
- deployment rollback
- alerting
- cost limits for model providers

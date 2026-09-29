# Environments

## Local

The local path uses representative data and deterministic execution so the project can be inspected without production credentials.

## Development

Development should use isolated databases, non-production API keys and test endpoints.

## Testing

Tests should not depend on production services. External connectors are represented through deterministic adapters or mocks.

## Staging

Staging should reproduce the production topology sufficiently to validate credentials, network access, schemas, retries and integration contracts.

## Production considerations

Production should add centralized logging, metrics, alerts, backups, rollback procedures, environment-specific secrets and least-privilege service identities.

## Technology footprint

- Python
- FastAPI
- PostgreSQL
- n8n
- HubSpot API
- Webhooks
- OpenAI
- Docker
- SQL

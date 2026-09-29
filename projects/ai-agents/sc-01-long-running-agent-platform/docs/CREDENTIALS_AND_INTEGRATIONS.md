# Credentials and integrations

## Principle

Credentials belong to the runtime environment, not to source control.

The repository contains variable names and safe examples only.

## Application access

`APP_API_KEY`

Optional API key expected through the `X-API-Key` header.

For a multi-user production platform this should be replaced or complemented by proper identity and authorization, such as OAuth/OIDC and role-based access control.

## PostgreSQL

`DATABASE_URL`

Example local value:

```text
postgresql+psycopg://scanalytics:scanalytics@db:5432/agents
```

The Docker Compose credentials are local development credentials and are not appropriate for production.

A managed environment should use a dedicated application role with only the permissions required by the service.

## Redis

`CELERY_BROKER_URL`

`CELERY_RESULT_BACKEND`

In production, Redis should use authentication, encryption in transit and network-level access restrictions when provided by the selected service.

## OpenAI

`OPENAI_API_KEY`

`OPENAI_MODEL`

The adapter is activated when a run uses `provider=openai`.

The key should be stored in a secret manager or deployment-platform secret store.

## Anthropic

`ANTHROPIC_API_KEY`

`ANTHROPIC_MODEL`

The adapter is activated when a run uses `provider=anthropic`.

## Outbound business-system integration

`OUTBOUND_WEBHOOK_TOKEN`

When present, the token is sent as:

```text
Authorization: Bearer <token>
```

The webhook URL itself is supplied per run.

A production integration should normally use a more specific connector with:

- narrow scopes
- request signing where supported
- explicit timeout policy
- idempotency
- retry rules
- response validation
- audit logging

## Secret storage by environment

Suitable examples include:

- local: uncommitted `.env`
- GitHub Actions: encrypted repository or environment secrets
- AWS: Secrets Manager or Parameter Store
- Azure: Key Vault
- Kubernetes: external secret integration or sealed secret pattern

The repository does not imply that all of these services are used by this implementation. They are deployment options for the same secret-management requirement.

# Credentials and integrations

Credentials belong to the runtime environment, never to source control.

## Integration matrix

| System | Authentication | Used by | Data exchanged | Public configuration |
|---|---|---|---|---|
| Platform API | Optional API key | API clients | Run requests and state | `APP_API_KEY` |
| PostgreSQL | Connection credentials | API + worker | Runs and audit events | `DATABASE_URL` |
| Redis | Service connection | API/worker task layer | Task messages | `CELERY_BROKER_URL`, `CELERY_RESULT_BACKEND` |
| OpenAI | API key | Worker | Controlled task context / model output | `OPENAI_API_KEY`, `OPENAI_MODEL` |
| Anthropic | API key | Worker | Controlled task context / model output | `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL` |
| External webhook | Optional bearer token | Worker | Approved action payload / response | `OUTBOUND_WEBHOOK_TOKEN` |

## Permission design

A production deployment should use the narrowest permissions compatible with each integration.

Examples:

- database application roles should not be database administrators
- external-system tokens should be scoped to the actions the agent is allowed to perform
- model-provider keys should have environment-specific spending and usage controls where available
- staging credentials should not be reused in production

## Secret storage

Examples of suitable runtime secret stores include GitHub environment secrets, AWS Secrets Manager, Azure Key Vault or an equivalent platform secret store.

These are deployment options for the same secret-management requirement.

# Credentials and integrations

Credentials belong to the runtime environment, not source control.

| System | Authentication | Used by | Data exchanged | Environment configuration |
|---|---|---|---|---|
| OpenAI / Anthropic | API key | Planner and specialist agents | Task context and structured responses | `OPENAI_API_KEY / ANTHROPIC_API_KEY` |
| PostgreSQL | service credentials | API + workers | Workflow state, messages and audit events | `DATABASE_URL` |
| Redis | service connection | worker queue | Task delivery and transient coordination | `REDIS_URL` |
| External action API | Bearer token | executor agent | Approved action payload and response | `ACTION_API_TOKEN` |

## Permission principles

- use the narrowest scope compatible with the operation
- separate development, staging and production credentials
- rotate long-lived secrets
- avoid embedding tokens in workflow exports or notebooks
- record external writes when the workflow can modify a business system

## Secret storage

Suitable options include GitHub environment secrets, AWS Secrets Manager, Azure Key Vault or the deployment platform's native secret store.

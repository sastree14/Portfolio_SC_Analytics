# Credentials and integrations

Credentials belong to the runtime environment, not source control.

| System | Authentication | Used by | Data exchanged | Environment configuration |
|---|---|---|---|---|
| n8n | webhook / credential store | primary workflow engine | Workflow events and task payloads | `N8N_URL / N8N_API_KEY` |
| Zapier | catch hook | external workflow connector | Event payloads | `ZAPIER_WEBHOOK_URL` |
| Make | custom webhook | external workflow connector | Event payloads | `MAKE_WEBHOOK_URL` |
| PostgreSQL | service credentials | state store | Workflow runs, payload hashes and outcomes | `DATABASE_URL` |

## Permission principles

- use the narrowest scope compatible with the operation
- separate development, staging and production credentials
- rotate long-lived secrets
- avoid embedding tokens in workflow exports or notebooks
- record external writes when the workflow can modify a business system

## Secret storage

Suitable options include GitHub environment secrets, AWS Secrets Manager, Azure Key Vault or the deployment platform's native secret store.

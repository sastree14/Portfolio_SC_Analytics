# Credentials and integrations

Credentials belong to the runtime environment, not source control.

| System | Authentication | Used by | Data exchanged | Environment configuration |
|---|---|---|---|---|
| HubSpot | OAuth / private app token | CRM connector | Contacts, companies, deals and activity updates | `HUBSPOT_ACCESS_TOKEN` |
| n8n | Webhook credential | workflow layer | Event payloads and approved automation steps | `N8N_WEBHOOK_URL / N8N_WEBHOOK_SECRET` |
| OpenAI | API key | message drafting service | Selected CRM context and generated draft | `OPENAI_API_KEY` |
| PostgreSQL | service credentials | application | Lead scores, proposed actions and audit events | `DATABASE_URL` |

## Permission principles

- use the narrowest scope compatible with the operation
- separate development, staging and production credentials
- rotate long-lived secrets
- avoid embedding tokens in workflow exports or notebooks
- record external writes when the workflow can modify a business system

## Secret storage

Suitable options include GitHub environment secrets, AWS Secrets Manager, Azure Key Vault or the deployment platform's native secret store.

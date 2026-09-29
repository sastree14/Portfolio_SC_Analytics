# Credentials and integrations

Credentials belong to the runtime environment, not source control.

| System | Authentication | Used by | Data exchanged | Environment configuration |
|---|---|---|---|---|
| Twilio | API credentials | voice / messaging gateway | Inbound message metadata and response text | `TWILIO_ACCOUNT_SID / TWILIO_AUTH_TOKEN` |
| Calendly | OAuth / personal access token | scheduling connector | Availability and booking hand-off | `CALENDLY_TOKEN` |
| OpenAI | API key | conversation engine | Conversation context and structured extraction | `OPENAI_API_KEY` |
| PostgreSQL | service credentials | application | Enquiries, qualification fields and routing state | `DATABASE_URL` |

## Permission principles

- use the narrowest scope compatible with the operation
- separate development, staging and production credentials
- rotate long-lived secrets
- avoid embedding tokens in workflow exports or notebooks
- record external writes when the workflow can modify a business system

## Secret storage

Suitable options include GitHub environment secrets, AWS Secrets Manager, Azure Key Vault or the deployment platform's native secret store.

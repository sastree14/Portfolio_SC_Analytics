# Credentials and integrations

Credentials belong to the runtime environment, not source control.

| System | Authentication | Used by | Data exchanged | Environment configuration |
|---|---|---|---|---|
| Supabase | service role / anon key | application data layer | Users, conversations and tool results | `NEXT_PUBLIC_SUPABASE_URL / SUPABASE_SERVICE_ROLE_KEY` |
| OpenAI | API key | LLM service | Conversation context and tool schemas | `OPENAI_API_KEY` |
| Vercel | project environment variables | hosting | Runtime configuration | `Configured in deployment environment` |
| Business API | Bearer token | tool connector | Structured read/write operations | `BUSINESS_API_TOKEN` |

## Permission principles

- use the narrowest scope compatible with the operation
- separate development, staging and production credentials
- rotate long-lived secrets
- avoid embedding tokens in workflow exports or notebooks
- record external writes when the workflow can modify a business system

## Secret storage

Suitable options include GitHub environment secrets, AWS Secrets Manager, Azure Key Vault or the deployment platform's native secret store.

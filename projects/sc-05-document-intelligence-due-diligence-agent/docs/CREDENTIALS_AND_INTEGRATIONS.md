# Credentials and integrations

Credentials belong to the runtime environment, not source control.

| System | Authentication | Used by | Data exchanged | Environment configuration |
|---|---|---|---|---|
| S3-compatible storage | access key / secret | document store | Source files and extracted artefacts | `S3_ENDPOINT / S3_ACCESS_KEY / S3_SECRET_KEY` |
| Qdrant | API key where enabled | retrieval service | Embeddings and document chunks | `QDRANT_URL / QDRANT_API_KEY` |
| OpenAI | API key | extraction / synthesis | Selected chunks and structured prompts | `OPENAI_API_KEY` |
| PostgreSQL | service credentials | application | Document metadata, jobs and findings | `DATABASE_URL` |

## Permission principles

- use the narrowest scope compatible with the operation
- separate development, staging and production credentials
- rotate long-lived secrets
- avoid embedding tokens in workflow exports or notebooks
- record external writes when the workflow can modify a business system

## Secret storage

Suitable options include GitHub environment secrets, AWS Secrets Manager, Azure Key Vault or the deployment platform's native secret store.

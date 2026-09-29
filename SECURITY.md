# Security

This repository contains public implementations and representative data only.

- Never commit credentials, private keys or production connection strings.
- Use `.env.example` for variable names and safe placeholders.
- Keep write-capable integrations least-privilege.
- Use separate identities for development, staging and production.
- Treat model-provider, CRM, cloud and database credentials as runtime secrets.
- Do not publish client records or private endpoints.

Project-specific controls are documented under each project's `docs/SECURITY_AND_PERMISSIONS.md`.

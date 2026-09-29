# Technical decisions

The stack is not a list of logos. Each technology has to earn its place in the architecture.

## Key decisions

1. n8n is used for orchestration rather than as the place where domain logic is hidden.
2. Webhook adapters make Zapier and Make optional edges rather than hard dependencies.
3. Run state is persisted outside the workflow tool for auditability.

## Technology footprint

- **n8n**
- **Python**
- **FastAPI**
- **PostgreSQL**
- **Redis**
- **Webhooks**
- **Zapier Webhooks**
- **Make Webhooks**
- **Docker**

## Decision rule

If a simpler component can meet the same operational requirement with lower maintenance cost, it should be preferred. The public implementation keeps boundaries explicit so individual tools can be replaced without redesigning the whole project.

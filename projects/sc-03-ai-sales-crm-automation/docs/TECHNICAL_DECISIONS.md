# Technical decisions

The stack is not a list of logos. Each technology has to earn its place in the architecture.

## Key decisions

1. HubSpot remains the operational system of record while the application owns scoring and proposed actions.
2. n8n handles cross-system workflow steps; model logic stays outside the workflow canvas.
3. Outbound writes are gated so a generated message cannot silently mutate CRM state.

## Technology footprint

- **Python**
- **FastAPI**
- **PostgreSQL**
- **n8n**
- **HubSpot API**
- **Webhooks**
- **OpenAI**
- **Docker**
- **SQL**

## Decision rule

If a simpler component can meet the same operational requirement with lower maintenance cost, it should be preferred. The public implementation keeps boundaries explicit so individual tools can be replaced without redesigning the whole project.

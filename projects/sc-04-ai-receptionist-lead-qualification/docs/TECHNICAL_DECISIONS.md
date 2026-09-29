# Technical decisions

The stack is not a list of logos. Each technology has to earn its place in the architecture.

## Key decisions

1. Fastify keeps the webhook boundary small and explicit.
2. Twilio and Calendly are isolated behind provider-specific connectors.
3. Qualification fields are structured before routing so downstream systems do not depend on free-form text.

## Technology footprint

- **TypeScript**
- **Node.js**
- **Fastify**
- **Twilio**
- **Calendly**
- **OpenAI**
- **PostgreSQL**
- **Docker**
- **Webhooks**

## Decision rule

If a simpler component can meet the same operational requirement with lower maintenance cost, it should be preferred. The public implementation keeps boundaries explicit so individual tools can be replaced without redesigning the whole project.

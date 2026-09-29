# Architecture

## Objective

A conversational intake layer that qualifies enquiries, captures structured requirements and routes the next action.

## Logical flow

```text
Sources / request
      ↓
Input validation
      ↓
AI Receptionist & Lead Qualification
      ↓
Decision / processing layer
      ↓
External integrations
      ↓
Persisted output + monitoring
```

## Responsibilities

The implementation separates input handling, domain logic, integrations and persistence so each concern can be tested and changed independently.

## Technology choices

- **TypeScript** — used where it has a clear responsibility in the implementation.
- **Node.js** — used where it has a clear responsibility in the implementation.
- **Fastify** — used where it has a clear responsibility in the implementation.
- **Twilio** — used where it has a clear responsibility in the implementation.
- **Calendly** — used where it has a clear responsibility in the implementation.
- **OpenAI** — used where it has a clear responsibility in the implementation.
- **PostgreSQL** — used where it has a clear responsibility in the implementation.
- **Docker** — used where it has a clear responsibility in the implementation.
- **Webhooks** — used where it has a clear responsibility in the implementation.

## Integration boundaries

- **Twilio** — voice / messaging gateway; exchanges inbound message metadata and response text.
- **Calendly** — scheduling connector; exchanges availability and booking hand-off.
- **OpenAI** — conversation engine; exchanges conversation context and structured extraction.
- **PostgreSQL** — application; exchanges enquiries, qualification fields and routing state.

## Reliability

The technical layer includes deterministic local execution, example outputs, explicit failure logging and tests. Production deployments should add environment-specific monitoring, alerting and access controls.

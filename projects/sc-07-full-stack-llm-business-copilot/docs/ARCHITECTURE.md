# Architecture

## Objective

A full-stack web application that combines conversational analysis, structured tools and persistent business context.

## Logical flow

```text
Sources / request
      ↓
Input validation
      ↓
Full-Stack LLM Business Copilot
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

- **Next.js** — used where it has a clear responsibility in the implementation.
- **TypeScript** — used where it has a clear responsibility in the implementation.
- **React** — used where it has a clear responsibility in the implementation.
- **PostgreSQL** — used where it has a clear responsibility in the implementation.
- **Supabase** — used where it has a clear responsibility in the implementation.
- **OpenAI** — used where it has a clear responsibility in the implementation.
- **Vercel** — used where it has a clear responsibility in the implementation.
- **Zod** — used where it has a clear responsibility in the implementation.
- **Tailwind CSS** — used where it has a clear responsibility in the implementation.

## Integration boundaries

- **Supabase** — application data layer; exchanges users, conversations and tool results.
- **OpenAI** — LLM service; exchanges conversation context and tool schemas.
- **Vercel** — hosting; exchanges runtime configuration.
- **Business API** — tool connector; exchanges structured read/write operations.

## Reliability

The technical layer includes deterministic local execution, example outputs, explicit failure logging and tests. Production deployments should add environment-specific monitoring, alerting and access controls.

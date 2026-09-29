# Architecture

## Objective

An event-driven automation layer that combines deterministic workflows with AI steps where interpretation is actually useful.

## Logical flow

```text
Sources / request
      ↓
Input validation
      ↓
AI Workflow Automation Hub
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

- **n8n** — used where it has a clear responsibility in the implementation.
- **Python** — used where it has a clear responsibility in the implementation.
- **FastAPI** — used where it has a clear responsibility in the implementation.
- **PostgreSQL** — used where it has a clear responsibility in the implementation.
- **Redis** — used where it has a clear responsibility in the implementation.
- **Webhooks** — used where it has a clear responsibility in the implementation.
- **Zapier Webhooks** — used where it has a clear responsibility in the implementation.
- **Make Webhooks** — used where it has a clear responsibility in the implementation.
- **Docker** — used where it has a clear responsibility in the implementation.

## Integration boundaries

- **n8n** — primary workflow engine; exchanges workflow events and task payloads.
- **Zapier** — external workflow connector; exchanges event payloads.
- **Make** — external workflow connector; exchanges event payloads.
- **PostgreSQL** — state store; exchanges workflow runs, payload hashes and outcomes.

## Reliability

The technical layer includes deterministic local execution, example outputs, explicit failure logging and tests. Production deployments should add environment-specific monitoring, alerting and access controls.

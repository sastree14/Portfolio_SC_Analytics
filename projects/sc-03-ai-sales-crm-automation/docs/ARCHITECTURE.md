# Architecture

## Objective

A sales-operations system that scores inbound activity, prepares follow-ups and keeps CRM actions controlled.

## Logical flow

```text
Sources / request
      ↓
Input validation
      ↓
AI Sales & CRM Automation System
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

- **Python** — used where it has a clear responsibility in the implementation.
- **FastAPI** — used where it has a clear responsibility in the implementation.
- **PostgreSQL** — used where it has a clear responsibility in the implementation.
- **n8n** — used where it has a clear responsibility in the implementation.
- **HubSpot API** — used where it has a clear responsibility in the implementation.
- **Webhooks** — used where it has a clear responsibility in the implementation.
- **OpenAI** — used where it has a clear responsibility in the implementation.
- **Docker** — used where it has a clear responsibility in the implementation.
- **SQL** — used where it has a clear responsibility in the implementation.

## Integration boundaries

- **HubSpot** — CRM connector; exchanges contacts, companies, deals and activity updates.
- **n8n** — workflow layer; exchanges event payloads and approved automation steps.
- **OpenAI** — message drafting service; exchanges selected crm context and generated draft.
- **PostgreSQL** — application; exchanges lead scores, proposed actions and audit events.

## Reliability

The technical layer includes deterministic local execution, example outputs, explicit failure logging and tests. Production deployments should add environment-specific monitoring, alerting and access controls.

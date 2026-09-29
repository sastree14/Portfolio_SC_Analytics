# Architecture

## Objective

A controlled multi-agent system that separates planning, specialist work, review and execution.

## Logical flow

```text
Sources / request
      ↓
Input validation
      ↓
Multi-Agent Operations Orchestrator
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
- **LangGraph** — used where it has a clear responsibility in the implementation.
- **PostgreSQL** — used where it has a clear responsibility in the implementation.
- **Redis** — used where it has a clear responsibility in the implementation.
- **Docker** — used where it has a clear responsibility in the implementation.
- **OpenAI** — used where it has a clear responsibility in the implementation.
- **Anthropic** — used where it has a clear responsibility in the implementation.
- **Pydantic** — used where it has a clear responsibility in the implementation.

## Integration boundaries

- **OpenAI / Anthropic** — Planner and specialist agents; exchanges task context and structured responses.
- **PostgreSQL** — API + workers; exchanges workflow state, messages and audit events.
- **Redis** — worker queue; exchanges task delivery and transient coordination.
- **External action API** — executor agent; exchanges approved action payload and response.

## Reliability

The technical layer includes deterministic local execution, example outputs, explicit failure logging and tests. Production deployments should add environment-specific monitoring, alerting and access controls.

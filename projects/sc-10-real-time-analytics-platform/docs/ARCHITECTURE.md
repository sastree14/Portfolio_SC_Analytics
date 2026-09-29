# Architecture

## Objective

A streaming architecture for ingesting events, updating analytical state and exposing low-latency operational views.

## Logical flow

```text
Sources / request
      ↓
Input validation
      ↓
Real-Time Analytics & Monitoring Platform
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

- **Redpanda / Kafka** — used where it has a clear responsibility in the implementation.
- **ClickHouse** — used where it has a clear responsibility in the implementation.
- **Python** — used where it has a clear responsibility in the implementation.
- **FastAPI** — used where it has a clear responsibility in the implementation.
- **WebSockets** — used where it has a clear responsibility in the implementation.
- **Grafana** — used where it has a clear responsibility in the implementation.
- **Docker** — used where it has a clear responsibility in the implementation.
- **SQL** — used where it has a clear responsibility in the implementation.

## Integration boundaries

- **Redpanda / Kafka** — event bus; exchanges operational events.
- **ClickHouse** — analytical store; exchanges events and aggregates.
- **Grafana** — monitoring UI; exchanges queries and dashboard state.
- **WebSocket clients** — live consumers; exchanges aggregated live metrics.

## Reliability

The technical layer includes deterministic local execution, example outputs, explicit failure logging and tests. Production deployments should add environment-specific monitoring, alerting and access controls.

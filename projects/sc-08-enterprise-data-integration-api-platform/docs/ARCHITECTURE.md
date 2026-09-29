# Architecture

## Objective

A governed data-integration layer that moves operational data into analytical storage and exposes controlled downstream APIs.

## Logical flow

```text
Sources / request
      ↓
Input validation
      ↓
Enterprise Data Integration & API Platform
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
- **Apache Airflow** — used where it has a clear responsibility in the implementation.
- **PostgreSQL** — used where it has a clear responsibility in the implementation.
- **ClickHouse** — used where it has a clear responsibility in the implementation.
- **AWS S3** — used where it has a clear responsibility in the implementation.
- **Azure Blob Storage** — used where it has a clear responsibility in the implementation.
- **Docker** — used where it has a clear responsibility in the implementation.
- **SQL** — used where it has a clear responsibility in the implementation.

## Integration boundaries

- **PostgreSQL** — source connector; exchanges operational tables.
- **AWS S3** — object storage connector; exchanges extracted files and snapshots.
- **Azure Blob Storage** — object storage connector; exchanges extracted files and snapshots.
- **ClickHouse** — analytical store; exchanges curated analytical tables.
- **Airflow** — orchestration; exchanges task schedules and connection references.

## Reliability

The technical layer includes deterministic local execution, example outputs, explicit failure logging and tests. Production deployments should add environment-specific monitoring, alerting and access controls.

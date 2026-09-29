# Architecture

## Objective

A reproducible analytics-engineering pipeline with tests, lineage-friendly transformations and explicit data-quality gates.

## Logical flow

```text
Sources / request
      ↓
Input validation
      ↓
ETL / ELT & Data Quality Pipeline
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

- **dbt** — used where it has a clear responsibility in the implementation.
- **DuckDB** — used where it has a clear responsibility in the implementation.
- **Python** — used where it has a clear responsibility in the implementation.
- **Pandera** — used where it has a clear responsibility in the implementation.
- **Parquet** — used where it has a clear responsibility in the implementation.
- **Apache Airflow** — used where it has a clear responsibility in the implementation.
- **SQL** — used where it has a clear responsibility in the implementation.
- **Docker** — used where it has a clear responsibility in the implementation.
- **GitHub Actions** — used where it has a clear responsibility in the implementation.

## Integration boundaries

- **DuckDB** — warehouse engine; exchanges staging and mart tables.
- **Parquet** — exchange format; exchanges raw and curated datasets.
- **Airflow** — orchestration; exchanges scheduled dbt and validation tasks.
- **GitHub Actions** — CI; exchanges tests and build status.

## Reliability

The technical layer includes deterministic local execution, example outputs, explicit failure logging and tests. Production deployments should add environment-specific monitoring, alerting and access controls.

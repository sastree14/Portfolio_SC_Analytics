# SC-09 · ETL / ELT & Data Quality Pipeline

**A reproducible analytics-engineering pipeline with tests, lineage-friendly transformations and explicit data-quality gates.**

Designed for **Analytics teams · reporting stacks · ML feature preparation · finance and operations data**.

## What changes for the business

- Catch broken data before it reaches reports or models
- Make transformations reviewable in SQL
- Separate raw, staging and business-ready layers
- Create repeatable build and test steps for analytics

[Business impact →](docs/BUSINESS_IMPACT.md)

## Example use case

Daily commercial data lands as Parquet, passes schema and rule checks, builds staging models and then produces finance-ready revenue and margin marts.

## Technology at a glance

**dbt · DuckDB · Python · Pandera · Parquet · Apache Airflow · SQL · Docker · GitHub Actions**

The technology is visible here for fast technical screening. The business explanation does not depend on understanding the stack.

## How the system works

```text
Business event / request
        ↓
Validation + context
        ↓
Core decision / orchestration layer
        ↓
Controlled integration boundary
        ↓
Result, action or analytical output
        ↓
Audit / monitoring
```

For implementation details, tests, SQL and infrastructure, use the [technical entry point](technical/README.md).

## Evidence

- [Business impact](docs/BUSINESS_IMPACT.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Credentials and integrations](docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Environments](docs/ENVIRONMENTS.md)
- [Limitations](docs/LIMITATIONS.md)
- [Example input](examples/inputs/example.json)
- [Example output](examples/outputs/result.json)
- [Example execution log](examples/logs/example.log)
- [Generated analytical visual](examples/visuals/result.svg)
- [Technical implementation](technical/README.md)

## Run locally

```bash
cd technical
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/main.py
pytest -q
```

The included example is deterministic and does not require external credentials. Real integrations are activated through environment configuration.

## Credentials

No credentials are committed. Integration boundaries and expected environment variables are documented explicitly.

[Credentials and integrations →](docs/CREDENTIALS_AND_INTEGRATIONS.md)

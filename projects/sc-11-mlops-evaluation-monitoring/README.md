# SC-11 · ML / AI Evaluation & Monitoring Platform

**A production-oriented layer for model evaluation, version tracking, drift checks and release gates.**

Designed for **ML teams · AI product teams · regulated analytics · production model operations**.

## Business impact

- Make model changes reviewable before release
- Track model versions, datasets and evaluation results together
- Detect data or prediction drift before it becomes a business issue
- Separate experimentation from production release decisions

[Business impact in detail →](docs/BUSINESS_IMPACT.md)

## Example use case

A challenger model is trained on a new dataset. The platform compares it with the current model, checks data drift and only marks it releasable when agreed thresholds pass.

## Technology at a glance

**Python · MLflow · Evidently · FastAPI · PostgreSQL · Docker · GitHub Actions · Prometheus**

## What a reviewer can inspect

- [Architecture](docs/ARCHITECTURE.md)
- [Credentials and integrations](docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Environments](docs/ENVIRONMENTS.md)
- [Limitations](docs/LIMITATIONS.md)
- [Example output](examples/outputs/result.json)
- [Execution log](examples/logs/example.log)
- [Generated analytical visual](examples/visuals/result.svg)
- [Technical implementation](technical/README.md)

## Run locally

See [technical/README.md](technical/README.md) for the project-specific execution path.

## Technology and business are separated deliberately

A non-technical reviewer can understand the decision and impact from this page. A technical reviewer can enter the implementation, SQL, model logic, tests and environment configuration directly.

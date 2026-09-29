# SC-14 · Power BI Executive Decision System

**A semantic-model-driven executive reporting system for revenue, margin, pipeline and operating performance.**

Designed for **Management teams · finance · sales · operations · executive reporting**.

## Business impact

- Create one consistent KPI definition layer across teams
- Move from static reporting to drillable management questions
- Connect commercial and financial performance in one model
- Make period, segment and product comparisons repeatable

[Business impact in detail →](docs/BUSINESS_IMPACT.md)

## Example use case

An executive opens one report to compare revenue, margin and pipeline against plan, then drills from company level into segment, product and owner.

## Technology at a glance

**Power BI · DAX · Power Query · SQL · Star Schema · PostgreSQL · Excel**

## What a reviewer can inspect

- [Architecture](docs/ARCHITECTURE.md)
- [Credentials and integrations](docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Environments](docs/ENVIRONMENTS.md)
- [Limitations](docs/LIMITATIONS.md)
- [Example output](examples/outputs/result.json)
- [Execution log](examples/logs/example.log)
- [Technical implementation](technical/README.md)

## Run locally

See [technical/README.md](technical/README.md) for the project-specific execution path.

## Technology and business are separated deliberately

A non-technical reviewer can understand the decision and impact from this page. A technical reviewer can enter the implementation, SQL, model logic, tests and environment configuration directly.

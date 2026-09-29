# SC-15 · Tableau Commercial Analytics & Drill-Down

**A Tableau-oriented commercial analytics system focused on interactive exploration, cohorts and drill-down behaviour.**

Designed for **Sales analytics · customer analytics · commercial leadership · account management**.

## Business impact

- Let users explore performance without requesting new static reports
- Make cohort and segment differences visible
- Connect top-level KPIs to the underlying customer or account detail
- Support fast exploratory analysis for commercial teams

[Business impact in detail →](docs/BUSINESS_IMPACT.md)

## Example use case

A commercial manager filters to one segment, compares cohort performance, drills into underperforming accounts and identifies where conversion is leaking.

## Technology at a glance

**Tableau · Tableau Calculated Fields · SQL · PostgreSQL · CSV · LOD Expressions**

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

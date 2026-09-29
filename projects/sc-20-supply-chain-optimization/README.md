# SC-20 · Supply Chain & Marketplace Optimization

**A constrained optimization system for inventory allocation, replenishment and service-level trade-offs.**

Designed for **Supply chain · retail · marketplaces · distribution · operations planning**.

## Business impact

- Allocate limited inventory where it creates the most value
- Respect capacity, stock and service constraints explicitly
- Compare optimized decisions against current or heuristic policies
- Turn forecasts into operational actions

[Business impact in detail →](docs/BUSINESS_IMPACT.md)

## Example use case

Available inventory must be allocated across locations with different demand, margin and service targets. The optimizer produces the highest-value feasible allocation and reports the trade-offs.

## Technology at a glance

**Python · OR-Tools · Pandas · NumPy · FastAPI · PostgreSQL · Plotly · Docker**

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

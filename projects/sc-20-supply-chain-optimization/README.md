# SC-20 · Supply Chain & Marketplace Optimization

**A constrained optimization system for inventory allocation, replenishment and service-level trade-offs.**

**Designed for:** Supply chain · retail · marketplaces · distribution

## Why this project matters

- Allocate scarce stock where it creates most value
- Respect service and capacity constraints
- Compare optimized decisions with heuristics
- Turn forecasts into operational actions

A business reviewer can stay on this page. A technical reviewer can move directly to the [technical implementation](technical/README.md).

## Example operating flow

```text
Demand + stock
    ↓\n    Constraints
        ↓\n        Objective function
            ↓\n            Solver
                ↓\n                Recommended allocation
                    ↓\n                    Approval
                        ↓\n                        ERP hand-off
```

## Technology at a glance

**Python · OR-Tools · Pandas · NumPy · FastAPI · PostgreSQL · Plotly · Docker**

The stack is shown early because technical fit matters. The project is still explained in business terms first.

## What is included

- [Business impact and KPIs](docs/BUSINESS_IMPACT.md)
- [Example results and how to read them](docs/RESULTS.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Technical decisions](docs/TECHNICAL_DECISIONS.md)
- [Data and public sample structure](docs/DATA.md)
- [Security and permissions](docs/SECURITY_AND_PERMISSIONS.md)
- [Credentials and integrations](docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Environments](docs/ENVIRONMENTS.md)
- [Limitations](docs/LIMITATIONS.md)
- [Example inputs, outputs and logs](examples/README.md)
- [Technical implementation, SQL and tests](technical/README.md)

## What the example data represents

Representative demand, stock, margin, service targets, capacity constraints and optimized allocation decisions.

The repository does not contain client credentials or confidential records.

## Local review

The public implementation is designed so that the core example can be inspected locally without production credentials. Tool-specific connectors are configured through environment variables and are documented separately.

[Open the technical implementation →](technical/README.md)

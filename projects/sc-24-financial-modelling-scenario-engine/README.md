# SC-24 · Financial Modelling & Scenario Engine

**A driver-based financial model linking revenue, margin, operating costs and cash flow to explicit assumptions.**

**Designed for:** CFO teams · startups · investment analysis · business planning

## Why this project matters

- Make assumptions editable and traceable
- Connect operational drivers to P&L and cash flow
- Compare base, upside and downside cases
- Identify drivers of runway and profitability

A business reviewer can stay on this page. A technical reviewer can move directly to the [technical implementation](technical/README.md).

## Example operating flow

```text
Historical actuals
    ↓\n    Assumptions
        ↓\n        Revenue drivers
            ↓\n            Cost model
                ↓\n                P&L
                    ↓\n                    Cash flow
                        ↓\n                        Scenario comparison
```

## Technology at a glance

**Python · Pandas · NumPy · OpenPyXL · Plotly · FastAPI · PostgreSQL · Excel**

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

Representative monthly actuals, operating assumptions, scenario drivers, projected statements and Excel exports.

The repository does not contain client credentials or confidential records.

## Local review

The public implementation is designed so that the core example can be inspected locally without production credentials. Tool-specific connectors are configured through environment variables and are documented separately.

[Open the technical implementation →](technical/README.md)

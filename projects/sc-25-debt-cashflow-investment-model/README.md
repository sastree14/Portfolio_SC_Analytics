# SC-25 · Debt, Cash Flow & Investment Model

**An integrated debt and investment model for repayment schedules, covenant headroom, returns and downside analysis.**

**Designed for:** Infrastructure · real estate · corporate finance · project finance

## Why this project matters

- Connect financing to project cash flows
- Measure covenant headroom
- Separate operating and financing effects
- Calculate returns consistently

A business reviewer can stay on this page. A technical reviewer can move directly to the [technical implementation](technical/README.md).

## Example operating flow

```text
Investment assumptions
    ↓\n    Debt terms
        ↓\n        Drawdown / amortization
            ↓\n            Operating cash flow
                ↓\n                Debt service
                    ↓\n                    Covenants
                        ↓\n                        IRR / NPV
```

## Technology at a glance

**Python · Pandas · NumPy · OpenPyXL · Plotly · XIRR · PostgreSQL · Excel**

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

Representative debt terms, drawdowns, repayment schedules, operating cash flow and investor distributions.

The repository does not contain client credentials or confidential records.

## Local review

The public implementation is designed so that the core example can be inspected locally without production credentials. Tool-specific connectors are configured through environment variables and are documented separately.

[Open the technical implementation →](technical/README.md)

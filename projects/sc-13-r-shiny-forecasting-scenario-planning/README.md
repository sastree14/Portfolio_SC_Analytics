# SC-13 · R Shiny Forecasting & Scenario Planning Application

**An interactive R application for decomposition, forecasting and business what-if scenarios.**

**Designed for:** Finance · planning · sales operations · R analytics teams

## Why this project matters

- Inspect trend and seasonality interactively
- Compare statistical forecasts without editing code
- Turn assumptions into scenario outputs
- Keep analytical logic reproducible in R

A business reviewer can stay on this page. A technical reviewer can move directly to the [technical implementation](technical/README.md).

## Example operating flow

```text
Historical series
    ↓\n    R transformation
        ↓\n        Forecast model
            ↓\n            Scenario assumptions
                ↓\n                Shiny reactive layer
                    ↓\n                    ggplot output
                        ↓\n                        Decision
```

## Technology at a glance

**R · Shiny · forecast · fable · ggplot2 · dplyr · DBI · PostgreSQL**

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

Representative time series, fitted statistical models, forecast intervals, scenario inputs and Shiny reactive outputs.

The repository does not contain client credentials or confidential records.

## Local review

The public implementation is designed so that the core example can be inspected locally without production credentials. Tool-specific connectors are configured through environment variables and are documented separately.

[Open the technical implementation →](technical/README.md)

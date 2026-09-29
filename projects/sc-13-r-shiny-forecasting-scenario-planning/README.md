# SC-13 · R Shiny Forecasting & Scenario Planning Application

**An interactive R application for time-series decomposition, forecasting and business what-if scenarios.**

Designed for **Finance · planning · sales operations · analysts who work in R**.

## Business impact

- Let users inspect trend, seasonality and uncertainty interactively
- Compare statistical forecasting methods without editing code
- Translate forecast assumptions into scenario outputs
- Keep analytical logic reproducible in R

[Business impact in detail →](docs/BUSINESS_IMPACT.md)

## Example use case

A planning team changes expected growth, promotional uplift and cost assumptions in the Shiny application and immediately sees the forecast and scenario effect.

## Technology at a glance

**R · Shiny · forecast · fable · ggplot2 · dplyr · DBI · PostgreSQL**

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

# Architecture

## Objective

An interactive R application for time-series decomposition, forecasting and business what-if scenarios.

```text
Source data / user input
          ↓
Validation and feature layer
          ↓
R Shiny Forecasting & Scenario Planning Application
          ↓
Decision / analytical output
          ↓
Integration or user interface
          ↓
Monitoring and review
```

## Technology responsibilities

- **R** — part of the implemented analytical or serving path.
- **Shiny** — part of the implemented analytical or serving path.
- **forecast** — part of the implemented analytical or serving path.
- **fable** — part of the implemented analytical or serving path.
- **ggplot2** — part of the implemented analytical or serving path.
- **dplyr** — part of the implemented analytical or serving path.
- **DBI** — part of the implemented analytical or serving path.
- **PostgreSQL** — part of the implemented analytical or serving path.

## Integration boundaries

- **PostgreSQL** — data access layer; exchanges historical measures and scenario inputs.
- **Shiny Server / Posit Connect** — application runtime; exchanges r application bundle.
- **CSV / Parquet** — public input; exchanges historical time series.

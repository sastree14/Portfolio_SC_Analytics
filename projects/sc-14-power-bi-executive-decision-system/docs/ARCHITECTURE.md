# Architecture

## Objective

A semantic-model-driven executive reporting system for revenue, margin, pipeline and operating performance.

```text
Source data / user input
          ↓
Validation and feature layer
          ↓
Power BI Executive Decision System
          ↓
Decision / analytical output
          ↓
Integration or user interface
          ↓
Monitoring and review
```

## Technology responsibilities

- **Power BI** — part of the implemented analytical or serving path.
- **DAX** — part of the implemented analytical or serving path.
- **Power Query** — part of the implemented analytical or serving path.
- **SQL** — part of the implemented analytical or serving path.
- **Star Schema** — part of the implemented analytical or serving path.
- **PostgreSQL** — part of the implemented analytical or serving path.
- **Excel** — part of the implemented analytical or serving path.

## Integration boundaries

- **PostgreSQL** — semantic-model source; exchanges fact and dimension tables.
- **Excel / CSV** — planning inputs; exchanges targets and mapping tables.
- **Power BI Service** — publishing and refresh; exchanges dataset and report artefacts.

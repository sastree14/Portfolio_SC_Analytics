# Architecture

## Objective

Connect demand forecasting evidence to inventory and purchasing decisions in a Power BI planning interface.

```text
Orders / demand / inventory
            ↓
SQL + Power Query preparation
            ↓
Star-schema semantic model
            ↓
DAX forecast and inventory measures
            ↓
Power BI planning interface
            ↓
Purchasing / inventory decision
```

## Technology responsibilities

- **Power BI** — interactive decision interface and drill-down.
- **DAX** — forecast, bias, coverage and service measures.
- **Power Query** — source shaping and controlled transformations.
- **SQL** — stable analytical grain before BI consumption.
- **Star Schema** — shared semantic layer across visuals.
- **PostgreSQL / Excel** — representative operational and planning inputs.

# Architecture

## Objective

Create a Power BI operating interface for service, order status, delivery lead time and exception management.

```text
Orders / commitments / deliveries
              ↓
SQL + Power Query preparation
              ↓
Service / lead-time semantic model
              ↓
DAX operational measures
              ↓
Power BI control tower
              ↓
Exception review / customer action
```

## Technology responsibilities

- **Power BI** — service-level monitoring and drill-down.
- **DAX** — service, lead-time and exception measures.
- **Power Query** — source shaping and normalization.
- **SQL** — stable order-event and delivery grain.
- **Star Schema** — shared customer, date, destination and Incoterm dimensions.

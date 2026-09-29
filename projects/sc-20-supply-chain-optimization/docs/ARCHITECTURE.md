# Architecture

## Objective

A constrained optimization system for inventory allocation, replenishment and service-level trade-offs.

```text
Source data / user input
          ↓
Validation and feature layer
          ↓
Supply Chain & Marketplace Optimization
          ↓
Decision / analytical output
          ↓
Integration or user interface
          ↓
Monitoring and review
```

## Technology responsibilities

- **Python** — part of the implemented analytical or serving path.
- **OR-Tools** — part of the implemented analytical or serving path.
- **Pandas** — part of the implemented analytical or serving path.
- **NumPy** — part of the implemented analytical or serving path.
- **FastAPI** — part of the implemented analytical or serving path.
- **PostgreSQL** — part of the implemented analytical or serving path.
- **Plotly** — part of the implemented analytical or serving path.
- **Docker** — part of the implemented analytical or serving path.

## Integration boundaries

- **PostgreSQL** — planning source; exchanges demand, inventory, cost and capacity tables.
- **FastAPI** — optimization API; exchanges scenario assumptions and recommended plan.
- **ERP export/import** — operational hand-off; exchanges inventory positions and approved recommendations.

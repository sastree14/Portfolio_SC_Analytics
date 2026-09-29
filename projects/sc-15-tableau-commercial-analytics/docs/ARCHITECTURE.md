# Architecture

## Objective

A Tableau-oriented commercial analytics system focused on interactive exploration, cohorts and drill-down behaviour.

```text
Source data / user input
          ↓
Validation and feature layer
          ↓
Tableau Commercial Analytics & Drill-Down
          ↓
Decision / analytical output
          ↓
Integration or user interface
          ↓
Monitoring and review
```

## Technology responsibilities

- **Tableau** — part of the implemented analytical or serving path.
- **Tableau Calculated Fields** — part of the implemented analytical or serving path.
- **SQL** — part of the implemented analytical or serving path.
- **PostgreSQL** — part of the implemented analytical or serving path.
- **CSV** — part of the implemented analytical or serving path.
- **LOD Expressions** — part of the implemented analytical or serving path.

## Integration boundaries

- **PostgreSQL** — primary data source; exchanges commercial fact and dimension tables.
- **Tableau Server / Cloud** — publishing layer; exchanges workbook and datasource refresh.
- **CSV** — reference mappings; exchanges targets and segment mappings.

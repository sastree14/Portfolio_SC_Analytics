# SC-15 · Tableau Commercial Analytics & Drill-Down

**A Tableau-oriented commercial analytics system focused on interactive exploration, cohorts and drill-down behaviour.**

**Designed for:** Sales analytics · customer analytics · commercial leadership

## Business impact

- Let users explore performance without requesting new static reports
- Make cohort and segment differences visible
- Connect top-level KPIs to account-level detail
- Support fast exploratory commercial analysis

## Technology at a glance

**Tableau · Tableau Calculated Fields · SQL · PostgreSQL · CSV · LOD Expressions**

## What is complete

- business context and KPI definition
- data model and source preparation
- SQL assets
- credentials and integration documentation
- environment guidance
- tests for the public datasource
- tool-specific calculations and model specification
- local data preparation scripts

## Native visual layer

The Tableau screenshot set is the only intentionally pending layer. It will be added from a native-tool visual reference rather than fabricated.

## Visual evidence

![SC-15 project visual](examples/visuals/result.svg)

This visual documents the analytical/model structure. The native BI screenshot layer remains pending until the real tool reference is supplied.

## Main technical execution

**Start with [`technical/run_project.py`](technical/run_project.py).** This is the principal end-to-end code path for the public implementation.

## Technical review

- [Architecture](docs/ARCHITECTURE.md)
- [Results and KPI interpretation](docs/RESULTS.md)
- [Data](docs/DATA.md)
- [Technical decisions](docs/TECHNICAL_DECISIONS.md)
- [Security and permissions](docs/SECURITY_AND_PERMISSIONS.md)
- [Credentials and integrations](docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Technical implementation](technical/README.md)

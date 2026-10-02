# SC-14 · Power BI Executive Decision System

**A semantic-model-driven executive reporting system for revenue, margin, pipeline and operating performance.**

**Designed for:** Management · finance · sales · operations

## Business impact

- Create one KPI definition layer across teams
- Move from static reporting to drillable management questions
- Connect commercial and financial performance in one model
- Make period and segment comparisons repeatable

## Technology at a glance

**Power BI · DAX · Power Query · SQL · Star Schema · PostgreSQL · Excel**

## What is complete

- business context and KPI definition
- data model and source preparation
- SQL assets
- credentials and integration documentation
- environment guidance
- tests for the public datasource
- tool-specific calculations and model specification
- local data preparation scripts
- representative Power BI interface derived from genuine design references

## Representative Power BI interface

![SC-14 representative Power BI interface](examples/visuals/result.svg)

The published visual is a **sanitized reconstruction based on genuine Power BI design references supplied privately**. It demonstrates the intended executive information architecture while using public-safe illustrative data. The private PBIX source files and client data are not published.

## Main technical execution

**Start with [`technical/run_project.py`](technical/run_project.py).**

## Technical review

- [Architecture](docs/ARCHITECTURE.md)
- [Results and KPI interpretation](docs/RESULTS.md)
- [Data](docs/DATA.md)
- [Technical decisions](docs/TECHNICAL_DECISIONS.md)
- [Security and permissions](docs/SECURITY_AND_PERMISSIONS.md)
- [Credentials and integrations](docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Technical implementation](technical/README.md)

# SC-31 · Power BI Forecast & Inventory Planning Dashboard

**A Power BI planning interface that connects multi-horizon forecast accuracy with inventory coverage, service level and replenishment decisions.**

**Designed for:** Supply chain · demand planning · purchasing · operations management

## Business problem

Forecast accuracy is often reported as one aggregate number while purchasing decisions are made at very different horizons. That can hide where uncertainty becomes operationally expensive.

This public implementation structures the decision around **1, 3, 6 and 9 month horizons**, then connects forecast quality to stock coverage, service level and replenishment action.

## Business impact

- compare forecast quality by planning horizon
- connect demand signal to stock and service implications
- expose bias rather than relying on one accuracy score
- give planners one repeatable drill-down for product, market and scenario

## Technology at a glance

**Power BI · DAX · Power Query · SQL · Star Schema · PostgreSQL · Excel**

## Representative Power BI interface

![SC-31 representative Power BI interface](examples/visuals/result.svg)

The published interface is a **sanitized reconstruction based on genuine Power BI design references supplied privately**. It uses illustrative public-safe data and does not reproduce confidential client data or a source PBIX screenshot.

## Main technical execution

**Start with [`technical/run_project.py`](technical/run_project.py).**

## Technical review

- [Architecture](docs/ARCHITECTURE.md)
- [Business impact](docs/BUSINESS_IMPACT.md)
- [Results](docs/RESULTS.md)
- [Data](docs/DATA.md)
- [Technical decisions](docs/TECHNICAL_DECISIONS.md)
- [Security and permissions](docs/SECURITY_AND_PERMISSIONS.md)
- [Credentials and integrations](docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Environments](docs/ENVIRONMENTS.md)
- [Limitations](docs/LIMITATIONS.md)
- [Technical implementation](technical/README.md)

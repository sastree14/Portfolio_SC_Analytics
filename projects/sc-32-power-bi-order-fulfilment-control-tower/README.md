# SC-32 · Power BI Order Fulfilment & Service Control Tower

**A Power BI operations control tower for service level, delivery lead times, order status and exception management.**

**Designed for:** Operations management · customer service · logistics · commercial teams

## Business problem

Service reporting becomes difficult when delivery performance, commitments, destinations and order exceptions live in separate views.

This public implementation brings those decisions together: **service level, on-time delivery, lead time, backlog and exceptions** can be reviewed from executive level down to customer, destination and Incoterm.

## Business impact

- one operating view for service and delivery performance
- faster identification of late or blocked orders
- repeatable customer, destination and Incoterm drill-down
- clearer separation between service KPI and operational exception

## Technology at a glance

**Power BI · DAX · Power Query · SQL · Star Schema · PostgreSQL · Excel**

## Representative Power BI interface

![SC-32 representative Power BI interface](examples/visuals/result.svg)

The published interface is a **sanitized reconstruction based on genuine Power BI service and operations references supplied privately**. No private PBIX file or client data is published.

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

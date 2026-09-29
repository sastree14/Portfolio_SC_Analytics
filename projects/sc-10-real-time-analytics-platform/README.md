# SC-10 · Real-Time Analytics & Monitoring Platform

**A streaming architecture for ingesting events, updating analytical state and exposing low-latency operational views.**

**Designed for:** Operations monitoring · marketplaces · telemetry · live decision systems

## Why this project matters

- Reduce event-to-insight latency
- Separate ingestion from analytical querying
- Support live dashboards and alerts
- Retain history for replay and investigation

A business reviewer can stay on this page. A technical reviewer can move directly to the [technical implementation](technical/README.md).

## Example operating flow

```text
Producer
    ↓\n    Kafka / Redpanda
        ↓\n        Consumer
            ↓\n            ClickHouse
                ↓\n                FastAPI / WebSocket
                    ↓\n                    Grafana
                        ↓\n                        Alerting
```

## Technology at a glance

**Redpanda / Kafka · ClickHouse · Python · FastAPI · WebSockets · Grafana · Docker · SQL**

The stack is shown early because technical fit matters. The project is still explained in business terms first.

## What is included

- [Business impact and KPIs](docs/BUSINESS_IMPACT.md)
- [Example results and how to read them](docs/RESULTS.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Technical decisions](docs/TECHNICAL_DECISIONS.md)
- [Data and public sample structure](docs/DATA.md)
- [Security and permissions](docs/SECURITY_AND_PERMISSIONS.md)
- [Credentials and integrations](docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Environments](docs/ENVIRONMENTS.md)
- [Limitations](docs/LIMITATIONS.md)
- [Example inputs, outputs and logs](examples/README.md)
- [Technical implementation, SQL and tests](technical/README.md)

## What the example data represents

Representative event messages, stream-consumer outputs, ClickHouse schema, live API payloads and monitoring configuration.

The repository does not contain client credentials or confidential records.

## Local review

The public implementation is designed so that the core example can be inspected locally without production credentials. Tool-specific connectors are configured through environment variables and are documented separately.

[Open the technical implementation →](technical/README.md)

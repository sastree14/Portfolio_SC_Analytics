# SC-10 · Real-Time Analytics & Monitoring Platform

**A streaming architecture for ingesting events, updating analytical state and exposing low-latency operational views.**

Designed for **Operations monitoring · marketplaces · trading-like event flows · product telemetry · live decision systems**.

## What changes for the business

- Reduce the delay between an operational event and analytical visibility
- Separate event ingestion from analytical querying
- Provide a scalable path for dashboards and downstream alerts
- Retain event history for replay and investigation

[Business impact →](docs/BUSINESS_IMPACT.md)

## Example use case

Order events are published to the event bus, consumed into ClickHouse, aggregated continuously and exposed through an API/WebSocket layer for live operational monitoring.

## Technology at a glance

**Redpanda / Kafka · ClickHouse · Python · FastAPI · WebSockets · Grafana · Docker · SQL**

The technology is visible here for fast technical screening. The business explanation does not depend on understanding the stack.

## How the system works

```text
Business event / request
        ↓
Validation + context
        ↓
Core decision / orchestration layer
        ↓
Controlled integration boundary
        ↓
Result, action or analytical output
        ↓
Audit / monitoring
```

For implementation details, tests, SQL and infrastructure, use the [technical entry point](technical/README.md).

## Evidence

- [Business impact](docs/BUSINESS_IMPACT.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Credentials and integrations](docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Environments](docs/ENVIRONMENTS.md)
- [Limitations](docs/LIMITATIONS.md)
- [Example input](examples/inputs/example.json)
- [Example output](examples/outputs/result.json)
- [Example execution log](examples/logs/example.log)
- [Generated analytical visual](examples/visuals/result.svg)
- [Technical implementation](technical/README.md)

## Run locally

```bash
cd technical
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/main.py
pytest -q
```

The included example is deterministic and does not require external credentials. Real integrations are activated through environment configuration.

## Credentials

No credentials are committed. Integration boundaries and expected environment variables are documented explicitly.

[Credentials and integrations →](docs/CREDENTIALS_AND_INTEGRATIONS.md)

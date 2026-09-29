# SC-27 · Quantitative Trading & Market Microstructure System

**A research stack for order-book events, microstructure signals, backtesting and strategy evaluation.**

**Designed for:** Quant research · market data engineering · execution research

## Why this project matters

- Separate raw market events from signals
- Replay history reproducibly
- Inspect imbalance and execution conditions
- Evaluate strategies with costs

A business reviewer can stay on this page. A technical reviewer can move directly to the [technical implementation](technical/README.md).

## Example operating flow

```text
WebSocket feed
    ↓\n    Event normalization
        ↓\n        ClickHouse
            ↓\n            Live Redis state
                ↓\n                Signal engine
                    ↓\n                    Backtest
                        ↓\n                        Research UI
```

## Technology at a glance

**Python · TypeScript · WebSockets · ClickHouse · Redis · Pandas · NumPy · Plotly · Docker**

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

Representative L1/L2-style events, normalized trades/quotes, microstructure features, backtest results and live-state payloads.

The repository does not contain client credentials or confidential records.

## Local review

The public implementation is designed so that the core example can be inspected locally without production credentials. Tool-specific connectors are configured through environment variables and are documented separately.

[Open the technical implementation →](technical/README.md)

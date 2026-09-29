# SC-27 · Quantitative Trading & Market Microstructure System

**A research and monitoring stack for order-book events, backtesting, market microstructure signals and strategy evaluation.**

Designed for **Quant research · trading analytics · market data engineering · execution research**.

## Business impact

- Separate raw market events from derived trading signals
- Backtest strategy logic against reproducible historical data
- Inspect order-book imbalance, delta and execution conditions
- Keep research, signal generation and visualization in one traceable stack

## Example use case

The system consumes L1/L2 events, calculates imbalance and absorption-style features, stores historical events for replay and evaluates a rules-based strategy with transaction costs.

## Technology at a glance

**Python · TypeScript · WebSockets · ClickHouse · Redis · Pandas · NumPy · Plotly · Docker**

## Evidence

- [Business impact](docs/BUSINESS_IMPACT.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Credentials and integrations](docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Environments](docs/ENVIRONMENTS.md)
- [Limitations](docs/LIMITATIONS.md)
- [Example output](examples/outputs/result.json)
- [Execution log](examples/logs/example.log)
- [Generated analytical visual](examples/visuals/result.svg)
- [Technical implementation](technical/README.md)

## Run locally

The technical README contains the exact environment and execution path.

The public example is deterministic and does not require production credentials.

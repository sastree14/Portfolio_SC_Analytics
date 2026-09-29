# Business impact

1. Separate raw market events from derived trading signals
2. Backtest strategy logic against reproducible historical data
3. Inspect order-book imbalance, delta and execution conditions
4. Keep research, signal generation and visualization in one traceable stack

## Example

The system consumes L1/L2 events, calculates imbalance and absorption-style features, stores historical events for replay and evaluates a rules-based strategy with transaction costs.

## KPIs

- fill-adjusted PnL
- max drawdown
- hit rate
- latency
- signal turnover

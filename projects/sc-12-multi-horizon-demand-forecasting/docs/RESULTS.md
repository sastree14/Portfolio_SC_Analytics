# Results

## What the public example demonstrates

The example output for **SC-12 · Multi-Horizon Demand Forecasting & Inventory Planning** is generated from representative public inputs and demonstrates the end-to-end decision path of the project.

It is useful for checking:

- WAPE
- MAE
- forecast bias
- service level
- inventory coverage

## Public example metrics

The deterministic public backtest currently yields:

| Metric | Value |
| --- | ---: |
| WAPE | 6.45% |
| MAE | 7.39 units |
| Forecast bias | -6.45% |
| Backtest observations | 6 |
| Planning horizons | 1, 3, 6 and 9 months |

These values belong to the representative public implementation. They are reproducible example metrics, not production client KPIs.

## How to read the evidence

- `examples/inputs/` shows the input shape used by the public run.
- `examples/outputs/` shows the resulting structured output.
- `examples/logs/` shows the execution sequence.
- `examples/visuals/` contains the project-level analytical visual when applicable.

The values in the public example are not presented as a production client KPI. The evidence is intended to make the implementation inspectable and reproducible.

## Business interpretation

- Measure forecast quality by horizon
- Expose forecast bias as well as absolute error
- Translate predictions into planning decisions
- Benchmark complex models against simple baselines

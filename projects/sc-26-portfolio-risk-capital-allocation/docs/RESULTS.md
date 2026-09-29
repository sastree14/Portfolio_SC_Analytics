# Results

## What the public example demonstrates

The example output for **SC-26 · Portfolio Risk & Capital Allocation Engine** is generated from representative public inputs and demonstrates the end-to-end decision path of the project.

It is useful for checking:

- expected return
- volatility
- VaR
- CVaR
- Sharpe ratio

## How to read the evidence

- `examples/inputs/` shows the input shape used by the public run.
- `examples/outputs/` shows the resulting structured output.
- `examples/logs/` shows the execution sequence.
- `examples/visuals/` contains the project-level analytical visual when applicable.

The values in the public example are not presented as a production client KPI. The evidence is intended to make the implementation inspectable and reproducible.

## Business interpretation

- Measure portfolio-level risk
- Compare constrained allocations
- Stress adverse scenarios
- Translate risk appetite into allocation limits

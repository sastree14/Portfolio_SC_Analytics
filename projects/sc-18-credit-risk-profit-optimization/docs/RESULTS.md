# Results

## What the public example demonstrates

The example output for **SC-18 · Credit Risk & Profit Optimization Engine** is generated from representative public inputs and demonstrates the end-to-end decision path of the project.

It is useful for checking:

- ROC AUC
- PR AUC
- expected loss
- approval rate
- risk-adjusted contribution

## How to read the evidence

- `examples/inputs/` shows the input shape used by the public run.
- `examples/outputs/` shows the resulting structured output.
- `examples/logs/` shows the execution sequence.
- `examples/visuals/` contains the project-level analytical visual when applicable.

The values in the public example are not presented as a production client KPI. The evidence is intended to make the implementation inspectable and reproducible.

## Business interpretation

- Move beyond a probability score to a lending decision
- Balance revenue against expected loss
- Make risk appetite explicit
- Explain material risk drivers

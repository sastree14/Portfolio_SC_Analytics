# Results

## What the public example demonstrates

The example output for **SC-23 · Operations Simulation & What-If Engine** is generated from representative public inputs and demonstrates the end-to-end decision path of the project.

It is useful for checking:

- average wait
- P95 wait
- resource utilization
- throughput
- queue length

## How to read the evidence

- `examples/inputs/` shows the input shape used by the public run.
- `examples/outputs/` shows the resulting structured output.
- `examples/logs/` shows the execution sequence.
- `examples/visuals/` contains the project-level analytical visual when applicable.

The values in the public example are not presented as a production client KPI. The evidence is intended to make the implementation inspectable and reproducible.

## Business interpretation

- Test changes without disrupting operations
- Quantify waiting-time and utilization risk
- Compare staffing scenarios under uncertainty
- Expose tail outcomes, not only averages

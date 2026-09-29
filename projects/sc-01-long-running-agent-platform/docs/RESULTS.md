# Results

## What the public example demonstrates

The example output for **SC-01 · Long-Running AI Agent Platform** is generated from representative public inputs and demonstrates the end-to-end decision path of the project.

It is useful for checking:

- completion rate
- approval waiting time
- retry count
- external-action success rate
- end-to-end execution time

## How to read the evidence

- `examples/inputs/` shows the input shape used by the public run.
- `examples/outputs/` shows the resulting structured output.
- `examples/logs/` shows the execution sequence.
- `examples/visuals/` contains the project-level analytical visual when applicable.

The values in the public example are not presented as a production client KPI. The evidence is intended to make the implementation inspectable and reproducible.

## Business interpretation

- Keep workflow state independent from a single LLM request
- Require explicit approval before sensitive external actions
- Recover from transient failures without losing the business process
- Preserve an inspectable execution history

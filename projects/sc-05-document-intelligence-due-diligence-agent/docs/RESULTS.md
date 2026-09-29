# Results

## What the public example demonstrates

The example output for **SC-05 · Document Intelligence & Due Diligence Agent** is generated from representative public inputs and demonstrates the end-to-end decision path of the project.

It is useful for checking:

- documents processed
- retrieval hit rate
- findings with evidence
- manual review time
- extraction exceptions

## How to read the evidence

- `examples/inputs/` shows the input shape used by the public run.
- `examples/outputs/` shows the resulting structured output.
- `examples/logs/` shows the execution sequence.
- `examples/visuals/` contains the project-level analytical visual when applicable.

The values in the public example are not presented as a production client KPI. The evidence is intended to make the implementation inspectable and reproducible.

## Business interpretation

- Reduce time spent searching large document sets
- Keep every finding tied to source evidence
- Separate extracted fact from interpretation
- Make document review repeatable

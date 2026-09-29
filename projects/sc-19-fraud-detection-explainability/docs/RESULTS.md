# Results

## What the public example demonstrates

The example output for **SC-19 · Fraud Detection & Explainability System** is generated from representative public inputs and demonstrates the end-to-end decision path of the project.

It is useful for checking:

- PR AUC
- recall at review capacity
- false-positive rate
- expected fraud loss
- cases prioritized

## How to read the evidence

- `examples/inputs/` shows the input shape used by the public run.
- `examples/outputs/` shows the resulting structured output.
- `examples/logs/` shows the execution sequence.
- `examples/visuals/` contains the project-level analytical visual when applicable.

The values in the public example are not presented as a production client KPI. The evidence is intended to make the implementation inspectable and reproducible.

## Business interpretation

- Prioritize limited investigation capacity
- Balance fraud capture against false positives
- Explain suspicious scores
- Choose thresholds using cost rather than accuracy

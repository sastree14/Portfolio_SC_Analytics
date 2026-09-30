# Validation

## Public execution

The principal `run_project.py` is deterministic and does not require GPU access.

It validates:

- class mapping
- confidence-policy behaviour
- object counting
- stream counting
- frame-level review decision

## Model validation

A trained detector should be reviewed using:

- precision per class
- recall per class
- mAP50
- mAP50-95
- confusion matrix
- confidence threshold analysis
- review-rate analysis
- latency on the target hardware

## Operational validation

Before deployment, validation should also cover:

- new lighting conditions
- occlusion
- camera vibration
- reflections
- partially visible items
- new packaging
- crowded frames

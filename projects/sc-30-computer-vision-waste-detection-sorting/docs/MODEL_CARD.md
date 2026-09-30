# Model card

## Task

Multi-class object detection for visible waste items.

## Classes

- plastic_bottle
- glass_bottle
- aluminum_can
- cardboard
- paper
- food_container
- residual_waste

## Intended use

- visual sorting assistance
- item counting
- material routing
- inspection and review prioritization
- quality-control workflows

## Out-of-scope use

The model should not be treated as a chemical material-identification system.

It identifies visually observable classes. It cannot reliably infer hidden material composition when packaging appearance is ambiguous.

## Training approach

The implementation uses transfer learning from pretrained object-detection weights.

The training process should include:

- task-specific bounding-box annotations
- augmentation appropriate to the camera environment
- separated train / validation / test capture sessions
- early stopping
- per-class evaluation

## Evaluation

Review at minimum:

- precision
- recall
- mAP50
- mAP50-95
- confusion matrix
- class support
- inference latency
- confidence / review policy

## Known difficult cases

- transparent materials
- reflections
- crushed objects
- partial occlusion
- visually similar packaging
- residual waste with highly variable shape
- new item types outside the training distribution

## Human review

Low-confidence results are deliberately allowed to enter a review state. The system is not designed to force an automatic class decision for every visible object.

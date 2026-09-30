# Data

## Dataset structure

The training pipeline expects a YOLO-compatible dataset.

```text
dataset/
├── images/
│   ├── train/
│   ├── val/
│   └── test/
├── labels/
│   ├── train/
│   ├── val/
│   └── test/
└── dataset.yaml
```

## Classes

| ID | Class | Operating stream |
|---:|---|---|
| 0 | plastic_bottle | plastic |
| 1 | glass_bottle | glass |
| 2 | aluminum_can | metal |
| 3 | cardboard | paper_cardboard |
| 4 | paper | paper_cardboard |
| 5 | food_container | plastic_or_review |
| 6 | residual_waste | residual |

## Annotation requirements

Each visible object should be annotated independently.

The dataset should intentionally include:

- partial occlusions
- multiple items per frame
- different rotations
- difficult lighting
- crushed containers
- transparent objects
- dirty packaging
- background clutter

## Train / validation / test split

Frames from the same video sequence or capture session should not be randomly distributed across every split if this creates near-duplicates.

A stronger split separates capture sessions so validation better represents new operating conditions.

## Public repository

The repository does not publish real production images. It includes the schema, configuration and representative detection outputs required to reproduce the workflow with an appropriate labeled dataset.

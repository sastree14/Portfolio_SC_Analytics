# Technical decisions

## 1. Object detection rather than image-level classification

A frame can contain multiple objects. Image-level classification would only answer "what is this image?" rather than "which objects are present and where are they?"

Object detection provides:

- class
- bounding box
- confidence
- countable instances

## 2. Transfer learning

The detector starts from pretrained weights and is fine-tuned on the project classes.

This reduces the quantity of task-specific data needed compared with training a detector from scratch.

## 3. Explicit residual class plus unknown/review state

Residual waste is visually heterogeneous. The system therefore keeps two concepts separate:

- `residual_waste`: a trained class with labeled examples
- `review`: the operational state for detections that are not trustworthy enough to automate

Unknown is not silently converted into residual.

## 4. Confidence threshold is a business control

The best confidence threshold is not necessarily the one with the best generic metric.

It depends on the cost of:

- missing an item
- misclassifying an item
- sending too many items to human review

## 5. Detector output remains structured

The downstream system receives structured detections rather than annotated pixels only.

That allows the same model output to support:

- counting
- verification
- alerts
- sorting
- dashboards
- audit

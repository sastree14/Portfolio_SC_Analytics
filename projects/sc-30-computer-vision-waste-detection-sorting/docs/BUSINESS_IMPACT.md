# Business impact

## Operating problem

Manual visual inspection is repetitive and inconsistent when many items must be identified quickly.

A computer-vision layer can convert a camera frame into a structured record:

- what objects were detected
- how many of each object were present
- where they appeared
- how confident the model was
- which material stream each object belongs to
- which detections require human review

## Decisions supported

The system supports decisions such as:

- whether the frame contains recyclable items
- how many items of each class were detected
- whether an item should be sent to plastic, glass, metal, paper/cardboard or residual
- whether confidence is too low for automatic handling
- which classes are producing the most review cases

## Operational KPIs

Useful production KPIs include:

- precision and recall by class
- mAP at the chosen IoU thresholds
- false-negative rate
- detections per frame
- percentage of frames requiring manual review
- inference latency
- review rate by class
- class distribution over time

The public example demonstrates the decision path. Real production targets should be defined after observing the actual camera, lighting, item mix and error cost.

# Architecture

## Objective

Convert a camera image into a structured and reviewable set of detections that can drive a sorting or verification workflow.

```text
Camera / image source
        ↓
OpenCV preprocessing
        ↓
YOLO detector
        ↓
Boxes + classes + confidence
        ↓
Post-processing
        ├── class mapping
        ├── confidence policy
        └── duplicate / count handling
        ↓
Decision layer
        ├── automatic stream
        └── manual review
        ↓
FastAPI / downstream integration
        ↓
Detection log + monitoring
```

## Component responsibilities

### Image ingestion

Receives a file, frame or camera snapshot and normalizes it to the input expected by the detector.

### Detector

Produces bounding boxes, class IDs and confidence scores.

### Post-processing

Maps detector classes into operational material streams and applies review thresholds.

### Decision layer

Determines whether a detection is safe to use automatically or should be reviewed.

### API

Exposes inference results to another application, conveyor controller, verification UI or operational system.

## Deployment pattern

A production system can run:

- on an edge device close to the camera
- on a local workstation
- on a GPU server
- in a cloud inference service

The correct option depends on latency, connectivity, hardware and data-retention constraints.

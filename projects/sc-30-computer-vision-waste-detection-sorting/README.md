# SC-30 · Computer Vision Waste Detection & Sorting System

**A computer-vision system for detecting, counting and classifying waste items from camera images, then mapping detections to material streams or manual review.**

**Designed for:** recycling · waste sorting · hospitality operations · quality control · edge-AI inspection

## Why this project matters

Visual sorting problems are operational problems, not only classification problems. A useful system has to identify objects, count them, handle overlapping items, preserve confidence information and decide what should happen when the model is uncertain.

SC-30 is designed around that complete workflow.

- detect multiple objects in the same frame
- distinguish visually identifiable materials and item types
- count detections by class
- map detected classes to disposal streams
- route low-confidence or ambiguous objects to review
- retain frame-level results for traceability and model improvement

A business reviewer can understand the operating value from this page. A technical reviewer can start directly with the [principal execution file](technical/run_project.py).

## Example operating flow

```text
Camera frame
    ↓
Image preprocessing
    ↓
Object detector
    ↓
Bounding boxes + class + confidence
    ↓
Material / stream mapping
    ↓
Count + verification rules
    ↓
Sort / residual / manual review
    ↓
Persisted detection result
```

## Detection classes

The reference implementation is structured around seven object classes:

- plastic_bottle
- glass_bottle
- aluminum_can
- cardboard
- paper
- food_container
- residual_waste

These are then mapped into broader operating streams such as plastic, glass, metal, paper/cardboard and residual waste.

## Why residual waste is treated differently

A bottle or can has relatively stable visual structure. Residual waste is broader and can include irregular or partially occluded objects.

For that reason, the system does not rely on one rule saying "anything unknown is residual." It uses:

1. an explicit residual-waste training class when examples exist
2. a confidence threshold
3. an unknown / review state when the detector is not sufficiently certain

That distinction is important in real operations because silently forcing every uncertain object into one class creates false confidence.

## Technology at a glance

**Python · PyTorch · Ultralytics YOLO · OpenCV · FastAPI · NumPy · Pandas · Plotly · Docker**

## What is included

- [Business impact](docs/BUSINESS_IMPACT.md)
- [Results and evaluation interpretation](docs/RESULTS.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Technical decisions](docs/TECHNICAL_DECISIONS.md)
- [Data and annotation structure](docs/DATA.md)
- [Model card](docs/MODEL_CARD.md)
- [Edge deployment](docs/EDGE_DEPLOYMENT.md)
- [Security and permissions](docs/SECURITY_AND_PERMISSIONS.md)
- [Credentials and integrations](docs/CREDENTIALS_AND_INTEGRATIONS.md)
- [Environments](docs/ENVIRONMENTS.md)
- [Limitations](docs/LIMITATIONS.md)
- [Example evidence](examples/README.md)
- [Technical implementation](technical/README.md)

## Visual evidence

![SC-30 project visual](examples/visuals/result.svg)

## Main technical execution

**Start with [`technical/run_project.py`](technical/run_project.py).**

That file shows the public end-to-end path in one place:

```text
detections
→ confidence handling
→ class-to-stream mapping
→ counting
→ review decision
→ structured output
```

The deeper computer-vision implementation then lives in `technical/src/`:

- training
- image inference
- post-processing
- evaluation
- API serving

## Local review

The deterministic public execution path does not need GPU access or model weights:

```bash
cd technical
python run_project.py
pytest -q
```

To train or run image inference with the detector, install the full requirements and provide a YOLO-format dataset/model checkpoint.

## Transferable pattern

Although this project is framed around waste identification, the same engineering pattern is directly applicable to:

- item counting
- packaging verification
- production-line inspection
- order verification
- missing-item detection
- visual quality control

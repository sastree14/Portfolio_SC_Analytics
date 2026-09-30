# Technical implementation

## Main execution path

**Start here → [`run_project.py`](run_project.py)**

This is the principal public execution file for SC-30. It shows the complete decision path after detector inference:

**detections → confidence policy → material mapping → counts → review decision → output**

The detector-specific training and image inference code lives in supporting modules because those paths require model weights and image data.

## Supporting implementation

- `src/train.py` — transfer-learning entry point
- `src/inference.py` — image inference using a trained detector
- `src/postprocess.py` — class mapping and review policy
- `src/evaluation.py` — class-level evaluation helpers
- `src/api.py` — FastAPI serving layer
- `data/dataset.yaml` — class configuration
- `tests/` — deterministic validation
- `infra/Dockerfile` — container runtime

## Stack

- Python
- PyTorch
- Ultralytics YOLO
- OpenCV
- FastAPI
- NumPy
- Pandas
- Plotly
- Docker

## Run the deterministic public path

```bash
python run_project.py
pytest -q
```

## Train a detector

After adding a YOLO-format dataset:

```bash
python src/train.py --data data/dataset.yaml --epochs 50
```

## Run image inference

```bash
python src/inference.py --model runs/detect/sc30/weights/best.pt --image path/to/image.jpg
```

## Review order

1. project README
2. `run_project.py`
3. `src/postprocess.py`
4. `src/train.py` and `src/inference.py`
5. API, tests and dataset configuration

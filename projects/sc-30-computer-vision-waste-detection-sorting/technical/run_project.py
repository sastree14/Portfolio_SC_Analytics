"""SC-30 · Computer Vision Waste Detection & Sorting System

MAIN EXECUTION FILE

This public entry point starts from representative detector outputs so the
complete business decision path is runnable without GPU access or model weights.

The actual training and image-inference implementations are in src/train.py and
src/inference.py.
"""
from __future__ import annotations

import json
from pathlib import Path

from src.postprocess import Detection, classify_detection, summarize_frame

TECHNICAL = Path(__file__).resolve().parent
PROJECT = TECHNICAL.parent
EXAMPLES = PROJECT / "examples"


def representative_detector_output() -> list[Detection]:
    return [
        Detection("plastic_bottle", 0.93, (86, 122, 260, 566)),
        Detection("plastic_bottle", 0.88, (304, 160, 447, 538)),
        Detection("glass_bottle", 0.91, (496, 98, 622, 548)),
        Detection("aluminum_can", 0.86, (682, 318, 804, 530)),
        Detection("residual_waste", 0.58, (844, 246, 1120, 558)),
        Detection("food_container", 0.39, (78, 48, 214, 142)),
    ]


def main() -> dict:
    raw = representative_detector_output()

    processed = [
        classify_detection(
            detection,
            confidence_threshold=0.45,
            review_threshold=0.60,
        )
        for detection in raw
    ]

    result = summarize_frame(processed, frame_id="frame-1042")

    output = EXAMPLES / "outputs" / "main_run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print(json.dumps(result, indent=2))
    return result


if __name__ == "__main__":
    main()

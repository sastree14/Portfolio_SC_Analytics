from __future__ import annotations

import argparse
import json
from pathlib import Path

from ultralytics import YOLO

from postprocess import Detection, classify_detection, summarize_frame


def predict(model_path: str, image_path: str, confidence: float = 0.25) -> dict:
    model = YOLO(model_path)
    result = model.predict(source=image_path, conf=confidence, verbose=False)[0]

    names = result.names
    raw_detections: list[Detection] = []

    if result.boxes is not None:
        for box in result.boxes:
            cls_id = int(box.cls.item())
            conf = float(box.conf.item())
            xyxy = tuple(int(round(x)) for x in box.xyxy[0].tolist())
            raw_detections.append(
                Detection(
                    class_name=names[cls_id],
                    confidence=conf,
                    bbox_xyxy=xyxy,
                )
            )

    processed = [classify_detection(x) for x in raw_detections]
    return summarize_frame(processed, frame_id=Path(image_path).stem)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--image", required=True)
    parser.add_argument("--confidence", type=float, default=0.25)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    print(json.dumps(predict(args.model, args.image, args.confidence), indent=2))

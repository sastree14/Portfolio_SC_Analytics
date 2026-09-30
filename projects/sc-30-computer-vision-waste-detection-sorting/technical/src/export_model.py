from __future__ import annotations

import argparse

from ultralytics import YOLO


def export_onnx(model_path: str, image_size: int = 640):
    model = YOLO(model_path)
    return model.export(
        format="onnx",
        imgsz=image_size,
        simplify=True,
        dynamic=True,
    )


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--image-size", type=int, default=640)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    print(export_onnx(args.model, args.image_size))

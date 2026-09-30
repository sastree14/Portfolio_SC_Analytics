from __future__ import annotations

import argparse
import os

from ultralytics import YOLO


def train(
    data: str,
    base_model: str,
    epochs: int,
    image_size: int,
    batch: int,
    device: str,
):
    model = YOLO(base_model)
    return model.train(
        data=data,
        epochs=epochs,
        imgsz=image_size,
        batch=batch,
        device=device,
        project="runs/detect",
        name="sc30",
        patience=12,
        cache=False,
        plots=True,
    )


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data/dataset.yaml")
    parser.add_argument("--base-model", default=os.getenv("BASE_MODEL", "yolo11n.pt"))
    parser.add_argument("--epochs", type=int, default=50)
    parser.add_argument("--image-size", type=int, default=640)
    parser.add_argument("--batch", type=int, default=16)
    parser.add_argument("--device", default=os.getenv("DEVICE", "cpu"))
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    train(
        data=args.data,
        base_model=args.base_model,
        epochs=args.epochs,
        image_size=args.image_size,
        batch=args.batch,
        device=args.device,
    )

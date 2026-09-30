from __future__ import annotations

import argparse
import time

import cv2
from ultralytics import YOLO


def run_camera(
    model_path: str,
    source: str,
    confidence: float = 0.45,
    every_n_frames: int = 1,
):
    model = YOLO(model_path)
    capture = cv2.VideoCapture(int(source) if source.isdigit() else source)

    if not capture.isOpened():
        raise RuntimeError(f"Unable to open camera source: {source}")

    frame_index = 0

    try:
        while True:
            ok, frame = capture.read()
            if not ok:
                break

            frame_index += 1
            if frame_index % every_n_frames:
                continue

            started = time.perf_counter()
            result = model.predict(frame, conf=confidence, verbose=False)[0]
            latency_ms = (time.perf_counter() - started) * 1000

            count = 0 if result.boxes is None else len(result.boxes)
            print(
                {
                    "frame": frame_index,
                    "detections": count,
                    "latency_ms": round(latency_ms, 1),
                }
            )
    finally:
        capture.release()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--source", default="0")
    parser.add_argument("--confidence", type=float, default=0.45)
    parser.add_argument("--every-n-frames", type=int, default=1)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    run_camera(
        model_path=args.model,
        source=args.source,
        confidence=args.confidence,
        every_n_frames=args.every_n_frames,
    )

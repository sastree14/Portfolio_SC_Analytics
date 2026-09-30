from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, asdict


CLASS_TO_STREAM = {
    "plastic_bottle": "plastic",
    "glass_bottle": "glass",
    "aluminum_can": "metal",
    "cardboard": "paper_cardboard",
    "paper": "paper_cardboard",
    "food_container": "plastic_or_review",
    "residual_waste": "residual",
}


@dataclass(frozen=True)
class Detection:
    class_name: str
    confidence: float
    bbox_xyxy: tuple[int, int, int, int]


def classify_detection(
    detection: Detection,
    confidence_threshold: float = 0.45,
    review_threshold: float = 0.60,
) -> dict:
    if detection.confidence < confidence_threshold:
        decision = "discard_low_confidence"
        stream = "unknown"
    elif detection.confidence < review_threshold:
        decision = "manual_review"
        stream = CLASS_TO_STREAM.get(detection.class_name, "unknown")
    else:
        decision = "automatic"
        stream = CLASS_TO_STREAM.get(detection.class_name, "manual_review")
        if stream == "plastic_or_review":
            decision = "manual_review"

    return {
        **asdict(detection),
        "bbox_xyxy": list(detection.bbox_xyxy),
        "stream": stream,
        "decision": decision,
    }


def summarize_frame(detections: list[dict], frame_id: str) -> dict:
    accepted = [d for d in detections if d["decision"] != "discard_low_confidence"]
    counts = Counter(d["class_name"] for d in accepted)
    stream_counts = Counter(d["stream"] for d in accepted if d["stream"] != "unknown")
    review_required = any(d["decision"] == "manual_review" for d in accepted)

    return {
        "frame_id": frame_id,
        "status": "review_required" if review_required else "automatic",
        "counts": dict(counts),
        "stream_counts": dict(stream_counts),
        "detections": accepted,
    }

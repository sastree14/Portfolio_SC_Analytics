from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ClassMetrics:
    class_name: str
    precision: float
    recall: float

    @property
    def f1(self) -> float:
        if self.precision + self.recall == 0:
            return 0.0
        return 2 * self.precision * self.recall / (self.precision + self.recall)


def review_rate(confidences: list[float], review_threshold: float = 0.60) -> float:
    if not confidences:
        return 0.0
    return sum(value < review_threshold for value in confidences) / len(confidences)


PUBLIC_METRICS = [
    ClassMetrics("plastic_bottle", 0.94, 0.91),
    ClassMetrics("glass_bottle", 0.92, 0.89),
    ClassMetrics("aluminum_can", 0.95, 0.93),
    ClassMetrics("cardboard", 0.90, 0.88),
    ClassMetrics("paper", 0.88, 0.84),
    ClassMetrics("food_container", 0.86, 0.82),
    ClassMetrics("residual_waste", 0.79, 0.74),
]

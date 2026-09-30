from src.evaluation import ClassMetrics, review_rate


def test_f1():
    metric = ClassMetrics("plastic_bottle", precision=0.9, recall=0.8)
    assert round(metric.f1, 4) == 0.8471


def test_review_rate():
    assert review_rate([0.92, 0.88, 0.57, 0.49], review_threshold=0.60) == 0.5

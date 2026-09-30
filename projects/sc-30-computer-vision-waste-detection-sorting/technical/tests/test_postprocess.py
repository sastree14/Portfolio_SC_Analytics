from src.postprocess import Detection, classify_detection, summarize_frame


def test_high_confidence_detection_is_automatic():
    result = classify_detection(
        Detection("plastic_bottle", 0.91, (0, 0, 100, 200)),
        confidence_threshold=0.45,
        review_threshold=0.60,
    )
    assert result["stream"] == "plastic"
    assert result["decision"] == "automatic"


def test_low_confidence_detection_is_discarded():
    result = classify_detection(
        Detection("glass_bottle", 0.31, (0, 0, 100, 200)),
        confidence_threshold=0.45,
        review_threshold=0.60,
    )
    assert result["stream"] == "unknown"
    assert result["decision"] == "discard_low_confidence"


def test_borderline_residual_requires_review():
    result = classify_detection(
        Detection("residual_waste", 0.58, (0, 0, 100, 200)),
        confidence_threshold=0.45,
        review_threshold=0.60,
    )
    assert result["stream"] == "residual"
    assert result["decision"] == "manual_review"


def test_frame_summary_counts_and_flags_review():
    detections = [
        classify_detection(Detection("plastic_bottle", 0.93, (0, 0, 10, 10))),
        classify_detection(Detection("plastic_bottle", 0.88, (12, 0, 22, 10))),
        classify_detection(Detection("residual_waste", 0.58, (30, 0, 50, 20))),
    ]
    result = summarize_frame(detections, "frame-1")
    assert result["counts"]["plastic_bottle"] == 2
    assert result["stream_counts"]["plastic"] == 2
    assert result["status"] == "review_required"

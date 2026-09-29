from prometheus_client import Counter, Histogram

PREDICTIONS = Counter("model_predictions_total", "Number of model predictions", ["model_version"])
LATENCY = Histogram("model_prediction_latency_seconds", "Prediction latency", ["model_version"])

def record_prediction(model_version: str, latency_seconds: float) -> None:
    PREDICTIONS.labels(model_version=model_version).inc()
    LATENCY.labels(model_version=model_version).observe(latency_seconds)

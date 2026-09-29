import mlflow

def log_candidate(model_name: str, metrics: dict):
    with mlflow.start_run(run_name=model_name):
        mlflow.log_params({"model_name":model_name})
        mlflow.log_metrics(metrics)

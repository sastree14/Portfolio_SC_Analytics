from prefect import flow, task

@task(retries=2, retry_delay_seconds=30)
def load_history():
    return {"rows": 10000, "status": "loaded"}

@task
def run_backtests(history):
    return {"h1_wape": 0.118, "h3_wape": 0.146, "h6_wape": 0.173, "h9_wape": 0.201}

@task
def publish_if_better(metrics):
    return {"published": metrics["h1_wape"] < 0.15, "metrics": metrics}

@flow(name="sc12-forecast-retraining")
def retraining_flow():
    history = load_history()
    metrics = run_backtests(history)
    return publish_if_better(metrics)

if __name__ == "__main__":
    retraining_flow()

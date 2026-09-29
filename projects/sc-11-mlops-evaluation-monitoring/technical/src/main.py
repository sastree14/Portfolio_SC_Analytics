THRESHOLDS={"quality":0.80,"drift":0.20}
RUNS=[
 {"model":"baseline","quality":0.79,"drift":0.08},
 {"model":"candidate-a","quality":0.84,"drift":0.12},
 {"model":"candidate-b","quality":0.87,"drift":0.27},
]
def evaluate(run):
    return {**run,"release":run["quality"]>=THRESHOLDS["quality"] and run["drift"]<=THRESHOLDS["drift"]}
def run_example(): return {"project":"SC-11","evaluations":[evaluate(x) for x in RUNS]}
if __name__=="__main__":
 import json; print(json.dumps(run_example(),indent=2))

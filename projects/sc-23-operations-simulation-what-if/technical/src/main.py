import random, statistics
def simulate(seed=7,arrivals=80,capacity=3):
    random.seed(seed)
    waits=[]
    for _ in range(arrivals):
        load=random.random()*capacity
        waits.append(max(0,round((load-(capacity-1))*8,2)))
    return {"avg_wait":round(statistics.mean(waits),2),"p95_wait":sorted(waits)[int(.95*len(waits))-1]}
def run_example():
    return {"project":"SC-23","current":simulate(capacity=3),"plus_one_resource":simulate(capacity=4)}
if __name__=="__main__":
 import json; print(json.dumps(run_example(),indent=2))

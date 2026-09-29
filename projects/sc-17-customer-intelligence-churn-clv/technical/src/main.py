from math import exp

SCORES=[-1.6,-0.8,-0.2,0.4,1.1,1.8]
def sigmoid(x): return 1/(1+exp(-x))
def run_example():
    probs=[round(sigmoid(x),4) for x in SCORES]
    ranked=sorted(enumerate(probs,1),key=lambda x:x[1],reverse=True)
    return {"project":"SC-17","probabilities":probs,"priority_order":[i for i,_ in ranked],"mean_probability":round(sum(probs)/len(probs),4)}
if __name__=="__main__":
    import json; print(json.dumps(run_example(),indent=2))

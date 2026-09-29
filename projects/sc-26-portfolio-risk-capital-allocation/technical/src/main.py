import math
RETURNS=[0.08,0.12,0.06]
VOL=[0.14,0.22,0.10]
def score(weights):
    er=sum(w*r for w,r in zip(weights,RETURNS))
    risk=math.sqrt(sum((w*v)**2 for w,v in zip(weights,VOL)))
    return {"weights":weights,"expected_return":round(er,4),"risk":round(risk,4),"return_to_risk":round(er/risk,3)}
def run_example():
    candidates=[[.33,.33,.34],[.5,.2,.3],[.2,.5,.3],[.4,.1,.5]]
    rows=[score(x) for x in candidates]
    return {"project":"SC-26","best":max(rows,key=lambda x:x["return_to_risk"]),"candidates":rows}
if __name__=="__main__":
 import json; print(json.dumps(run_example(),indent=2))

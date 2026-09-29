DEMAND=[34,28,19,41]
MARGIN=[12,9,15,8]
CAPACITY=85

def optimize():
    remaining=CAPACITY
    allocation=[0]*len(DEMAND)
    order=sorted(range(len(DEMAND)),key=lambda i:MARGIN[i],reverse=True)
    for i in order:
        allocation[i]=min(DEMAND[i],remaining)
        remaining-=allocation[i]
        if remaining<=0: break
    value=sum(a*m for a,m in zip(allocation,MARGIN))
    return {"project":"SC-20","allocation":allocation,"unused_capacity":remaining,"objective_value":value}
if __name__=="__main__":
    import json; print(json.dumps(optimize(),indent=2))

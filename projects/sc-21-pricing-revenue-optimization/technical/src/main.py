BASE_DEMAND=1000
def demand(price,base_price=100,elasticity=-1.4):
    return BASE_DEMAND*(price/base_price)**elasticity
def contribution(price,unit_cost=52):
    q=demand(price); return {"price":price,"demand":round(q,1),"contribution":round((price-unit_cost)*q,2)}
def run_example():
    candidates=[80,90,100,110,120]
    rows=[contribution(p) for p in candidates]
    return {"project":"SC-21","best":max(rows,key=lambda x:x["contribution"]),"candidates":rows}
if __name__=="__main__":
 import json; print(json.dumps(run_example(),indent=2))

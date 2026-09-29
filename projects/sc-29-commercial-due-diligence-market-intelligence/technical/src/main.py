QUESTIONS={"market_growth":4,"competition":3,"customer_concentration":2,"pricing_power":4,"regulation":2}
def run_example():
    supported={k:{"evidence_items":v,"status":"supported" if v>=3 else "review"} for k,v in QUESTIONS.items()}
    return {"project":"SC-29","questions":supported,"supported_count":sum(1 for x in supported.values() if x["status"]=="supported")}
if __name__=="__main__":
 import json; print(json.dumps(run_example(),indent=2))

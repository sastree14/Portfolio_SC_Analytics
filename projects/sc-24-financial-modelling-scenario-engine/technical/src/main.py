def project_cashflows(revenue0=120000,growth=.12,margin=.58,opex0=52000,months=12):
    rows=[]; cash=150000
    for m in range(1,months+1):
        revenue=revenue0*((1+growth)**(m/12))
        gross=revenue*margin
        opex=opex0*(1.01**m)
        fcf=gross-opex
        cash+=fcf
        rows.append({"month":m,"revenue":round(revenue,2),"fcf":round(fcf,2),"cash":round(cash,2)})
    return rows
def run_example():
    rows=project_cashflows()
    return {"project":"SC-24","ending_cash":rows[-1]["cash"],"months":rows}
if __name__=="__main__":
 import json; print(json.dumps(run_example(),indent=2))

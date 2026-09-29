def feasibility(gdv,land,build,fees,finance):
    total=land+build+fees+finance
    profit=gdv-total
    margin=profit/gdv
    return {"gdv":gdv,"total_cost":total,"profit":profit,"margin":round(margin,4)}
def run_example():
    return {"project":"SC-28","downside":feasibility(7_600_000,1_500_000,4_300_000,420_000,380_000),"base":feasibility(8_400_000,1_500_000,4_200_000,420_000,360_000),"upside":feasibility(9_100_000,1_500_000,4_100_000,420_000,340_000)}
if __name__=="__main__":
 import json; print(json.dumps(run_example(),indent=2))

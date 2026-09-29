from ortools.sat.python import cp_model

def assign(jobs,resources):
    model=cp_model.CpModel()
    x={(j,r):model.NewBoolVar(f"x_{j}_{r}") for j in jobs for r in resources}
    for j in jobs:
        model.Add(sum(x[j,r] for r in resources)==1)
    return model,x

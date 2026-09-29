from ortools.linear_solver import pywraplp

def build_model(demand, margin, capacity):
    s=pywraplp.Solver.CreateSolver("SCIP")
    x=[s.IntVar(0,demand[i],f"x_{i}") for i in range(len(demand))]
    s.Add(sum(x)<=capacity)
    s.Maximize(sum(x[i]*margin[i] for i in range(len(x))))
    return s,x

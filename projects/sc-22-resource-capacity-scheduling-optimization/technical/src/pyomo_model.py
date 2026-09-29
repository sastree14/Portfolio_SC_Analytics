import pyomo.environ as pyo

def build(jobs, resources):
    m=pyo.ConcreteModel()
    m.J=pyo.Set(initialize=jobs)
    m.R=pyo.Set(initialize=resources)
    m.x=pyo.Var(m.J,m.R,domain=pyo.Binary)
    m.assign=pyo.Constraint(m.J,rule=lambda m,j: sum(m.x[j,r] for r in m.R)==1)
    return m

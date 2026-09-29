import cvxpy as cp
import numpy as np

def min_variance(cov, max_weight=.6):
    n=cov.shape[0]; w=cp.Variable(n)
    problem=cp.Problem(cp.Minimize(cp.quad_form(w,cov)),[cp.sum(w)==1,w>=0,w<=max_weight])
    problem.solve()
    return np.asarray(w.value).round(6)

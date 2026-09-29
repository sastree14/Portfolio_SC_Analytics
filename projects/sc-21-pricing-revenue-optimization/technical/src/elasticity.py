import statsmodels.api as sm
import numpy as np

def estimate_elasticity(price, quantity):
    X=sm.add_constant(np.log(price))
    model=sm.OLS(np.log(quantity),X).fit()
    return float(model.params[1])

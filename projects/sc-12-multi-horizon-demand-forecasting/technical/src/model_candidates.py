from lightgbm import LGBMRegressor
from xgboost import XGBRegressor

def candidates():
    return {
        "xgboost": XGBRegressor(n_estimators=250,max_depth=6,learning_rate=0.05),
        "lightgbm": LGBMRegressor(n_estimators=250,num_leaves=31,learning_rate=0.05),
    }

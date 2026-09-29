from xgboost import XGBClassifier

def build_model(scale_pos_weight: float):
    return XGBClassifier(n_estimators=350,max_depth=6,learning_rate=0.04,scale_pos_weight=scale_pos_weight)

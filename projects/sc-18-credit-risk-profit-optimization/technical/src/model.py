from xgboost import XGBClassifier

def build_model():
    return XGBClassifier(n_estimators=300,max_depth=5,learning_rate=0.04,subsample=0.85,colsample_bytree=0.8)

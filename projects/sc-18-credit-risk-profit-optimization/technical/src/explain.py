import shap

def explain(model, frame):
    return shap.TreeExplainer(model)(frame)

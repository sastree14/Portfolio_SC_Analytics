import shap

def transaction_explanation(model, row):
    return shap.TreeExplainer(model)(row)

from lifelines import CoxPHFitter

def fit_survival(frame):
    model=CoxPHFitter()
    model.fit(frame,duration_col="tenure_days",event_col="churned")
    return model

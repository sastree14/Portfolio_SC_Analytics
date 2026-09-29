from fastapi import FastAPI
from main import feasibility
app=FastAPI()
@app.get("/feasibility")
def calc(gdv:float,land:float,build:float,fees:float,finance:float):
    return feasibility(gdv,land,build,fees,finance)

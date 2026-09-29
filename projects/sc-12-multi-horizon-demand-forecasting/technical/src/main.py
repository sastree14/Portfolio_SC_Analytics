from statistics import mean

SERIES=[100,108,96,116,123,119,131,128]

def moving_average(values, window=3):
    out=[]
    for i in range(len(values)):
        start=max(0,i-window+1)
        out.append(round(mean(values[start:i+1]),2))
    return out

def run_example():
    fitted=moving_average(SERIES)
    return {"project":"SC-12","actual":SERIES,"fitted":fitted,"next_forecast":round(mean(SERIES[-3:]),2)}

if __name__=="__main__":
    import json; print(json.dumps(run_example(),indent=2))

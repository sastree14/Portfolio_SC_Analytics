PRICES=[100,101,100.5,102,103,102.2,104]
def run_example():
    returns=[round(PRICES[i]/PRICES[i-1]-1,5) for i in range(1,len(PRICES))]
    signal=[1 if r>0 else -1 for r in returns]
    pnl=[round(signal[i-1]*returns[i],5) if i else 0 for i in range(len(returns))]
    return {"project":"SC-27","returns":returns,"signal":signal,"strategy_pnl":pnl,"total_pnl":round(sum(pnl),5)}
if __name__=="__main__":
 import json; print(json.dumps(run_example(),indent=2))

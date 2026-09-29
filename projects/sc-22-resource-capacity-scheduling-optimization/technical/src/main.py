JOBS=[("J1",4,9),("J2",6,14),("J3",3,8),("J4",5,11)]
CAPACITY=12
def run_example():
    ranked=sorted(JOBS,key=lambda x:x[2]/x[1],reverse=True)
    used=0; selected=[]
    for job,hours,value in ranked:
        if used+hours<=CAPACITY:
            selected.append(job); used+=hours
    return {"project":"SC-22","selected_jobs":selected,"used_hours":used,"remaining_hours":CAPACITY-used}
if __name__=="__main__":
 import json; print(json.dumps(run_example(),indent=2))

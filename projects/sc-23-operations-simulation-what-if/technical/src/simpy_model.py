import simpy

def customer(env, resource, service_time, waits):
    arrival=env.now
    with resource.request() as req:
        yield req
        waits.append(env.now-arrival)
        yield env.timeout(service_time)

def run(capacity=3):
    env=simpy.Environment(); resource=simpy.Resource(env,capacity=capacity); waits=[]
    for i in range(20):
        env.process(customer(env,resource,2+(i%3),waits))
        env.run(until=env.now+1)
    env.run()
    return waits

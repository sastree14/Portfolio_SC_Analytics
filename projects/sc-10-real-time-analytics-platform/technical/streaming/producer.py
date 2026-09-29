import json, time
from confluent_kafka import Producer

producer=Producer({"bootstrap.servers":"localhost:19092"})
for i in range(10):
    producer.produce("events", json.dumps({"event_id":i,"value":i*7}).encode())
producer.flush()

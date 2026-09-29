import json
import redis

class LiveBook:
    def __init__(self,url="redis://localhost:6379/0"):
        self.r=redis.from_url(url,decode_responses=True)
    def set(self,symbol,state):
        self.r.set(f"book:{symbol}",json.dumps(state),ex=30)
    def get(self,symbol):
        raw=self.r.get(f"book:{symbol}"); return json.loads(raw) if raw else None

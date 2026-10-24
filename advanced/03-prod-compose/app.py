import os

import redis
from fastapi import FastAPI

app = FastAPI()
client = redis.Redis.from_url(os.environ["REDIS_URL"], decode_responses=True)


@app.get("/")
def index():
    count = client.incr("hits")
    return {"hits": count, "via": "api -> redis"}


@app.get("/health")
def health():
    client.ping()
    return {"status": "ok"}

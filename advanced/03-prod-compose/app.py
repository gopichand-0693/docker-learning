import os

from flask import Flask, jsonify
import redis

app = Flask(__name__)
client = redis.Redis.from_url(os.environ["REDIS_URL"], decode_responses=True)


@app.get("/")
def index():
    count = client.incr("hits")
    return jsonify({"hits": count, "via": "api -> redis"})


@app.get("/health")
def health():
    client.ping()
    return jsonify({"status": "ok"})

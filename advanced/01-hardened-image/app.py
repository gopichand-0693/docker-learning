import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(
        {
            "message": "running as a non-root process behind gunicorn",
            "user": os.getuid(),
        }
    )


@app.get("/health")
def health():
    return jsonify({"status": "ok"})

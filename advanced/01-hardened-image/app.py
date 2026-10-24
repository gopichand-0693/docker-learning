import os

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {
        "message": "running as a non-root process behind uvicorn",
        "user": os.getuid(),
    }


@app.get("/health")
def health():
    return {"status": "ok"}

import os

import psycopg2
from fastapi import FastAPI

app = FastAPI()
DATABASE_URL = os.environ["DATABASE_URL"]


def connect():
    return psycopg2.connect(DATABASE_URL)


@app.get("/")
def index():
    conn = connect()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO visits (created_at) VALUES (NOW()) RETURNING id;"
            )
            visit_id = cur.fetchone()[0]
            cur.execute("SELECT COUNT(*) FROM visits;")
            count = cur.fetchone()[0]
        conn.commit()
    finally:
        conn.close()
    return {
        "via": "nginx -> api -> postgres",
        "visits": count,
        "last_visit_id": visit_id,
    }


@app.get("/health")
def health():
    conn = connect()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT 1;")
            cur.fetchone()
    finally:
        conn.close()
    return {"status": "ok"}

import os
import time

import psycopg2
import uvicorn
from fastapi import FastAPI

app = FastAPI()
DATABASE_URL = os.environ["DATABASE_URL"]


def connect():
    return psycopg2.connect(DATABASE_URL)


def wait_for_db():
    last_error = None
    for _ in range(30):
        try:
            conn = connect()
            conn.close()
            return
        except psycopg2.OperationalError as exc:
            last_error = exc
            time.sleep(1)
    raise RuntimeError(f"Postgres never became ready: {last_error}")


@app.get("/")
def index():
    conn = connect()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            version = cur.fetchone()[0]
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
        "message": "FastAPI talked to Postgres over the Compose network",
        "visits": count,
        "last_visit_id": visit_id,
        "postgres": version,
    }


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    wait_for_db()
    conn = connect()
    with conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS visits (
                id SERIAL PRIMARY KEY,
                created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
            );
            """
        )
    conn.commit()
    conn.close()
    uvicorn.run(app, host="0.0.0.0", port=8000)

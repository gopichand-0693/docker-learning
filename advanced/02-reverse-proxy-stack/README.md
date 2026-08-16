# 02 — Reverse proxy stack

The browser should not talk to Flask or Postgres. It talks to **nginx**. nginx talks to **api**. api talks to **db**.

```text
localhost:8080  -->  nginx  -->  api:8000  -->  db:5432
                     frontend     frontend        backend
                                  backend
```

`depends_on: condition: service_healthy` is the fix for the race you met in intermediate lesson 1. nginx starts only after the API healthcheck passes; the API starts only after `pg_isready`.

## Run

```bash
cd docker-learning/advanced/02-reverse-proxy-stack
docker compose up --build
```

```bash
curl -s http://localhost:8080
curl -s http://localhost:8080/health
```

There is no host port on `api` or `db`. This should fail:

```bash
curl -s http://localhost:8000
```

## Watch startup order

```bash
docker compose ps
```

`db` becomes healthy, then `api`, then `nginx`. If you `compose up` without health conditions, nginx can boot, proxy to a dead API, and return 502 until things catch up.

## Networks

```bash
docker compose exec nginx wget -qO- http://api:8000/health
docker compose exec nginx wget -qO- http://db:5432 || true
```

The first call should return JSON. The second should fail: nginx is not on `backend`. That is isolation, not an accident.

## Postgres init script

`db/init.sql` is mounted into `/docker-entrypoint-initdb.d/`. Postgres runs those files **only on an empty data volume**. If you change the SQL after the first boot, you must `docker compose down -v` to start clean.

## Check yourself

- Why is `api` missing a `ports:` section?
- What is the difference between `depends_on: api` and `depends_on: api: condition: service_healthy`?
- Who is allowed to resolve the hostname `db`?

Next: [`../03-prod-compose`](../03-prod-compose/README.md)

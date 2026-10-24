# 01 — Compose: web + database

Typing `docker run` twice, with matching networks and env vars, gets old. **Compose** is a YAML file that starts the whole stack.

This lesson: a FastAPI service that writes visit counts into Postgres. FastAPI reaches Postgres at hostname `db` — the **service name**.

## Start

```bash
cd docker-learning/intermediate/01-compose-web-db
docker compose up --build
```

`--build` rebuilds the web image when the Dockerfile or app changes.

Wait until both services look healthy, then:

```bash
curl -s http://localhost:8000
curl -s http://localhost:8000
```

`visits` should go 1, then 2. Refresh the browser if you prefer.

## What Compose did for you

1. Built `web` from the local Dockerfile.
2. Pulled `postgres:16-alpine`.
3. Created a **private network** and attached both containers.
4. Registered DNS: inside that network, `db` resolves to the Postgres container.
5. Mounted a named volume on Postgres so data survives `compose down` **without** `-v`.

Open `docker-compose.yml` next to this file. The hostname in `DATABASE_URL` is `db`, not `localhost`. `localhost` inside `web` means the web container itself — Postgres is a sibling, not the same process.

## Useful commands

```bash
docker compose ps
docker compose logs -f web
docker compose exec db psql -U app -d appdb -c "SELECT COUNT(*) FROM visits;"
docker compose down          # stop and remove containers; keep the volume
docker compose down -v       # also delete pgdata (visits reset to zero)
```

`depends_on` only waits until the **container starts**, not until Postgres is ready to accept connections. That is why `app.py` retries. Advanced lesson 2 waits on a real healthcheck.

## Check yourself

- Why is the database host `db` and not `localhost`?
- What does the `pgdata` volume protect you from?
- What is the difference between `compose down` and `compose down -v`?

Next: [`../02-custom-networks`](../02-custom-networks/README.md)

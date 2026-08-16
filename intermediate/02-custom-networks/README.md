# 02 — Custom networks

Compose already gives you a default network. Custom networks let you **split** who can talk to whom.

This stack:

```text
your browser  -->  ping:8001  -->  pong   (internal only)
                     |                |
                  frontend         backend
                  + backend
```

- `ping` sits on both networks and is published to localhost.
- `pong` sits only on `backend`, and that network is `internal: true` — no outbound internet, no host ports.

## Run

```bash
cd docker-learning/intermediate/02-custom-networks
docker compose up --build
```

```bash
curl -s http://localhost:8001
```

You should see JSON from `ping` that **includes** a nested `pong` object. That nested call used Docker DNS: hostname `pong`.

This should fail (pong is not published):

```bash
curl -s http://localhost:8000
```

## Inspect

```bash
docker compose exec ping python -c "import urllib.request; print(urllib.request.urlopen('http://pong:8000').read())"
docker network ls
docker inspect docker-learning-intermediate-02-custom-networks-backend
```

The inspect output lists which containers are attached. DNS names are the service names.

## Why bother

In a real app, Postgres and Redis belong on an internal network. Only the reverse proxy (or the API) is published. Lesson 2 of advanced does that with nginx.

## Check yourself

- What hostname does `ping` use to call `pong`?
- Why can your browser reach `ping` but not `pong`?
- What does `internal: true` change?

Next: [`../03-env-files`](../03-env-files/README.md)

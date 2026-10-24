# 01 — A hardened image

The FastAPI / uvicorn `--reload` workflow and `USER root` are fine for learning. They are not fine for anything you expose.

This image:

- installs deps in a throwaway **builder** stage
- runs as UID **1000**, not root
- uses **uvicorn** with workers
- declares a **HEALTHCHECK** against `/health`

## Build and run

```bash
cd docker-learning/advanced/01-hardened-image
docker build -t hardened-api .
docker run --rm -p 8000:8000 --name hardened hardened-api
```

```bash
curl -s http://localhost:8000
curl -s http://localhost:8000/health
```

`user` in the JSON should be `1000`, not `0`.

## Prove it is not root

```bash
docker exec hardened id
docker exec hardened whoami
```

`whoami` may print `appuser`. `id` should show `uid=1000`.

Try writing to `/app` as that user — it should fail if you attempt to create a file you do not own. That is the point.

## Watch the healthcheck

Wait ~15 seconds, then:

```bash
docker inspect --format='{{json .State.Health}}' hardened | python3 -m json.tool
```

`Status` should be `"healthy"`. Compose in the next lesson waits on that before starting nginx.

## Why each piece exists

| Piece | If you skip it |
|---|---|
| Non-root `USER` | A breakout in the app is already root in the container |
| uvicorn workers | `--reload` is a single-process dev loop, not for production |
| `HEALTHCHECK` | Orchestrators cannot tell "process up" from "app hung" |
| Multi-stage | Build tools and pip cache ride along into prod |
| `PYTHONUNBUFFERED=1` | Logs sit in a buffer and you debug blind |

## Check yourself

- Why bind to `0.0.0.0` and not `127.0.0.1` inside a container?
- Who runs the `HEALTHCHECK` command?
- What would `docker run --user 0` do to this image, and why is that a smell in production?

Next: [`../02-reverse-proxy-stack`](../02-reverse-proxy-stack/README.md)

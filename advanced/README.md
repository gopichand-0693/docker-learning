# Advanced

Goal: ship images and Compose files that look closer to production.

| # | Folder | You will learn |
|---|---|---|
| 1 | [`01-hardened-image`](01-hardened-image/README.md) | Non-root user, gunicorn, `HEALTHCHECK`, multi-stage |
| 2 | [`02-reverse-proxy-stack`](02-reverse-proxy-stack/README.md) | nginx in front, `depends_on` + health, split networks |
| 3 | [`03-prod-compose`](03-prod-compose/README.md) | Restart, logs, memory limits, `read_only`, profiles |

None of this replaces Kubernetes. It is the Docker layer you should get right first.

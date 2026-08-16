# 03 — Production Compose habits

The YAML in this lesson is the checklist people skip: restart policy, log rotation, memory caps, a read-only root filesystem, and an optional **profile** for extra tools.

The app is a hit counter in Redis. Small on purpose — the Compose file is the curriculum.

## Run the default stack

```bash
cd docker-learning/advanced/03-prod-compose
docker compose up --build
```

```bash
curl -s http://localhost:8000
curl -s http://localhost:8000
```

`hits` should increment. Redis Commander is **not** running yet.

## Profile: extra services for development

```bash
docker compose --profile dev up --build
```

Open http://localhost:8081 for Redis Commander. Profiles keep debug UIs out of production without a second repo.

## Production overlay

Compose merges files left to right. Later files win.

```bash
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build
```

That overlay:

- un-publishes the API (`ports: !reset []`) so the host has no direct door
- turns on Redis AOF and a named volume
- raises resource limits a bit
- uses `restart: always`

You would put nginx or a cloud load balancer in front. Lesson 2 already showed that shape.

## What the knobs mean

| Knob | Why |
|---|---|
| `restart: unless-stopped` | Come back after a crash or a Docker daemon reboot, unless you stopped it on purpose |
| `logging.max-size` | A chatty app will not fill the disk |
| `deploy.resources.limits` | One leaky process cannot eat the machine |
| `read_only: true` | The container cannot write its own OS files |
| `tmpfs: /tmp` | The app still gets a writable temp dir, in memory |
| `no-new-privileges` | Blocks `sudo`-style privilege escalation inside the container |
| `profiles` | Optional sidecars, same file, not started by default |

`read_only` will break apps that write to `/app` or `/var`. That is useful: it forces you to put state in volumes or tmpfs on purpose.

## Confirm limits and health

```bash
docker compose ps
docker stats --no-stream
docker inspect --format='{{.HostConfig.Memory}} {{.HostConfig.ReadonlyRootfs}}' $(docker compose ps -q api)
```

Memory is in bytes. `ReadonlyRootfs` should be `true`.

## Check yourself

- What is the difference between `restart: unless-stopped` and `restart: always`?
- Why does `read_only` need `tmpfs: /tmp`?
- When do you use `--profile`, and when do you use a second Compose overlay file?

You are done with the path. Go back to a real project and write a Dockerfile that copies `requirements.txt` first, runs as non-root, and has a healthcheck. That is the whole course in one sentence.

# 04 — Ports and volumes

Two facts that surprise people:

1. A process listening on port 8000 **inside** a container is invisible on your Mac until you **publish** the port.
2. Files written inside a container die with the container unless you mount a **volume**.

## Build

```bash
cd docker-learning/basic/04-volumes-and-ports
docker build -t notes-app .
```

## Publish a port

```bash
docker run --rm -p 8000:8000 --name notes notes-app
```

`-p 8000:8000` means `host:container`.

Open http://localhost:8000 then http://localhost:8000/add?text=hello

`EXPOSE 8000` in the Dockerfile is documentation. Without `-p`, the browser still cannot reach it.

Leave this terminal running, or use `-d` and `docker stop notes` later.

## Prove data is ephemeral

In another terminal:

```bash
curl -s "http://localhost:8000/add?text=first"
curl -s http://localhost:8000
```

Stop the container (`Ctrl+C` or `docker stop notes`). Run it again **without** a volume:

```bash
docker run --rm -p 8000:8000 --name notes notes-app
```

Visit `/` — the note is gone. The old container's filesystem was deleted.

## Named volume (Docker manages the disk)

```bash
docker run --rm -p 8000:8000 -v notes-data:/data --name notes notes-app
```

Add a note, stop the container, start it again with the **same** `-v notes-data:/data`. The note survives.

```bash
docker volume ls
docker volume inspect notes-data
```

## Bind mount (your folder, live)

```bash
mkdir -p data
docker run --rm -p 8000:8000 -v "$(pwd)/data:/data" --name notes notes-app
```

Add a note, then open `./data/notes.txt` in your editor. That file is on **your** disk. This is how you live-edit code in development.

| Mount | Use it for |
|---|---|
| Named volume `-v name:/path` | Databases, data you do not need to edit |
| Bind mount `-v /host/path:/path` | Source code, config you want to see in the editor |

## Cleanup

```bash
docker stop notes 2>/dev/null
docker volume rm notes-data
```

## Check yourself

- What do the two numbers in `-p 8000:8000` mean?
- Why did the note vanish without a volume?
- When would you pick a bind mount over a named volume?

Basic is done. Next: [`../../intermediate`](../../intermediate/README.md)

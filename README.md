# Docker, hands-on

Learn Docker by **running things**, not by memorizing flags.

Work through the folders in order. Each lesson has a `README.md` that explains the idea, then exact commands to try.

```
docker-learning/
  basic/          images, containers, Dockerfile, layers, ports, volumes
  intermediate/   Compose, networking, env files, multi-stage builds
  advanced/       non-root images, healthchecks, nginx proxy, production Compose
```

## What you need

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Mac / Windows) or Docker Engine (Linux)
- A terminal

Check that Docker works:

```bash
docker version
docker run --rm hello-world
```

`--rm` deletes the container when it exits. You still have the image.

## Mental model (read this once)

| Word | What it is |
|---|---|
| **Image** | A frozen snapshot: OS files + your app. Like a class. |
| **Container** | A running instance of an image. Like an object. |
| **Dockerfile** | The recipe that builds an image. |
| **Registry** | Where images live (Docker Hub is the public one). |
| **Volume** | Disk that outlives the container. |
| **Network** | How containers find each other by name. |
| **Compose** | A YAML file that starts several containers together. |

A container is **not** a tiny VM. It shares the host kernel. It is a process with its own filesystem, network, and process list.

## How to use this repo

1. Open `basic/README.md` and finish every lesson there.
2. Then `intermediate/`, then `advanced/`.
3. When something breaks, that is the lesson. Read the error; do not skip ahead.

Start here: [`basic/`](basic/README.md)

When this path is done, related courses (separate repos) with the same shape:

- **kubernetes-learning** — schedule the images you just learned to build
- **terraform-learning** — create the cloud around them (GCP)

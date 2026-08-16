# 01 — Hello, container

You are not writing a Dockerfile yet. You are using images that already exist on Docker Hub.

## Image vs container

- An **image** is the blueprint (`python:3.12-slim`).
- A **container** is one running copy of that blueprint.

You can start ten containers from one image. Deleting a container does not delete the image.

## 1. Run a one-shot command

```bash
docker run --rm python:3.12-slim python -c "print('hello from a container')"
```

What happened:

1. Docker looked for `python:3.12-slim` on your machine.
2. If missing, it **pulled** it from Docker Hub.
3. It started a container, ran that Python one-liner, printed the line, then `--rm` threw the container away.

## 2. Land inside a container

```bash
docker run -it --rm python:3.12-slim bash
```

- `-i` keeps STDIN open
- `-t` gives you a terminal

Inside the container, try:

```bash
whoami
cat /etc/os-release
python --version
exit
```

This Linux is **not** your Mac. It is the filesystem baked into the image.

## 3. A container that stays up

```bash
docker run -d --name web alpine sleep 1000
```

- `-d` = detached (background)
- `--name web` = a name you can type instead of a random id
- `sleep 1000` = the process Docker watches. When it exits, the container stops.

```bash
docker ps
docker logs web
docker exec -it web sh
# inside: hostname ; ls /
exit
docker stop web
docker rm web
```

`docker exec` runs a **second** process in an already-running container. It is not a new container.

## 4. See what you have

```bash
docker ps -a          # containers, including stopped
docker images         # images on disk
docker inspect web    # JSON dump of one container (if it still exists)
```

## Commands worth memorizing

```text
docker run      start a new container from an image
docker ps       list running containers   (-a = include stopped)
docker logs     stdout/stderr of a container
docker exec     run a command in a running container
docker stop     send SIGTERM, then SIGKILL
docker rm       delete a container
docker rmi      delete an image
docker pull     download an image without running it
```

## Check yourself

- Can you explain the difference between `docker run` and `docker exec`?
- What does `--rm` do?
- If you `docker rm` a container, is the image gone?

Next: [`../02-first-dockerfile`](../02-first-dockerfile/README.md)

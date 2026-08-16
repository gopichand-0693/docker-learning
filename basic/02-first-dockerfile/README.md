# 02 — Your first Dockerfile

A Dockerfile is a recipe. `docker build` cooks it into an **image**. `docker run` starts a **container** from that image.

## The six instructions you will see everywhere

| Instruction | Meaning |
|---|---|
| `FROM` | Base image. Everything else stacks on top. |
| `WORKDIR` | `cd` for the rest of the file. Created if missing. |
| `COPY` | Copy files from your project into the image. |
| `RUN` | Run a command **at build time** (install packages, compile). |
| `CMD` | Default command **at run time**. Easy to override. |
| `ENTRYPOINT` | Command that is harder to override. Often used with `CMD` as args. |

`RUN` happens while building. `CMD` happens when the container starts. Mixing them up is the most common beginner bug.

## Build

From this folder:

```bash
cd docker-learning/basic/02-first-dockerfile

docker build -t hello-app .
```

- `-t hello-app` tags the image with a name you can remember
- `.` is the **build context** — the folder Docker may copy files from

Open `Dockerfile` and `.dockerignore` and read every comment.

## Run

```bash
docker run --rm hello-app
```

You should see two lines of text, then the container exits. That is correct: `app.py` prints and finishes, so the container's main process exits.

Override `CMD` without rebuilding:

```bash
docker run --rm hello-app python -c "print('I replaced CMD')"
```

## Look at the layers

```bash
docker history hello-app
```

Each Dockerfile instruction is a **layer**. Next lesson is about why that matters.

## Check yourself

- What is the difference between `RUN` and `CMD`?
- Why is `.dockerignore` useful even for a one-file app?
- What does the `.` in `docker build -t hello-app .` mean?

Next: [`../03-layers-and-cache`](../03-layers-and-cache/README.md)

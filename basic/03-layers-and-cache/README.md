# 03 — Layers and the build cache

Docker builds an image as a stack of layers. If an instruction's **input did not change**, Docker reuses the cached layer and skips the work.

Cache is invalidated from the first changed instruction **downward**. Order is the whole game.

## The rule

Copy the files that change **least often** first.

1. Base image
2. Dependency files (`requirements.txt`, `package.json`)
3. `RUN pip install` / `npm ci`
4. Your source code (changes all day)

## Feel the difference

First build of each file is slow — that is expected (pip + base image).

```bash
cd docker-learning/basic/03-layers-and-cache

docker build -f Dockerfile.slow -t cache-slow .
docker build -f Dockerfile.fast -t cache-fast .
```

Now edit `app.py` (change the print text) and rebuild **both**:

```bash
docker build -f Dockerfile.slow -t cache-slow .
docker build -f Dockerfile.fast -t cache-fast .
```

Watch the output:

- **slow**: `COPY . .` changed, so `RUN pip install` runs again.
- **fast**: `COPY requirements.txt` is unchanged, so `pip install` says `CACHED`. Only `COPY app.py` is new.

That is why every serious Dockerfile copies lockfiles before source.

## `--no-cache-dir` on pip

That flag is about **pip's download cache inside the image**, not Docker's layer cache. It keeps the image smaller. Different cache.

## Check yourself

- Why does `COPY . .` before `pip install` hurt you?
- What happens to later layers if you change one early `RUN` line?

Next: [`../04-volumes-and-ports`](../04-volumes-and-ports/README.md)

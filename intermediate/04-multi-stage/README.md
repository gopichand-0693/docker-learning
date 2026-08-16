# 04 — Multi-stage builds

Build tools do not belong in the image you ship. A **multi-stage** Dockerfile uses one stage to install/compile, then copies **only the result** into a thin runtime image.

This lesson uses a Python virtualenv as the "compiled artifact". The same pattern is how Go, Rust, and Node production images stay small.

## Build both

```bash
cd docker-learning/intermediate/04-multi-stage

docker build -t app-single -f Dockerfile.single .
docker build -t app-multi .
```

## Compare size

```bash
docker images app-single app-multi
```

`app-multi` should be the same size or slightly smaller here (the demo dependency is tiny). The win is the **shape**: compilers, `gcc`, npm, Maven, cargo never land in `runtime`.

On a compiled language the difference is huge. The pattern is what you are learning, not the megabytes of `six`.

## Run the multi-stage image

```bash
docker run --rm -p 8003:8000 app-multi
curl -s http://localhost:8003
```

## Read the Dockerfile

- `AS builder` names the first stage.
- `COPY --from=builder /venv /venv` is the only thing that crosses the boundary.
- The final image's `FROM` is what you actually run. Earlier stages are build cache.

You can also stop at a stage while debugging:

```bash
docker build --target builder -t app-builder .
```

## Check yourself

- What does `COPY --from=builder` copy, and what does it leave behind?
- Why is `CMD` in the last stage, not the first?

Intermediate is done. Next: [`../../advanced`](../../advanced/README.md)

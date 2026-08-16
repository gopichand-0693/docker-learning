# 03 — Environment files (config is not code)

Images should be **the same** in every environment. What changes is config: URLs, tokens, log level.

Three layers, highest wins:

1. `environment:` in Compose (or `-e` on `docker run`)
2. `env_file:`
3. `ENV` in the Dockerfile (avoid for secrets)

This lesson's Compose file **overrides** `APP_MESSAGE` on purpose so you can see the order.

## Setup

```bash
cd docker-learning/intermediate/03-env-files
cp .env.example .env
```

`.env` is gitignored. `.env.example` is the template you commit.

## Run

```bash
docker compose up --build
curl -s http://localhost:8002
```

You should see `hello from docker-compose.yml (overrides .env)` and a truncated token from `.env`.

## Change config without rebuilding

Edit `.env`:

```text
API_TOKEN=abcd1234secret
```

Recreate the container (no `--build` needed):

```bash
docker compose up -d
curl -s http://localhost:8002
```

`token_preview` should start with `abcd`.

Comment out the `APP_MESSAGE` line under `environment:` in `docker-compose.yml`, then `docker compose up -d` again. The message should fall back to the `.env` value.

## Rules

- Never `COPY .env` into an image.
- Never `ENV API_TOKEN=...` in a Dockerfile you will push.
- Compose automatically loads a file named `.env` in the project directory for **variable substitution** in the YAML (`${POSTGRES_PASSWORD}`). That is separate from `env_file:` which injects vars **into the container**. Both can exist. Read the Compose file twice if that sentence felt dense.

## Check yourself

- Why rebuild is unnecessary after an env change?
- Which wins: `environment:` or `env_file:`?
- Why is `.env.example` committed and `.env` not?

Next: [`../04-multi-stage`](../04-multi-stage/README.md)

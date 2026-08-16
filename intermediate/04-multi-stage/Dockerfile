# Stage 1: install deps into a virtualenv. This layer can be fat
# (compilers, headers). It is discarded after the copy below.
FROM python:3.12-slim AS builder
WORKDIR /app
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: only the venv + app. No pip cache, no build tools.
FROM python:3.12-slim AS runtime
WORKDIR /app
COPY --from=builder /venv /venv
ENV PATH="/venv/bin:$PATH"
COPY app.py .
EXPOSE 8000
CMD ["python", "app.py"]

FROM python:3.12-slim AS builder
WORKDIR /app
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12-slim AS runtime
WORKDIR /app

# A dedicated UID. The process should not be root.
RUN useradd --create-home --uid 1000 --shell /usr/sbin/nologin appuser

COPY --from=builder --chown=appuser:appuser /venv /venv
COPY --chown=appuser:appuser app.py .

ENV PATH="/venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

USER appuser
EXPOSE 8000

# Runs inside the container on a timer. Unhealthy containers can be
# restarted by Compose/Swarm/K8s. Slim images often lack curl, so use Python.
HEALTHCHECK --interval=10s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health')"

# Production server, not Flask's built-in one.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "app:app"]

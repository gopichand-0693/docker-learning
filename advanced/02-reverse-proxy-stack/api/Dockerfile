FROM python:3.12-slim AS builder
WORKDIR /app
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12-slim AS runtime
WORKDIR /app
RUN useradd --create-home --uid 1000 --shell /usr/sbin/nologin appuser
COPY --from=builder --chown=appuser:appuser /venv /venv
COPY --chown=appuser:appuser app.py .
ENV PATH="/venv/bin:$PATH" PYTHONUNBUFFERED=1
USER appuser
EXPOSE 8000
HEALTHCHECK --interval=5s --timeout=3s --start-period=10s --retries=5 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health')"
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]

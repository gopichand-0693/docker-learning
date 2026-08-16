FROM python:3.12-slim
WORKDIR /app
COPY app.py .
# No ENV for secrets here. Config belongs at *run* time.
EXPOSE 8000
CMD ["python", "app.py"]

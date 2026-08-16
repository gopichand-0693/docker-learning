# Every Dockerfile starts FROM an existing image.
# python:3.12-slim = official Python, Debian-based, smaller than the full image.
FROM python:3.12-slim

# Directory inside the image. Later COPY/RUN/CMD are relative to this.
WORKDIR /app

# Copy only this file from your machine into the image.
COPY app.py .

# Default process. Exec form (JSON array) is preferred:
# it is not wrapped in a shell, so signals (docker stop) reach Python.
CMD ["python", "app.py"]

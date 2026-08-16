FROM python:3.12-slim
WORKDIR /app
COPY app.py .

# Documents which port the process listens on. Does NOT publish it to your Mac.
# Publishing is `docker run -p`.
EXPOSE 8000

CMD ["python", "app.py"]

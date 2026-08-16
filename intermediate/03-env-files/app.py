import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

PORT = int(os.environ.get("PORT", "8000"))
APP_MESSAGE = os.environ.get("APP_MESSAGE", "unset")
API_TOKEN = os.environ.get("API_TOKEN", "unset")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps(
            {
                "message": APP_MESSAGE,
                "token_preview": API_TOKEN[:4] + "..." if API_TOKEN != "unset" else "unset",
                "hint": "Change .env and recreate the container. Do not rebuild.",
            }
        ).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        print(format % args)


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
import urllib.request

PING_PORT = int(os.environ.get("PORT", "8000"))
PONG_URL = os.environ.get("PONG_URL", "http://pong:8000/")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        with urllib.request.urlopen(PONG_URL, timeout=3) as response:
            pong = json.loads(response.read().decode())
        body = json.dumps(
            {
                "from": "ping",
                "message": "I reached pong by Docker DNS",
                "pong": pong,
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
    print(f"ping listening on {PING_PORT}, calling {PONG_URL}", flush=True)
    HTTPServer(("0.0.0.0", PING_PORT), Handler).serve_forever()

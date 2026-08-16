from pathlib import Path
from urllib.parse import parse_qs
from wsgiref.simple_server import make_server

DATA = Path("/data/notes.txt")
PORT = 8000


def add_note(text):
    DATA.parent.mkdir(parents=True, exist_ok=True)
    with DATA.open("a", encoding="utf-8") as file:
        file.write(text + "\n")
    return f"Added: {text}\n".encode()


def show_notes():
    notes = DATA.read_text(encoding="utf-8") if DATA.exists() else "(no notes yet)\n"
    return (
        "<h1>Notes inside the container</h1>"
        f"<pre>{notes}</pre>"
        "<p>Add a note: <code>/add?text=hello</code></p>"
    ).encode()


def app(environ, start_response):
    """Called by the server on every browser request. You pass this function in below."""
    path = environ.get("PATH_INFO", "/")
    query = parse_qs(environ.get("QUERY_STRING", ""))

    if path == "/add":
        body = add_note(query.get("text", ["empty"])[0])
        content_type = "text/plain; charset=utf-8"
    else:
        body = show_notes()
        content_type = "text/html; charset=utf-8"

    start_response(
        "200 OK",
        [
            ("Content-Type", content_type),
            ("Content-Length", str(len(body))),
        ],
    )
    return [body]


if __name__ == "__main__":
    print(f"Listening on 0.0.0.0:{PORT}", flush=True)
    # This is the call site: each GET runs app(...) → add_note or show_notes.
    make_server("0.0.0.0", PORT, app).serve_forever()

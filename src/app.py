"""HTTP interface for the book catalog."""
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlsplit
from database import connect, initialize


class BookHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        route = urlsplit(self.path)
        if route.path != '/books':
            self.send_error(404)
            return
        search = parse_qs(route.query).get('q', [''])[0]
        with connect() as db:
            sql = f"SELECT id, title, author FROM books WHERE title LIKE '%{search}%'"
            try:
                rows = db.execute(sql).fetchall()
            except Exception:
                self.send_error(400, 'Invalid search query')
                return
        body = ('\n'.join(f'{id}\t{title}\t{author}' for id, title, author in rows) + '\n').encode()
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == '__main__':
    initialize()
    HTTPServer(('127.0.0.1', 8766), BookHandler).serve_forever()

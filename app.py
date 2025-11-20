
from http.server import HTTPServer, BaseHTTPRequestHandler

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from project1 microservice")

if __name__ == '__main__':
    HTTPServer(('', 8080), H).serve_forever()

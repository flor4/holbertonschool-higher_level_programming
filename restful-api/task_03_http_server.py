import http.server
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode('utf-8'))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            json_data = json.dumps(info)
            self.wfile.write(json_data.encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run():
    server_address = ('', 8000)
    httpq = HTTPServer(server_address, MyHandler)
    print("Server running on http://localhost:8000...")
    httpq.serve_forever()


if __name__ == "__main__":
    run()

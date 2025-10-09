import http.server
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

"""
Set up a basic web server using the http.server module.
Handle different types of HTTP requests (GET, POST, etc.).
Serve JSON data in response to specific endpoints.
"""


class MyHandler(BaseHTTPRequestHandler):
    """ My handler"""
    def do_GET(self):
        """return void"""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write
            (bytes("Hello, this is a simple API".encode("utf-8")))

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
            self.wfile.write(bytes(json_data.encode('utf-8')))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("OK".encode('utf-8'))

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            json_data = json.dumps(info)
            self.wfile.write(bytes(json_data.encode('utf-8')))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("Endpoint not found".encode('utf-8')))


def main():
    """
    main - Main function
    Return: Void
    """
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print("Server running on http://localhost:8000...")
    httpd.serve_forever()


if __name__ == "__main__":
    main()

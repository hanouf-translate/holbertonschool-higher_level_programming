#!/usr/bin/python3
"""
Module that implements a simple HTTP server using http.server
to handle different endpoints and serve plain text or JSON data.
"""

import json
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    Custom HTTP request handler that routes GET requests to specific endpoints
    and returns appropriate text or JSON responses.
    """

    def do_GET(self):
        """
        Handles HTTP GET requests and routes based on self.path.
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))
            
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"OK")
            
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    """
    Runs the HTTP server on localhost and the specified port.
    """
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print("Starting httpd server on port {}...".format(port))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("Server stopped.")


if __name__ == "__main__":
    run()
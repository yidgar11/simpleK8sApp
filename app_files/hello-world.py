from http.server import BaseHTTPRequestHandler, HTTPServer


# Define a request handler
class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Handle GET request for /hello
        if self.path == "/":
            self.send_response(200)  # HTTP status 200: OK
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Welcome")
        elif self.path == "/hello":
            self.send_response(200)  # HTTP status 200: OK
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"hello world")
        else:
            # Return 404 for other paths
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Not Found")


# Set up and start the server
def run_server():
    server_address = ("", 9009)  # Listen on all interfaces, port 9009
    httpd = HTTPServer(server_address, SimpleRequestHandler)
    print("Server running on port 9009...")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()

from http.server import HTTPServer, BaseHTTPRequestHandler

# in your browser, go to 10.235.209.94:1932
HOST = "10.235.209.94"
PORT = 1932

HTML_FILE = "<html><body>Hello World!</body></html>"

class FirehouseHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes(HTML_FILE, "utf-8"))


server = HTTPServer((HOST, PORT), FirehouseHTTP)
print("Server now running...")
server.serve_forever()
server.server_close()

print("Server stopped")

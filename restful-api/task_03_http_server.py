#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOSTNAME = "localhost"
PORT = 8000


class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/data':
            data = {
                'name': 'John',
                'age': '30',
                'city': 'New York'
            }

            json_data = json.dumps(data)

            self.send_response(200)

            self.send_header('Content-type', 'application/json')
            self.end_headers()

            self.wfile.write(json_data.encode('utf-8'))
        elif self.path == '/status':

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'OK')

        else:

            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'Endpoint not found')


if __name__ == '__main__':

    httpd = HTTPServer((HOSTNAME, PORT), SimpleRequestHandler)

    print(f'Starting server on port 8000...')
    server.serve_forever()

######################################################################################################
# Script:       Info Gather [PY]
# Description:  This script starts an HTTP server that listens for POST requests, gathers data from
#               the client (such as username, hostname, OS, etc.), and appends it to a file named
#               curl_data.txt. The server can be run on a specified port or default to port 80.
#
# Execution Examples:
#   python3 info_gather.py 8080    # Run the server on port 8080
#   python3 info_gather.py         # Run the server on the default port 80
######################################################################################################

import json
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime
import pytz

class RequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, message):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(message + "\n", "utf8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        # Add local date, time, and timezone to the data
        current_time = datetime.now(pytz.timezone('UTC')).astimezone().strftime('%Y-%m-%d %H:%M:%S %Z%z')
        data['recorded_at'] = current_time

        with open('curl_data.txt', 'a') as file:
            file.write(json.dumps(data) + '\n')

        self._send_response("Info submitted, thank you!\n")

def run(server_class=HTTPServer, handler_class=RequestHandler, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}')
    httpd.serve_forever()

if __name__ == "__main__":
    port = 80  # Default port
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Invalid port number. Using default port 80.")

    run(port=port)

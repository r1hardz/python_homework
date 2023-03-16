import socket
import re

MAX_CHARACTERS = 1800

url = input("Enter a URL || URL example: [https://example.com]: ")

if not re.match(r'^https?://', url):
    print("Error: Invalid URL")
    exit()

try:
    hostname = url.split("/")[2]
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    sock.connect((hostname, 80))
    request = f"GET {url} HTTP/1.0\r\nHost: {hostname}\r\n\r\n"
    sock.send(request.encode())

    response = sock.recv(MAX_CHARACTERS).decode()
    headers, body = response.split("\r\n\r\n", 1)
    print(f"Headers:\n{headers}\n\nBody:\n{body}\n")
    print(f"Number of characters received: {len(response)}")
except (socket.gaierror, ValueError, socket.timeout) as e:
    print(f"Error: {e}")
finally:
    sock.close()

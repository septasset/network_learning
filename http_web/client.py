from socket import *
encoding = 'utf-8'

s = socket()
host = 'localhost'
port = 8888
s.connect((host, port))

head = """GET /index.html HTTP/1.1\r
Host: localhost:8888\r
Connection: close\r
User-agent: Chrome\r
\r
"""
s.send(head.encode(encoding))

response_header = s.recv(1024)
response_data = s.recv(1024)
if response_header:
    print(response_header.decode())
    if response_data:
        print(response_data.decode())
# s.close()

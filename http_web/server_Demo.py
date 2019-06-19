from socket import *

s = socket(family=AF_INET, type=SOCK_STREAM)

host = 'localhost'
port = 8888
s.bind((host, port))

s.listen(5)
while True:
    conn, address = s.accept()
    with conn:
        print('Connected by:', address)
        # while True:
        data = conn.recv(1024)
            # if not data:break
        print('Received from client:', data.decode('utf-8'))
        conn.sendall("hello".encode('utf-8'))
        conn.close()

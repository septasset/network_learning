from socket import *

s = socket()
host = 'localhost'
port = 8888

s.connect((host, port))
s.sendall('Client greeting!'.encode('utf-8'))
print('Received from server:',s.recv(1024).decode('utf-8'))
s.close()

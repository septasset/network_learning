from socket import *
encoding = 'utf-8'

s = socket(family=AF_INET, type=SOCK_STREAM)

host = 'localhost'
port = 8888
s.bind((host, port))
s.listen(1)

# blocked when no connection
conn, addr = s.accept()

# while True:
if True:
    # try receive at max 1KB
    data= conn.recv(1024)
    # request is a GET http message
    request = data.decode().split('\r\n')[0]
    filename = request.split()[1]
    print('Request paga:', filename)
    try:
        file = open('.'+filename, encoding='utf-8')
        file_data = file.read()
        # print(file_data)

        # respond with data
        header = """HTTP/1.1 200 OK\r\n\r\n"""
        conn.send(header.encode(encoding))
        conn.sendall(file_data.encode(encoding))

    except IOError:
        # respond with failure
        header = """HTTP/1.1 404 NOT FOUND\r\n\r\n"""
        conn.send(header.encode(encoding))

    finally:
        s.close()

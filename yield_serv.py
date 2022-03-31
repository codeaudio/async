import socket
from select import select
to_read = {}
to_write = {}
tasks = []
def server():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serv.bind(('localhost', 5005))
    serv.listen()
    while True:
        yield 'read', serv
        client, addr = serv.accept()
        send_msg(client)


def send_msg(client):
    while True:
        yield 'read', client
        req = client.recv(4096)
        if not req:
            client.close()
        else:
            yield 'write', client
            client.send(str(req).encode())
def event():
    while any([tasks, to_read, to_write]):
tasks.append(server())
server()
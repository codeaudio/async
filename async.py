import socket
from select import select

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv.bind(('localhost', 5005))
serv.listen()

monitor = []


def accept(serv):
    client, addr = serv.accept()
    print(client)
    monitor.append(client)


def send_msg(client):
    req = client.recv(4096)
    if not req:
        client.close()
    else:
        client.send(str(req).encode())


def event():
    while True:
        try:
            ready, _, _ = select(monitor, [], [])
            for sock in ready:
                if sock is serv:
                    accept(sock)
                else:
                    send_msg(sock)
        except:
            for close_sock in range(0, len(monitor)):
                try:
                    if monitor[close_sock].fileno() == -1:
                        monitor.pop(close_sock)
                except:
                    pass


if __name__ == '__main__':
    monitor.append(serv)
    event()

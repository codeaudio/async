import socket
import selectors

selector = selectors.DefaultSelector()


def server():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serv.bind(('localhost', 5005))
    serv.listen()
    selector.register(serv, selectors.EVENT_READ, accept)


def accept(serv):
    client, addr = serv.accept()
    selector.register(client, selectors.EVENT_READ, send_msg)


def send_msg(client):
    req = client.recv(4096)
    if not req:
        client.close()
    else:
        client.send(str(req).encode())


def event():
    while True:
        events = selector.select()
        for key, _ in events:
            callback = key.data
            print(key)
            print(callback, key.fileobj, key.data)
            callback(key.fileobj)


def brakets(n, left, right, res):
    if (left and right) == n:
        print(res)

    else:
        if left < n:
            brakets(n, left + 1, right, res + '(')
        if right < left:
            brakets(n, left, right + 1, res + ')')


print(brakets(3, 0, 0, ''))
if __name__ == '__main__':
    server()
    event()

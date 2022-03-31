import asyncio
import random
import socket
import time
from select import select
from time import sleep
from contextvars import ContextVar
import grequests


serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('localhost', 5003))
serv.listen()
monitor = {}


def accept(serv):
    client, addr = serv.accept()
    monitor[client.fileno()] = client


def send(client):
    resp = client.recv(4096)
    if resp:
        client.send(resp)
    else:
        monitor.pop(client.fileno())
        client.close()


def event():
    while True:
        socket, _, _ = select(monitor.values(), '', '')
        for soc in socket:
            if soc is serv:
                accept(soc)
            else:
                send(soc)


import asyncio


async def cook(order, time_to_prepare):
    print(f'Новый заказ: {order}')
    await asyncio.sleep(0)
    print(order, '- готово')


tasks = [(cook, ('Паста', 1)),
         (cook, ('Пицца', 1)),
         (cook, ('Тост', 1)),
         ]
async def eve():
    while tasks:
        t = tasks.pop(0)
        t = await t[0](*t[1])
        try:

            print(next(t))
            tasks.append(t)

        except:
            pass
asyncio.run(eve())

import asyncio

urls = [
    'http://kennethreitz.com',
    'http://yandex.ru'
]

rs = (grequests.get(u) for u in urls)
t1 = time.time()
print([i for i in grequests.map(rs)])
print(time.time() - t1)

import asyncio


async def count(counter):
    print(f"Количество записей в списке {len(counter)}")
    while True:
        await asyncio.sleep(1 / 1000)
        counter.append(1)


async def print_every_sec(counter):
    while True:
        await asyncio.sleep(1)
        print(f'- 1 секунда прошла. '
              f'Количество записей в списке: {len(counter)}')


async def print_every_5_sec():
    while True:
        await asyncio.sleep(5)
        print(f'---- 5 секунд прошло')


async def print_every_10_sec():
    while True:
        await asyncio.sleep(10)
        print(f'---------- 10 секунд прошло')


async def main():
    counter = list()
    tasks = [
        count(counter),
        print_every_sec(counter),
        print_every_5_sec(),
        print_every_10_sec()
    ]
    await asyncio.gather(*tasks)


import asyncio
import time
from aiohttp import ClientSession, ClientResponseError


async def fetch_url_data(session, url):
    try:
        async with session.get(url, timeout=60) as response:
            resp = await response.read()
    except Exception as e:
        print(e)
    else:
        return resp
    return


async def fetch_async(loop, r):
    url = "https://www.uefa.com/uefaeuro-2020/"
    tasks = []
    async with ClientSession() as session:
        for i in range(r):
            task = asyncio.ensure_future(fetch_url_data(session, url))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
    return responses


l = asyncio.new_event_loop()
asyncio.set_event_loop(l)
for ntimes in [1]:
    start_time = time.time()
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(fetch_async(loop, ntimes))
    # будет выполняться до тех пор, пока не завершится или не возникнет ошибка
    loop.run_until_complete(future)
    responses = future.result()
    print(f'Получено {ntimes} результатов запроса за {time.time() - start_time} секунд')
if __name__ == '__main__':
    monitor[serv.fileno()] = serv
    event()

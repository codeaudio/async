from time import time


def gen(n):
    for i in n:
        yield i


def gen2(n):
    for i in range(n):
        yield i


def gen_filename():
    while True:
        yield f"file{int(time() * 100)}.jpg"

gg = gen('ivan')
ggg = gen2(4)
tasks = [gg, ggg]
while tasks:
    task = tasks.pop(0)
    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except:
        pass

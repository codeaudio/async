import asyncio
import collections
import random
import re
import sys
from collections import defaultdict
from contextvars import ContextVar
from itertools import permutations
from time import time

import grequests as grequests
import requests

increment = ContextVar('inc', default=0)


def inc():
    local_inc = increment.get()
    local_inc += 1
    increment.set(local_inc)
    return local_inc


async def counter(delay):
    while True:
        r = inc()
        await asyncio.sleep(delay)
        print(r, delay)


async def main():
    tasks = [
        counter(1),
        counter(1.5),
        counter(0.35)
    ]
    await asyncio.gather(*tasks)


def simple_num(n):
    nums = [i for i in range(1, n + 1)]
    x = 1
    nums[0] = 0
    nums[1] = 0
    while x < len(nums) - 1:
        flg = False
        for i in range(2, nums[x + 1]):
            if i * i > nums[x + 1]:
                break
            if nums[x + 1] % i == 0:
                flg = True
        if flg is True:
            nums[x + 1] = 0
        x += 1

    return list(nums)


print(simple_num(30))


def fact(n):
    if n == 1:
        return n
    return n * fact(n - 1)


print(fact(5))


def fib(n):
    if n in [1, 2]:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(9))


def find_depth(l, target):
    stack = [l]
    i = 0
    detph = 0
    while stack:
        for element in stack[i]:
            if element == target:
                return [element, detph]
            if isinstance(element, list):
                stack.append(element)
                i += 1
                detph += 1
        i -= 1
        stack.pop(0)


def quic_sort(l):
    def get_pivot():
        return l[random.randint(0, len(l) - 1)]

    if len(l) > 1:
        less = []
        eq = []
        great = []
        pivot = get_pivot()

        for x in l:
            if x > pivot:
                great.append(x)
            elif x == pivot:
                eq.append(x)
            elif x < pivot:
                less.append(x)
        return quic_sort(less) + eq + quic_sort(great)
    return l


class Data:
    def __init__(self, data):
        self.data = data
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        x = self.i
        self.i += 1
        return self.data[x]


def permute_unique(myList):
    per = [[]]
    for i in myList:
        save_perm = []
        for el in per:
            for j in range(len(el) + 1):
                save_perm.append(el[:j] + [i] + el[j:])
        per = save_perm
    return per


def per(l):
    mask = None
    if isinstance(l[0], str):
        mask = l
        l = [i for i in range(len(l))]
        mask = dict(zip(l, mask))
    len_l = len(l) - 1
    k = len_l
    first = l[0]
    result = [l]
    while True:
        if k == first:
            if mask:
                return list(map(lambda x: list(map(lambda y: mask.get(y), x)), result))
            return result
        l = l[1:k + 1] + [l[0]] + l[k + 1:]
        if k == l[k]:
            k -= 1
        elif k != l[k]:
            k = len_l
            result.append(l)


d1 = {'el1': 1, 'el2': 2}
d2 = {'el1': 1, 'el2': 2, 'e5': 5}
d5 = {'el1': 5, 'el9': 0, 'e15': 100, 'el22': 229}
d7 = {'e2': 100, 'el22': 229}
merge_d = {}


def rec_d(l, result: dict):
    for el in l:
        if isinstance(el, dict):
            rec_d(el, result)
        else:
            if el not in result:
                result[el] = l.get(el)
            else:
                result[el] += l.get(el)

    return result


def accum(l: list, left, right):
    return sum(1 for i in range(left, right) if l[i] in ['C', 'G'])


print(accum(list('AGTAGATCAACTGTGTCGTGAGAG'), 0, 6))


def lucky_ticket(n):
    l1 = 0
    l2 = 0
    n = str(n)
    for i in range(len(n)):
        if (i + 1) % 2 == 0:
            l1 += int(n[i])
        else:
            l2 += int(n[i])
    return l1 == l2


t1 = time()
print(lucky_ticket(1))
print(time() - t1)


def is_prime(n):
    nums = [i for i in range(2, n + 1)]
    for el in nums:
        el_sq = (el * el) - 2
        if el_sq > n:
            return list(filter(lambda x: x, nums))
        if el:
            for i in range(el_sq, n, el):
                nums[i] = False


print(is_prime(100))


def get_least_primes_linear(n):
    lp = [0] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
        for p in primes:
            x = p * i
            if (p > lp[i]) or (x > n):
                break
            lp[x] = p
    return primes, lp


print(get_least_primes_linear(10))


from itertools import *

a = (''.join(el) for el in combinations_with_replacement('abcd', 3))
print(*a)

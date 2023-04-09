#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Pool
import random
import time


def Monte_Karlo_integration(l1):
    f, a, b, n = l1
    """
    Расчет интеграла функции `f` на интервале `[a, b]` методом Монте-Карло
    с использованием `n` точек.
    """
    s = 0
    for i in range(n):
        x = random.uniform(a, b)
        s += f(x)
    return (b - a) * s / n


def f(x):
    return x ** 2


if __name__ == '__main__':
    with Pool(16) as p:
        start = time.time()
        l1 = (p.map(Monte_Karlo_integration,
                    [(f, -1, 1, 10000), (f, -1, 1, 10000), (f, -1, 1, 10000), (f, -1, 1, 10000), (f, -1, 1, 10000)]))
        print(sum(l1) / len(l1), time.time() - start)

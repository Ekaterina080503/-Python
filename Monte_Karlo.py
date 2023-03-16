#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scipy import integrate
import random


def Monte_Karlo_integration(f, a, b, n):
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


result = Monte_Karlo_integration(f, 0, 1, 100000)
print(result)  # должно вывести значение приближенного интеграла
v, err = integrate.quad(f, 0, 1)  # считаем интеграл с помощью библиотеки scipy
print(abs(v-result))
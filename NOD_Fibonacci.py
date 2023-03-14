#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Evklid import gcd
from Fibonachy import Fib


def nod_Fibonacci(n, m):
    """Программа будет считать НОД двух чисел Фибоначчи"""
    f1 = Fib().finite_number(n)
    f2 = Fib().finite_number(m)
    return gcd(f1, f2)


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    print(nod_Fibonacci(n, m))
    # обычно получается 1, но 25 и 50 чисел получилось не так

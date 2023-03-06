#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import itertools


class Fib:
    """По объектам этого класса можно итерироваться и получать много чисел Фибоначчи"""

    class _Fib_iter:
        """Внутренний класс — итератор"""

        def __init__(self):
            self.a = 1  # первое число Фибоначчи
            self.b = 1  # второе число Фибоначчи
            self.c = 0  # следующее число Фибоначчи
            self.i = -1  # счётчик

        def __next__(self):
            self.i += 1
            if self.i == 0 or self.i == 1:
                return self.b
            else:
                self.c = self.a + self.b
                self.a = self.b
                self.b = self.c
                return self.b

    def __iter__(self):
        """Создать и вернуть итератор"""
        return Fib._Fib_iter()

    def finite_number(self, n):
        for i in itertools.islice(self, n):
            s = i
        return s


if __name__ == '__main__':
    f = Fib()
    print(f.finite_number(120))
    for i in itertools.islice(f, 120):
        print(i)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numba import int64
from numba.experimental import jitclass
from numba import jit


@jitclass([
    ('x', int64),
    ('a', int64), ('b', int64)
])
class Evklid():
    def __init__(self):
        self.x = 1
        self.a = 7614581656
        self.b = self.x % 4018367011 + 4018367011

    def my_gcd(self) -> int64:
        self.x += 1
        self.b = self.x % 4018367011 + 4018367011
        while self.b != 0:
            self.a, self.b = self.b, self.a % self.b
        return self.a

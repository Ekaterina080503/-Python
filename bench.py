#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit

from pure_python import Evklid as Evklid0
from pure_cython import Evklid as Evklid1
from mypy_python import Evklid as Evklid3
from numba_jit import Evklid as Evklid4


def load(fate_class):
    f = fate_class()
    for _ in range(1_000_000):
        r = f.my_gcd()
    return r


def test(fate_class):
    f = fate_class()
    for _ in range(1_000):
        r = f.my_gcd()
    return r


for fc in [Evklid0, Evklid1, Evklid3, Evklid4]:
    print(fc, test(fc), timeit.timeit(lambda: load(fc), number=10) / 10)
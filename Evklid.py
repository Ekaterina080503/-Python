#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(gcd(a, b))
    print(math.gcd(a, b) == gcd(a, b))

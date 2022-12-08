#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        d, x, y = egcd(b % a, a)
    return (d, y - (b // a) * x, x)


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    d, x, y = egcd(a, b)
    print(d, x, y)
    print(d == a * x + b * y)

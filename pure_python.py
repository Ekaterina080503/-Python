#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Evklid():
    def __init__(self):
        self.x = 1
        self.a = 7614581656
        self.b = self.x % 4018367011 + 4018367011

    def my_gcd(self):
        self.x += 1
        self.b = self.x % 4018367011 + 4018367011
        while self.b != 0:
            self.a, self.b = self.b, self.a % self.b
        return self.a

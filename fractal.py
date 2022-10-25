#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle as tl

tl.lt(90)


def fr(w):  # w - размер мервой веточки
    if w >= 1:
        tl.pensize(w)
        tl.fd(w * 10)
        tl.rt(30)
        fr(w * 0.75)
        tl.lt(60)
        fr(w * 0.75)
        tl.rt(30)
        tl.bk(w * 10)
        tl.pensize(w)


tl.speed(10000)
tl.hideturtle()
tl.penup()
tl.goto(0, -200)
tl.pendown()
fr(10)

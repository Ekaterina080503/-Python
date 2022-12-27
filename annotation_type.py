#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from matplotlib import pyplot as pp
import numpy as np
from typeguard import typechecked

MODEL_G = 9.81
MODEL_DT = 0.001


@typechecked
class Body:
    def __init__(self, x: float, y: float, vx: float, vy: float) -> None:
        """
        Создать тело.

        Пареметры:
        ----------
        x: float
            горизонтальная координата
        y: float
            вертикальная координата
        vx: float
            горизонтальная скорость
        vy: float
            вертикальная скорость
        """

        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.trajectory_x = []
        self.trajectory_y = []

    def advance(self) -> None:
        """
        Выполнить шаг мат. модели применительно к телу, предварительно записав его координаты
        """
        self.trajectory_x.append(self.x)
        self.trajectory_y.append(self.y)

        self.x += self.vx * MODEL_DT
        self.y += self.vy * MODEL_DT
        self.vy -= MODEL_G * MODEL_DT


@typechecked
class Rocket(Body):
    def __init__(self, x: float, y: float, m0: float, dm: float, u: float, a: float) -> None:
        """
        Создать ракету.

        Пареметры:
        ----------
        x: float
            горизонтальная координата
        y: float
            вертикальная координата
        m0: float
            начальная масса
        dm: float
            скорость изменения массы
        u: float
            скорость выпускания газов
        a: float
            угол сопла (отсчитывается по часовой стрелки от низа)

        """
        super().__init__(x, y, 10, 10)  # Вызовем конструктор предка — тела, т.к. он для ракеты актуален
        self.m = m0
        self.dm = dm
        self.u = u
        self.a = math.radians(a)

    def advance(self) -> None:
        self.trajectory_x.append(self.x)
        self.trajectory_y.append(self.y)
        if self.m > 0:
            'Всё про Ох'
            self.x += self.vx * MODEL_DT
            dvx = self.u * math.sin(self.a) * self.dm * MODEL_DT / self.m
            self.vx += dvx

            'Всё про Оy'
            self.y += self.vy * MODEL_DT
            dvy = self.u * math.cos(self.a) * self.dm * MODEL_DT / self.m - MODEL_G * MODEL_DT
            self.vy += dvy

            'Всё про массу'
            self.m -= self.dm * MODEL_DT
        else:
            super().advance()


bodies = []
try:
    r = Rocket(0, 0, 10, 1, 100, 45)
    bodies.append(r)
    print('целые числа можно')
    print('добавим в список и постороим график траектории')
except:
    print('поываполрылвп')

try:
    r = Rocket(0.0, 0.0, 10.1, 1.1, -100, 45)
    bodies.append(r)
    print('вещественные и отрицательные числа можно')
    print('добавим в список и постороим график траектории')
except:
    print('вещественные и отрицательные числа нельзя')

try:
    r = Rocket('1', 0, 10, 1, 100, 45)
    bodies.append(r)
    print('строки можно')
    print('добавим в список и постороим график траектории')
except:
    print('строки нельзя')

try:
    r = Rocket(1j, 0, 10, 1, 100, 45)
    bodies.append(r)
    print('комплексные числа можно')
    print('добавим в список и постороим график траектории')
except:
    print('комплексные числа нельзя')

for t in np.arange(0, 10, MODEL_DT):  # для всех временных отрезков
    for b in bodies:  # для всех тел
        b.advance()  # выполним шаг

for b in bodies:  # для всех тел
    pp.plot(b.trajectory_x, b.trajectory_y)  # нарисуем их траектории
pp.show()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import matplotlib.pyplot as mpp  # импорт библиотек
import numpy

# Эта программа рисует график функции, заданной выражением ниже

if __name__ == '__main__':  # начало программы что бы при импорте не активировались
    arguments = numpy.arange(0, 200, 0.1)  # список точек от 0 до 200 с шагом 0.1
    mpp.plot(  # строим график по точкам
        arguments,  # сюда передаем х
        [math.sin(a) * math.sin(a / 20.0) for a in arguments]  # здесь полуем список у
    )
    mpp.show()  # вывод картинки

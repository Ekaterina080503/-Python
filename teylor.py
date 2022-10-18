import math
import matplotlib.pyplot as plt
import numpy as np

ITERATIONS = 200


def my_arct(x):  # считаем арктангенс. эта функция подходит для -1<=x<=1
    """
    Вычисление Арктангенса при помощи частичного суммирования
    ряда Тейлора для окрестности 0
    эта функция подходит для -1<=x<=1
    """
    multiplier = -1
    partial_sum = 0
    new_x = x
    for n in range(1, ITERATIONS, 2):
        multiplier *= -1
        new_x = x ** n
        partial_sum += new_x / n * multiplier

    return partial_sum


help(math.atan)
help(my_arct)

print(math.atan(0.4))  # сравним значения
print(my_arct(0.4))

vs = np.vectorize(my_arct)
print(my_arct, vs)

angles = np.r_[-1.03:1.03:0.001]
plt.plot(angles, np.arctan(angles), linewidth=3.0, color='cyan', label='библиотечный арктангенс')  # построим графики
plt.plot(angles, vs(angles), linewidth=1.0, color='black', label='наш арктангенс')
plt.legend()
plt.show()

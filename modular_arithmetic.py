#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numbers import Number
from Evklid_extended import egcd  # импортируем из прошлых работ функции :)


class ModularTypeError(TypeError):
    pass


class ModularDomainError(ValueError):
    pass


class IncorrectNumberModulusError(ValueError):
    pass


class Modular_Number(Number):
    def __init__(self, number=0, modul=2):
        if isinstance(number, int) and isinstance(modul, int):
            self.number = number % modul
            self.modul = modul
        else:
            raise ModularTypeError('You are trying to create Modular Number from ' + repr(number) + repr(modul))

    def __str__(self):
        return '[' + str(self.number) + ']mod(' + str(self.modul) + ')'

    def __eq__(self, other):
        if isinstance(other, int):
            other = Modular_Number(other, self.modul)

        if isinstance(other, Modular_Number):
            if other.modul == self.modul:
                return self.number == other.number
            else:
                raise IncorrectNumberModulusError('the numbers must have the same modulus')
        else:
            raise ModularDomainError("Can't say if Quaternion is equal to " + str(type(other)))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        if isinstance(other, int):
            other = Modular_Number(other, self.modul)

        if isinstance(other, Modular_Number):
            if other.modul == self.modul:
                return Modular_Number(self.number + other.number, self.modul)
            else:
                raise IncorrectNumberModulusError('the numbers must have the same modulus')
        else:
            raise ModularDomainError("Can't say if Quaternion is equal to " + str(type(other)))

    def __radd__(self, other):
        return self.__add__(other)

    def __neg__(self):
        return Modular_Number(-1 * self.number, self.modul)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Modular_Number(other, self.modul)

        if isinstance(other, Modular_Number):
            if other.modul == self.modul:
                return Modular_Number(self.number - other.number, self.modul)
            else:
                raise IncorrectNumberModulusError('the numbers must have the same modulus')
        else:
            raise ModularDomainError("Can't say if Quaternion is equal to " + str(type(other)))

    def __rsub__(self, other):
        return self.__neg__().__add__(other)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Modular_Number(other, self.modul)

        if isinstance(other, Modular_Number):
            if other.modul == self.modul:
                return Modular_Number(self.number * other.number, self.modul)
            else:
                raise IncorrectNumberModulusError('the numbers must have the same modulus')
        else:
            raise ModularDomainError("Can't say if Quaternion is equal to " + str(type(other)))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __pow__(self, power, modulo=None):
        if power == 1:
            return self
        else:
            if isinstance(power, int):
                return self.__mul__(self.__pow__(power - 1))
            else:
                raise ModularTypeError("You can't raise Modular_Number to a not-int degree")

    def __int__(self):
        return int(self.number)

    def __bool__(self):
        return bool(self.number)

    def multiply_module(self, a=1):  # умножим модуль числа на целое число
        if isinstance(a, int):
            self.modul *= a
        else:
            raise ModularTypeError("You can't multiply a module by a not-int number")

    def reverse_number(self):  # Вернем обратный класс если можем
        d, x, y = egcd(self.number, self.modul)
        if d == 1:
            return Modular_Number(x, self.modul)
        else:
            raise IncorrectNumberModulusError("class and module are not mutually simple")


a = Modular_Number(1, 5)  # проверка
b = Modular_Number(8, 5)
print(a, b)
print(a + b)
print(a - b)
print(a + 1)
print(1 - a)
print(a * b)
print(b ** 3)
print(a.reverse_number())
a.multiply_module(5)
print(a)
print(int(a))
c = Modular_Number(6, 7)
print(a + c)

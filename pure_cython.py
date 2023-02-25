# cython: language_level=3

class Evklid():
    def __init__(self):
        self.x: int = 1
        self.a: int = 7614581656
        self.b: int = self.x % 4018367011 + 4018367011

    def my_gcd(self) -> int:
        self.x += 1
        self.b: int = self.x % 4018367011 + 4018367011
        while self.b != 0:
            self.a, self.b = self.b, self.a % self.b
        return self.a

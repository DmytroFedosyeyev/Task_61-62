class Fraction:
    def __init__(self, num, divider):
        if divider == 0:
            raise ValueError('Делитель не может быть 0!')
        self.num = num
        self.divider = divider

    def __add__(self, other):
        num = self.num * other.divider + other.num * self.divider
        divider = self.divider * other.divider
        return Fraction(num, divider)

    def __sub__(self, other):
        num = self.num * other.divider - other.num * self.divider
        divider = self.divider * other.divider
        return Fraction(num, divider)

    def __mul__(self, other):
        num = self.num * other.num
        divider = self.divider * other.divider
        return Fraction(num, divider)

    def __truediv__(self, other):
        if other.num == 0:
            raise ValueError("На ноль делить нельзя!")
        num = self.num * other.divider
        divider = self.divider * other.num
        return Fraction(num, divider)

    def __eq__(self, other):
        return self.num == other.num and self.divider == other.divider

    def __str__(self):
        return f"{self.num}/{self.divider}"


f1 = Fraction(3, 4)
f2 = Fraction(5, 12)
print(f1)
print(f2)
print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 / f2)


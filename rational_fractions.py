from math import gcd

def lcm(x, y):
    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1

    return lcm


class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den
    def __str__(self):
        return f'{self.num}/{self.den}'
    def __add__(self, other):
        lcm = lcm(self.den, other.den)
        sum_num = self.num * (lcm / self.den) + other.num * (lcm / other.den)
        return Fraction(sum_num, lcm)
    def __sub__(self, other):
        lcm = lcm(self.den, other.den)
        sum_num = self.num * (lcm / self.den) - other.num * (lcm / other.den)
        return Fraction(sum_num, lcm)
    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)
    def __truediv__(self, other):
        res_num = self.num * other.den
        res_den = self.den * other.num
        res_gcd = gcd(res_num, res_den)
        return Fraction(res_num / res_gcd, res_den / res_gcd)
    def __eq__(self, other):
        f1 = self.simplify(self)
        f2 = self.simplify(other)
        return f1.num == f2.num and f1.den == f2.den
    def simplify(self):
        res_gcd = gcd(self.num, self.den)
        return Fraction(self.num / res_gcd, self.den / res_gcd)
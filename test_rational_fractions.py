from rational_fractions import Fraction


def test_class_fraction():
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)
    f3 = f1 + f2
    assert str(f3) == '5/4'
    f4 = f1 * f2
    assert str(f4) == '3/8'
    f5 = f1 - f2
    assert str(f5) == '-1/4'
    f6 = f1 / f2
    assert str(f6) == '2/3'
    assert f1 == Fraction(2, 4)
    assert str(f1.simplify()) == '1/2'
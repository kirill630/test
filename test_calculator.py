from calculator import Calc

calc = Calc()
def test_add_positive():
    x = 2
    y = 3
    res = 5
    assert calc.plus(x, y) == res, f"Проверка сложения не пройдена {x} + {y} != {res}"


def test_add_negative():
    x = 2
    y = 3
    res = 8
    assert calc.plus(x, y) != res

def test_subs_positive():
    x = 6
    y = 2
    res = 4
    assert calc.subs(x, y) == res, f"Проверка вычитания не пройдена {x} / {y} != {res}"

def test_subs_negative():
    x = 6
    y = 2
    res = 5
    assert calc.subs(x, y) != res

def test_mult_positive():
    x = 3
    y = 4
    res = 12
    assert calc.mult(x, y) == res, f"Проверка умножения не пройдена {x} * {y} != {res}"

def test_mult_negative():
    x = 3
    y = 4
    res = 10
    assert calc.mult(x, y) != res

def test_divis_positive():
    x = 10
    y = 5
    res = 2
    assert calc.divis(x, y) == res, f"Проверка деления не пройдена {x} / {y} != {res}"

def test_divis_negative():
    x = 10
    y = 5
    res = 3
    assert calc.divis(x, y) != res
def complex_sum(x: complex, y: complex) -> complex:
    return complex(x) + complex(y)


def complex_diff(x: complex, y: complex) -> complex:
    return complex(x) - complex(y)


def complex_mult(x: complex, y: complex) -> complex:
    return complex(x) * complex(y)


def complex_div(x: complex, y: complex) -> complex:
    return complex(x) / complex(y)


def complex_calc(d: dict) -> complex:
    if d['op'] == 0:
        arifmetic = complex_sum #Сумма
    elif d['op'] == 1:
        arifmetic = complex_diff #Вычитание
    elif d['op'] == 2:
        arifmetic = complex_mult #Умножение
    elif d['op'] == 3:
        arifmetic = complex_div #Деление
    else:
        raise ValueError
    return arifmetic(d['x'], d['y'])
from fractions import Fraction


def real_sum(x: Fraction, y: Fraction) -> Fraction:
    return Fraction(x) + Fraction(y)


def real_diff(x: Fraction, y: Fraction) -> Fraction:
    return Fraction(x) - Fraction(y)


def real_mult(x: Fraction, y: Fraction) -> Fraction:
    return Fraction(x) * Fraction(y)


def real_div(x: Fraction, y: Fraction) -> Fraction:
    return Fraction(x) / Fraction(y)



def real_calc(d: dict) -> Fraction:
    if d['op'] == 0: 
        arifmetic = real_sum #Сумма
    elif d['op'] == 1:
        arifmetic = real_diff #Вычитание
    elif d['op'] == 2:
        arifmetic = real_mult #Умножение
    elif d['op'] == 3:
        arifmetic = real_div #Деление
    else:
        raise ValueError
    return arifmetic(d['x'], d['y'])
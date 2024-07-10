import cmath


def extract_real_image(number: complex) -> tuple:
    """
    Извлекает целую и мнимую часть и возвращает кортеж
    Args:
        number (complex): исходное комплексное число
    Returns:
        pair (tuple): кортеж пары значений
    """
    return number.real, number.imag


# complex number
def program_1():
    c1 = 3 + 1j
    c2 = -3 - 1j
    c3 = 6 + -4j
    print(type(c1), type(c2), type(c3))
    print(c1, c2, c3)
    print(extract_real_image(c1), extract_real_image(c2), extract_real_image(c3))
    pass


program_1()


def program_2():
    pass


program_2()

from decimal import Decimal

from helpers import print_section


# Проблема вывода, вызванная ограниченным пространством для хранения значений
def program_1():
    print('float: 0.1 + 0.1 + 0.1 - 0.3')
    a = 0.1
    b = 0.1
    c = 0.1
    result = a + b + c - 0.3
    print(result)
    pass


print_section("Проблемы аппаратной точности компьютера в отношении float типа")
program_1()


# Пример противопоставление program_1()
def program_2():
    print('Decimal: 0.1 + 0.1 + 0.1 - 0.3')
    a = Decimal('0.1')
    b = Decimal('0.10')
    c = Decimal('0.10')
    result = a + b + c - Decimal('0.3')
    print(result)
    pass


print_section("Аналогичный пример но с Decimal, который решает проблему погрешности")
program_2()


# Создание десятичного объекта из объекта с плавающей точкой
def program_3():
    f = 10.523
    d1 = Decimal(f)
    d2 = Decimal.from_float(f)
    print(d1)
    print(d2)
    pass


print_section("Создание десятичного объекта из объекта с плавающей точкой")
program_3()

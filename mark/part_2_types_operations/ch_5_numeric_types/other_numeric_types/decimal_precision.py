from decimal import Decimal, getcontext

from helpers import print_section


# Глобальная установка точности вычислений с Decimal
def program_1():
    a = Decimal(1)
    b = Decimal(7)
    division = a / b
    print('a:', a)
    print('b:', b)
    print('a / b:', division)
    print(division.as_integer_ratio()[0])
    print(division.as_integer_ratio()[1])

    getcontext().prec = 4
    division = a / b
    print('a:', a)
    print('b:', b)
    print('a / b:', division)

    print(Decimal('0.1'))
    print(Decimal(0.1))
    print(Decimal(0.1) / 1)
    pass


print_section("Глобальная установка точности вычислений с Decimal")
program_1()

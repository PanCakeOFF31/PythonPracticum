import decimal
from decimal import Decimal

from helpers import print_section


def program_1():
    a = Decimal('1.00')
    b = Decimal('1.35')
    result = a / b
    print(result)

    decimal.getcontext().prec = 4

    result = a / b
    print(result)

    with decimal.localcontext() as ctx:
        ctx.prec = 1
        result = a / b
        print(result)

    result = a / b
    print(result)

    pass


print_section("контекст")
program_1()

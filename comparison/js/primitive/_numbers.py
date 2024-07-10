from decimal import Decimal
from fractions import Fraction

from helpers import print_section


# Underline
def program_1():
    print_section("program_1(): Underline")

    billion = 1_000_000_000
    print('billion:', billion)
    print(f'billion: {billion}')
    print('billion: {}'.format(billion))
    print('billion: %d, billion: %d' % (billion, billion))

    pass


# Underline
program_1()


# Different number-radix representation
def program_2():
    print_section("program_2(): Different number-radix representation")

    print(int('ff', 16))
    print(0xff, 0o777, 0b10101010)
    print(int('123456', 36))
    print(bin(1000)[2:])
    print(f'{10.923456:.0f}')

    pass


# Different number-radix representation
program_2()


# Parsers
def program_3():
    print_section("program_3(): Parsers")

    pass


# Parsers
program_3()


# Fraction digits
def program_4():
    print_section("program_4(): Fraction digits")

    print(f'{1.35:.1f}, {6.35:.1f}')

    d1 = Decimal('1.35')
    d2 = Decimal('6.35')
    print(f'{d1:.1f}, {d2:.1f}')

    f1 = Fraction(135, 100)
    f2 = Fraction(635, 100)
    print(f1, f2, float(f1), float(f2))
    print(f'{f1:.1f}, {f2:.1f}')

    pass


# Fraction digits
program_4()

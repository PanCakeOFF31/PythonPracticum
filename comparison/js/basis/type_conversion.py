# Type conversion - Number
from helpers import print_section


# Type conversion - bool()
def program_1():
    print_section("program_1(): Type conversion - bool()")
    print(bool(' '), bool(''), bool('0'), bool(None), bool(True))
    pass


# Type conversion - bool()
program_1()


# Type conversion - int()/float()
def program_2():
    print_section("program_2(): Type conversion - int()/float()")

    pass


# Type conversion - int()/float()
program_2()


# Assignment statement-expression
def program_3():
    print_section("program_3(): Assignment statement-expression")
    b = a = 20
    print(b, a)
    pass


# Assignment statement-expression
program_3()


# Multiplication
def program_4():
    print_section("program_4(): Multiplication")
    print('max' * 3)
    pass


# Multiplication
program_4()

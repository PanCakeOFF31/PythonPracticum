# common string literals and operators
from helpers import print_section


def program_1():
    print_section("program_1()")

    s = r"\temp\dir\files"  # неформатированная строка - no escapes
    b = b"asndkla"  # byte string
    u = u"фывлощчср"  # unicode string

    n1 = 10
    f = f'some text {n1}'
    f = "format string %d" % n1
    f = "format string {}".format(n1)
    pass


# common string literals and operators
program_1()


# list comprehension from sr
def program_2():
    print_section("program_2()")

    origin = "maxim"
    result = [c * 2 for c in origin]
    print(f"orig = {origin}", f"result = {result}")
    pass


program_2()


def program_3():
    print_section("program_3()")
    pass


program_3()

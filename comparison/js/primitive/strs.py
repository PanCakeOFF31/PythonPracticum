# Strings
from helpers import print_section


def program_1():
    print_section("program_1(): Strings")

    string = 'some text'

    print(string, len(string), string[8], string[-1])
    print(string * 3)
    print(string.index('e'))
    print(string.rindex('e'))

    pass


# Strings
program_1()


# Some methods
def program_2():
    print_section("program_2(): Some methods")

    original = 'some text asd bcd'
    print(original)
    print('asd' in original)
    print(original.title())

    pass


# Some methods
program_2()


# Slice
def program_3():
    print_section("program_3(): Slice")

    original = 'Lorem ipsum dolerum'
    start = 0
    end = 14
    step = 2

    print(original)
    print(original[slice(start, end, step)])
    print(original[3:3 + 5:1])
    print('asd'.swapcase())
    pass


# Slice
program_3()

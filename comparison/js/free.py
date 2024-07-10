#
from helpers import print_section


# Destructuring assignment - unpacking
def program_1():
    print_section("program_1(): Destructuring assignment - unpacking ")

    def foo1(ls):
        a, b, *_ = list(ls) + [0, 0]
        print(a, b)
        pass

    foo1([])

    pass


# Destructuring assignment - unpacking
program_1()

for i in range(-3, -6, -1):
    print(i)

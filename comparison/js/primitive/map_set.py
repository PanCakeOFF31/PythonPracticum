# Map
from helpers import print_section


def program_1():
    print_section("program_1(): Map")

    map1 = {10: 20, 11: 30}
    print(map1.pop(11))

    pass


# Map
program_1()


# Enum
def program_2():
    print_section("program_2(): Enum")

    ls = [3, 13, 33, 343]
    for enum in enumerate(ls):
        print(enum)

    pass


# Enum
program_2()

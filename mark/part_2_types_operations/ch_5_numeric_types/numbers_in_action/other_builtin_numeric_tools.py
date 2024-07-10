import random

# Разные способы округления результата
from helpers import print_section


def program_1():
    print(1 / 3.0)
    print(repr(1 / 3.0))
    print(repr(round(1 / 3.0, 2)))
    print(repr('%.2f' % (1 / 3.0)))
    pass


print_section("Разные способы округления результата")
program_1()


def program_2():
    print(random.random())
    print(random.randrange(1, 11))
    print(random.randrange(11))
    print(random.randint(0, 10))
    print(random.choice([1, 2]))

    init_list = [3, 18, -4, 9]
    print(init_list)
    random.shuffle(init_list)
    print(init_list)

    pass


print_section("The random module")
program_2()

# set comprehension
from helpers import print_section


def program_1():
    s = {v for v in range(1, 11)}
    print(s)
    pass


print_section("set comprehension")
program_1()

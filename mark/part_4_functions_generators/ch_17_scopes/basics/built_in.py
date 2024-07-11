import builtins

from helpers import print_section


# Built-ins
def program_1():
    print_section("program_1(): Built-ins")

    print(list(zip([10], [20])))
    print(builtins.abs(10))
    print(zip is builtins.zip)

    pass


# Built-ins
program_1()

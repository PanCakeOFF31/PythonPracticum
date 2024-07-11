# Global
from helpers import print_section


def program_1():
    print_section("program_1(): Global")
    global global_x
    global_x = 200


global_x = 100
print('global_x:', global_x)
# Global
program_1()
print('global_x:', global_x)

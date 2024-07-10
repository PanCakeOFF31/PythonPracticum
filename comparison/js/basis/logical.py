# Logical operator
from helpers import print_section


# Логические операторы возвращают выражение
def program_1():
    print_section("program_1(): Logical operator and return value")

    print(bool(10) or bool(5))
    # Возвращает первое истинное
    print(10 or 5)
    # Возвращает первое ложное
    print(10 and 4 and 0 and True)

    pass


# Logical operator and return value
program_1()

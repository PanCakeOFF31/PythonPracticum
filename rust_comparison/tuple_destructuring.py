from helpers import print_section


def program_1():
    t = (500, 6.4, 44, 1)
    print(t)

    a, *b, c = t
    print(a, b, c)

    a, b, *c = t
    print(a, b, c)


print_section("Составной тип - tuple + деструктуризация")
program_1()

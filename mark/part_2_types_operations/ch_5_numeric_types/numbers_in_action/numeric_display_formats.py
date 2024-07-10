from helpers import print_section


def program_1():
    print('%e' % 10000000.0)
    pass


# Выражение форматирования строк
program_1()


def program_2():
    s1 = repr('spam')
    s2 = str('spam')
    print(s1, s2)
    pass


print_section('repr и str по-разному форматируют значения')
# Выражение форматирования строк
program_2()

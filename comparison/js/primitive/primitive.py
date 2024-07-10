from helpers import print_section


# Форматирование строки
def program_1():
    print_section("program_1(): Форматирование строки")
    num = 155.123
    print(num)

    print(f"{num}, {num:.2f}")
    pass


# Форматирование строки
program_1()

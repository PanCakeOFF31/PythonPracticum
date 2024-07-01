from helpers import print_section


# Балуемся с числовыми литералами в разны СС
def program_1():
    number = 1774
    # Численные литералы в различных системах счисления
    print(number, '->', oct(number), '->', hex(number), '->', bin(number))
    print(1774, 0o3356, 0x6ee, 0b11011101110)
    # Восьмеричное представление двоичного литерала десятичного числа 11774
    print(oct(0b11011101110))


print_section("Балуемся с числовыми литералами в разны СС")
program_1()


# Запись float-point number
def program_2():
    print(3.14E+10)
    print(3.14E-10)
    print(0.000000000314)
    pass


print_section("Запись float-point number")
program_2()


# Преобразование строки с основанием в десятичное число
def program_3():
    print(int('21', 3))
    pass


print_section("Преобразование строки с основанием в десятичное число")
program_3()


# Комплексные числа
def program_4():
    number = 10 + 44j
    print(number, type(number), type(number) is complex)
    alternative = complex(15, -13)
    print(alternative)


print_section("Демонстрация комплексных чисел")
program_4()

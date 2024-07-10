from helpers import print_section


# Аналогия между нормальным и цепочным сравнением
def program_1():
    x = 10
    y = 20
    z = 30
    d = 25
    # Chained comparison
    print(x < y < z)  # Equivalent to print(x < y and y < z)
    # Chained comparison
    print(x < y < z > d)
    # Normal comparison
    # Эквивалентное нормальное сравнение
    print(x < y and y < z and z > d)
    pass


print_section("Демонстрация цепочного сравнения")
program_1()


# Целое число в bool() обертке
def program_2():
    T = True
    F = False
    print(T, int(T), float(T))
    print(F, int(F), float(F))
    pass


print_section("Целое число в bool() обертке")
program_2()


# Сравнение чисел с логическим типом
def program_3():
    t = True  # 1
    f = False  # 0
    a = 10
    b = -10
    print(t > b)
    print(f > b)
    pass


print_section("Сравнение чисел с логическим типом")
program_3()


# Цепочное сравнение с не интуитивно понятным результатом
def program_4():
    print(1 == 2 < 3)  # Equivalent to print: (1 == 2 and 2 < 3) -> False

    a = 5
    b = 20
    c = 30
    print(a < b < c > a ** 2 > b)
    # Equivalent to print: (a < b and b < c and c > a**2 and a**2 > b)
    pass


print_section("Цепочное сравнение с не интуитивно понятным результатом")
program_4()

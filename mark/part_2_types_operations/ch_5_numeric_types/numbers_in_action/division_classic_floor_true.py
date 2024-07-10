# Не очевидный результат сравнения чисел с плавающей точкой
import math

from helpers import print_section


def program_1():
    a = 1.1
    b = 2.2
    print(a + b)  # 3.3000000000000003
    print(a + b == 3.3)
    print(round(a + b, 1) == 3.3)
    pass


print_section("Не очевидный результат сравнения чисел с плавающей точкой")
program_1()


# Сравнительный результат с math.floor(), math.ceil(), round(), trunc()
def program_2():
    a = 3.1
    b = 3.5
    c = 3.9
    print('initial values:', a, b, c)
    print('values when use math.floor():', math.floor(a), math.floor(b), math.floor(c))
    print('values when use math.ceil():', math.ceil(a), math.ceil(b), math.ceil(c))
    print('values when use round():', round(a), round(b), round(c))
    print('values when use trunc():', math.trunc(a), math.trunc(b), math.trunc(c))
    pass


print_section("Сравнительный результат с math.floor(), math.ceil(), round(), trunc()")
program_2()


# Операции связанные с остатком для отрицательных чисел
def program_3():
    a = -3.1
    b = -3.5
    c = -3.9
    print('initial values:', a, b, c)
    print('values when use math.floor():', math.floor(a), math.floor(b), math.floor(c))
    print('values when use math.ceil():', math.ceil(a), math.ceil(b), math.ceil(c))
    print('values when use round():', round(a), round(b), round(c))
    print('values when use trunc():', math.trunc(a), math.trunc(b), math.trunc(c))
    pass


print_section("Операции связанные с остатком для отрицательных чисел")
program_3()


# true division vs floor division for both sign numbers
def program_4():
    a = 7.6
    b = 3.2
    print(a, b, -a, -b)
    print(a / b, a / -b, -a / b)
    print(a // b, -a // -b, a // -b, -a // b)
    print("Явное использование trunc():",
          math.trunc(a // b),
          math.trunc(-a // -b),
          math.trunc(-a / b),
          math.trunc(a / -b))
    pass


print_section("true division vs floor division for both sign numbers")
program_4()

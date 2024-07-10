import decimal
from decimal import Decimal
from fractions import *

from helpers import print_section


# Пример использования дробного числа
def program_1():
    f1 = Fraction(numerator=8, denominator=15)
    f2 = Fraction(7, 17)
    print('f1:', f1, 'numerator:', f1.numerator, 'denominator:', f1.denominator)
    print('f2:', f2, 'numerator:', f2.numerator, 'denominator:', f2.denominator)
    pass


# Нельзя использовать 0 в знаменателе
def program_2():
    try:
        Fraction(1 / 0)
    except ZeroDivisionError:
        print("Попытка создать дробное число с 0 знаменателем")
    pass


# Альтернативные варианты конструкторов
def program_3():
    print("Fraction(0.255) =", Fraction(0.255))
    print("Fraction('0.255') =", Fraction('0.255'))
    print("Fraction(Decimal('0.445')) =", Fraction(Decimal('0.445')))
    pass


print_section("Дробные (Fraction) числа")
program_1()

print_section("Ноль в знаменатель")
program_2()

print_section("Альтернативные конструкторы для Fraction")
program_3()


# Упрощение операций над числами с плавающей точкой
def program_4():
    a1 = 2 / 5
    a2 = 2 / 3
    print(a1, a2)
    print(a1 + a2)

    f1 = Fraction(2, 5)
    f2 = Fraction('2/3')
    print(f1, f2)
    print(f1 + f2)
    print(float(f1 + f2))

    decimal.getcontext().prec = 2
    d1 = Decimal(2 / 5)
    d2 = Decimal(2 / 3)
    print(d1, d2)
    print(d1 + d2)


print_section("Упрощение операций над числами с плавающей точкой")
program_4()


# Преобразование Fraction и Decimal
def program_5():
    f = 2.555
    print(f.as_integer_ratio())
    print(Decimal(f.__str__()))
    print(Fraction(*f.as_integer_ratio()))
    pass


print_section("Преобразование Fraction и Decimal")
program_5()


# Смешение разных чисел
def program_6():
    x = Fraction(1, 3)
    print(type(x), x)
    print(type(x + 2), x + 2)
    print(type(x + 2.0), x + 2.0)
    print((x + 3).limit_denominator(10))
    pass


print_section("Смешение разных чисел")
program_6()

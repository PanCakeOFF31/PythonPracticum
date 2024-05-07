from helpers import print_article, print_section


def summing(a, b):
    print_section("Функция с позиционными аргументами")
    print(a + b)


def summing_error_b():
    print_section("Вызов функции с пропущенным positional arg ")
    try:
        summing(10)
    except TypeError as te:
        print("Пропущен обязательный позиционный аргумент - b")
        print(te)


def summing_error_a():
    print_section("Вызов функции с пропущенным positional arg ")
    try:
        summing(b=20)
    except TypeError as te:
        print("Пропущен обязательный позиционный аргумент - a")
        print(te)


def summing_error_too():
    print_section("Вызов функции с лишним positional arg ")
    try:
        summing(10, 20, 30)
    except TypeError as te:
        print("Лишний аргумент")
        print(te)


print_article("Аргументы функции и позиционные аргументы")

summing(10, 20)
summing(b=20, a=10)

summing_error_a()
summing_error_b()
summing_error_too()
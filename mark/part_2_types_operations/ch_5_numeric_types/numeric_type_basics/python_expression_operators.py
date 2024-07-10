from helpers import print_section


def program_1():
    print(type(repr(10)), repr(10))
    print(type(str(10)), str(10))
    pass


print_section("Функция representation - repr()")
program_1()


# equivalent to indexing
def program_2():
    sl = slice(1, 3, 1)
    collection = [111, 2, 3, 44, 5]
    print(collection[sl])
    print(collection[1:3:1])
    pass


print_section("Эквивалентный синтаксис использования среза")
program_2()


# Сравнение словаря
def program_3():
    d1 = {'name': 'Max'}
    d2 = {'name': 'Max'}
    print(d1 is d2)
    print(d1 == d2)
    pass


print_section("Сравнение словаря")
program_3()


# operator grouping
def program_4():
    print(2 ** 3 * 4)
    pass


program_4()


# Конвертация типов во время смешивания разных типов в выражениях
def program_5():
    print(type(10 + 4))
    print(type(10 + 4.0))
    print(type(10 + 4 + 1j))
    print(type(10.0 + 4 + 1j))
    pass


program_5()

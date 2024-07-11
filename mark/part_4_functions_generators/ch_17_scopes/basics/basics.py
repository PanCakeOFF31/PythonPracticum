from helpers import print_section


# Scope, dir, vars - запустить вне функции
def program_1():
    print_section("program_1(): Scope, dir, vars")

    # Возвращает список атрибутов в текущей области видимости
    print(dir())

    # Получаем и распаковываем словарь атрибутов
    scope_attributes = {**vars()}

    for attr in scope_attributes:
        print(attr, ':', scope_attributes[attr])

    print(__name__)


# Scope, dir, vars
# program_1()


# Конфликт областей
def program_2():
    print_section("program_2(): Конфликт областей")
    pass


# Конфликт областей
program_2()

program_3_global = 100


# Nonlocal, global
def program_3():
    print_section("program_3(): Nonlocal, global")

    program_3_global = 200
    print(program_3_global)


# Nonlocal, global
program_3()

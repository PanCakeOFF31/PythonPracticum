# Closure with for
from helpers import print_section


def program_1():
    print_section("program_1(): Closure with for ")

    # Проблема - запоминаем одно и тоже лексическое окружение
    # В котором значением i является 4
    # Так как i создается глобально в f1-scope, у for нет своего scope
    def f1():
        actions = []
        for i in range(5):
            actions.append(lambda n: i ** n)
            # print(actions[i](2))
        return actions

    acts = f1()

    for act in acts:
        print(act(2))


# Closure with for
program_1()


# Способ обхода проблемы выше
def program_2():
    print_section("program_2(): Способ обхода проблемы выше")

    def f1():
        actions = []

        for i in range(5):
            # Стандартное значение оценивается в момент создания объекта-функции
            actions.append(lambda n, i=i: i ** n)
        return actions

    acts = f1()

    for act in acts:
        print(act(2))


# Способ обхода проблемы выше
program_2()


# Вычисление значения по умолчанию происходит в момент создании функции
def program_3():
    print_section("program_3(): Вычисление значения по умолчанию происходит в момент создании функции")

    def evaluate():
        print('evaluate execution')
        return 100

    def f1(x=evaluate()):
        print('f1, x:', x)

    f1()
    f1(10)
    f1()


# Вычисление значения по умолчанию происходит в момент создании функции
program_3()

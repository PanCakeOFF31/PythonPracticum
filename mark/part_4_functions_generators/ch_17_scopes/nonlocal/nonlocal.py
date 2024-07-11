# Nonlocal, var must be initialized
from helpers import print_section


def program_1():
    print_section("program_1(): Nonlocal, var must be initialized")

    # def fn():
    #     nonlocal x
    #     x += 10
    #     print(x)

    # fn()


# Nonlocal, var must be initialized
# program_1()


# Global
def program_2():
    print_section("program_2(): Global")

    def fn_1():
        global x
        x = 10

        def fn_2():
            global x
            x = 30
            print(x)

        fn_2()
        print(x)

    fn_1()
    print(x)
    pass


# Global
# program_2()
# print(x)


# nonlocal in actions
def program_3():
    print_section("program_3(): nonlocal in actions")

    def tester(start):
        state = start

        def nested(label):
            # Здесь state берется из localscope
            print(label, state)
            # В данной ситуации в scope существует state = uninitialized
            # По умолчанию изменять нельзя
            state += 1

    pass


# nonlocal in actions
program_3()


# nonlocal in action with changing
def program_4():
    print_section("program_4(): nonlocal in action with changing")

    def tester(start):
        state = start

        def nested(label):
            nonlocal state
            print(label, state)
            state += 1

        return nested

    nested = tester(10)

    nested(5)
    nested(5)
    nested(5)

    pass


# nonlocal in action with changing
# program_4()


# nonlocal boundary
def program_5():
    print_section("program_5(): nonlocal boundary")

    def fn():
        nonlocal x
        print(x)

    # Нелокальные переменные создаются на этапе
    # создания функции, а не во время вызова
    x = 15
    fn()
    # x = 15


# nonlocal boundary
program_5()

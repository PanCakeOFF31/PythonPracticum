# Factory function
from helpers import print_section


def program_1():
    print_section("program_1(): Factory function")

    def maker(n):
        def action(x):
            return n ** x

        return action

    # каждый вызов
    m_1 = maker(2)
    # повторный вызов вернет новую функцию с новой присоединенной информацией
    m_2 = maker(3)
    print(m_1(4), m_1(16))
    print(m_2(4), m_2(16))


# Factory function
program_1()


# Factory function with lambda
def program_2():
    print_section("program_2(): Factory function with lambda")

    def maker(n):
        return lambda x: x ** n

    m_1 = maker(3)
    m_2 = maker(5)

    print(m_1(4), m_1(16))
    print(m_2(4), m_2(16))


# Factory function with lambda
program_2()


# Ранний способ сохранения состояния, до реализации enclosing scope
def program_3():
    print_section("program_3(): Ранний способ сохранения состояния, до реализации enclosing scope")

    # Старый способ, чтобы запомнить состояние enclosing scope - не было
    def f1():
        x = 88

        def f2(x=x):
            x *= 2
            return x

        return f2

    f = f1()
    print(f())
    # Чтобы реализовать механизм генераторов, необходимо повторно передавать
    # результирующее значение
    print(f(f()))

    # Здесь современный подход для сохранения состояния
    def f3():
        x = 88

        def f4():
            nonlocal x
            x *= 2
            return x

        return f4

    ff = f3()
    print(ff())
    print(ff())


# Ранний способ сохранения состояния, до реализации enclosing scope
program_3()

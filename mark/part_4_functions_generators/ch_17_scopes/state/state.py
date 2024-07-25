from helpers import print_section


# nonlocal state
def program_1():
    print_section("program_1(): nonlocal state")

    def tester(start):
        state = start

        def nested(label):
            nonlocal state
            print(label, state)
            state += 1

        return nested

    f1 = tester(100)
    f2 = tester(True)

    f1('True')
    f2('True')
    f1('True')
    f2('True')


# nonlocal state
program_1()


# global state
def program_2():
    print_section("program_2(): global state")

    def tester(start):
        global state
        state = start

        def nested(label):
            global state
            print(label, state)
            state += 1
            return state

        return nested

    # Каждый вызов инкриминирует разделяемую переменную
    f1 = tester(10)
    f1('Hi')
    f1('Hi')
    # Повторный вызов tester сбрасывает единственную разделяемую информацию
    f2 = tester(30)
    f2('Hoo')
    f1('Hi')


# global state
program_2()


# class state
def program_3():
    print_section("program_3(): class state")

    class Tester:
        def __init__(self, start):
            self.state = start

        def nested(self, label):
            print(label, ':', self.state)
            self.state += 1

        def __call__(self, label):
            print(label, ':', self.state)
            self.state += 1

    f1 = Tester(0)
    f2 = Tester(0)

    Tester.nested(f1, 'f1')

    f1.nested('f1')
    f2.nested('f2')
    f1.nested('f1')
    f2.nested('f2')

    f3 = Tester(20)
    f3('f3')

    # Использование перегрузки __cal__
    Tester(15)('f4')


# class state
program_3()


# function attribute state
def program_4():
    print_section("program_4(): function attribute state")

    def tester(start):
        # Нельзя иметь доступ к переменной до инициализации
        # nested.state = start

        # Это должно быть перед def nested... Так как создание
        # объекта функции at runtime
        x = 20

        def nested(label, x=x):
            print(x, y)
            print(label, nested.state)
            nested.state += 1

        #  nested может использовать y, так как он существует во внешнем scope
        y = 30
        nested.state = start
        return nested

    f1 = tester(0)
    f1('f1')
    f1('f1')
    f1('f1')


# function attribute state
program_4()


# State with mutable object
def program_5():
    print_section("program_5(): State with mutable object")

    def tester(start):
        def nested(label):
            # Обращаемся к имени в режиме read-only
            print(label, state[0])
            # Изменение состояния объекта != измените переменной
            # Переменная state ссылается на тот же объект
            state[0] += 1

        # Здесь объявлен mutable object
        state = [start]
        return nested

    f1 = tester(0)
    f2 = tester(10)
    f1('f1')
    f1('f1')
    f2('f2')
    f1('f1')
    f2('f2')


# State with mutable object
program_5()

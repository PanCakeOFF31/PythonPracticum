from helpers import print_section


# Keyword-only
def program_1():
    print_section("program_1(): Keyword-only")

    # Использование передачи аргументов только по ключевым словам
    def fn(*, mode, iteration, log=True):
        print('mode:', mode)
        print('iteration:', iteration)
        print('log:', log)
        pass

    # В любом порядке, log можно не указывать
    fn(iteration=1, mode='hard')

    print(10, 20, sep='___', end='[end]\n')
    print(10, 20, sep='___', end='[end]\n\n')
    # Допустимо key-word only при условии * в аргументах
    print(sep='___', *[10, 20])
    print(sep='___', *[10, 20], *[13, 15])

    # Такой синтаксис уже недопустим и неоднозначен
    # print(sep='___', 10, 20)

    def fn_2(a, b=3, *c, d, **e):
        print('a:', a)
        print('b:', b)
        print('c:', c)
        print('d:', d)
        print('e:', e)

    fn_2(1, 2, d=3, *[5], x=15)

    print('maxim', file=open('./console.txt', 'a'))


# Keyword-only
program_1()


# Некоторые проверки
def program_2():
    print_section("program_2(): Некоторые проверки")

    def fn_1(a, **kwargs):
        print(a, kwargs)
        pass

    # fn_1(**{'b': 15, 'c': 20}, 15)
    fn_1(**{'b': 15, 'c': 20, 'a': 15})
    fn_1(b=15, c=20, a=15)

    def fn_2(a, *b):
        print(a, b)
        pass

    # fn_2(1, 2, a=3)
    # fn_2(*[1, 2], a=77)
    fn_2(15, 10, 10)

    def fn_3(a, *b, c):
        print(a, b, c)
        pass

    fn_3(1, c=3, *[15, 20])
    fn_3(1, *[15, 20], c=3)
    fn_3(c=3, *[15, 20, 30])
    fn_3(c=3, a=1)
    pass


# Некоторые проверки
program_2()

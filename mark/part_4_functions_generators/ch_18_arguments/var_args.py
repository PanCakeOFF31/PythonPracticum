# Varargs implementation
from helpers import print_section


def program_1():
    print_section("program_1(): Varargs implementation")

    # Универсальная функция tracer, которая вызывает переданную
    def tracer(function, *args, **kwargs):
        print('Calling:', function.__name__)
        return function(*args, **kwargs)
        pass

    def summing(a, b, c, d):
        return a + b + c + d

    print(tracer(summing, 1, **{'b': 2, 'd': 4, 'c': 3}))


# Varargs implementation
program_1()


# Keyword-only arguments
def program_2():
    print_section("program_2(): Keyword-only arguments")

    # c - keyword-only. Чтобы передать c, необходимо указывать c явно в keyword
    def fn_1(a, *b, c):
        print('a:', a)
        print('b:', b)
        print('c:', c)

    # В данном случае 'missing keyword-only argument'
    # fn_1(1, 2, 3)
    fn_1(1, 2, c=3)

    # Если указать пустой символ *, то функция будет ожидать только keyword-only args
    def fn_2(*, a, b):
        print('a:', a)
        print('b:', b)

    fn_2(b=3, a=True)

    def fn_3(*, a, **kwargs):
        print(a)
        print(kwargs)

    fn_3(b=True, a=15)
    fn_3(**{'b': 10}, a=15)
    fn_3(a=15, **{'b': 10})

    def fn_4(a, *b, c=6, **d):
        print(a, b, c, d)

    # keyword-only passing, допустимые варианты расположения
    # после **
    fn_4(1, *[2, 3], **{'f': 15, 'ff': True}, c=6)
    # перед ** и после *
    fn_4(1, c=6, *[2, 3], **{'f': 15, 'ff': True})
    # перед *
    fn_4(1, *[2, 3], **{'f': 15, 'ff': True, 'c': 3})

    def fn_5(*b, c=6, **d):
        print(b, c, d)

    fn_5(1, 2, c=3, z=15, x=17)
    # Нельзя key-word only перед * когда нет positional args
    # fn_5(c=3, 1, 2, z=15, x=17)


# Keyword-only arguments
program_2()

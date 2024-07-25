from helpers import print_section


# Argument matching, full pack
def program_1():
    print_section("program_1(): Argument matching")

    # Порядок параметров в заголовке функции
    def fn_1(a, b, c=15, d=16, *e, f=0, g=0, **h):
        print(a, b, c, d, e, f, g, h)

    fn_1(1, 2, 3, 4, 5, 6, 7, f=8, g=10, name='maxim')

    # a - varargs collection
    # b - keyword-only or by name only
    # c - тоже только по ключевому слову, он перекрыт varargs collection
    def fn_2(*a, b, c):
        pass


# Argument matching
# program_1()


# Keyword and default combination
def program_2():
    print_section("program_2(): Keyword and default")

    def evaluate():
        print('Значение вычислено')
        return 'default'

    def fn_1(a, b, c):
        print('a:', a, 'b:', b, 'c:', c)

    fn_1(1, 2, 3)
    fn_1(1, c=10, b=20)

    # fn_1(c=10, 10,b=20) - недопустимо так смешивать

    def fn_2(a, b=False, c: any = evaluate()):
        print('a:', a, 'b:', b, 'c:', c)

    print('default значение определено при создании fn_2')
    fn_2(15)
    # a - получило значение по позиции
    # b - по default
    # c - по ключевому слову
    fn_2(15, c=True)
    fn_2(**{'a': 15, 'b': 15, 'c': 15})


# Keyword and default
program_2()


# Arbitrary arguments
def program_3():
    print_section("program_3(): Arbitrary arguments")

    def collection_pos(*args):
        print(type(args), args)
        pass

    collection_pos(10, 0b1010, 30)

    def collection_key(**kwargs):
        print(type(kwargs), kwargs)
        pass

    collection_key(name='John', age=25)

    def combination(pos=15, *args, **kwargs):
        print('pos:', pos)
        print('args:', args)
        print('kwargs:', kwargs)
        pass

    combination(True, True, True, true=True)

    x = 10

    def fn(x=15):
        print(x)

    fn(x=30)


# Arbitrary arguments
program_3()


# Unpacking arguments
def program_4():
    print_section("program_4(): Unpacking arguments")

    def fn(a, b, c, d, f):
        print('a:', a, 'b:', b, 'c:', c, 'd:', d, 'f:', f)
        pass

    fn(True, *[10], **{'d': 17, 'c': 'c'}, f=15)


# Unpacking arguments
program_4()

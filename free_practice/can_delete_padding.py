import sys;

from helpers import print_section

print('Hello!')
print('HellO!'.casefold())
print('HellO!'.lower())
print("МакСимКа".swapcase())


def fn_1():
    a = 10

    def fn_inner(v):
        return v * 2

    b = fn_inner(a)

    print(a, b)

    l = lambda v: v * 2
    c = l(a)

    print(a, b, c)


fn_1()


def fn2() -> tuple:
    pass


fn2()


# assert
def program_1():
    print_section("program_1(): assert")
    assert sum([1, 3]) == 4, 'OK'
    # assert sum(1, 3) == TypeError
    pass


# assert
program_1()

print(sys.getsizeof('aяы'))

# удаление по значению
ls = [10, 20, 30]
# удаление по индексу
# del ls[10]
ls.remove(10)
print(ls)

# удаления ключа
dc = {'a': 10, 'b': 20}
del dc['a']
print(dc)

try:
    print(123)
except TypeError:
    print()

print('dir')
print(dir())
print(dir(str))
print(help(str.index))

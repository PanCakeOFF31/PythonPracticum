# Arrays
from helpers import print_section


def program_1():
    print_section("program_1(): Arrays")

    arr1 = [10, 20, 30]
    print(arr1[-1])
    list((10, 20, 30))

    pass


# Arrays
program_1()


# Appending
def program_2():
    print_section("program_2(): Appending")

    ls = [10, -10]
    print(ls)

    ls.append(100)
    ls.insert(0, 200)
    print(ls)

    del ls[0]
    print(ls)

    del ls[1:]
    print(ls)

    for item in reversed('asd'):
        print(item)

    pass


# Appending
program_2()


# split(), join()
def program_3():
    print_section("program_3(): split(), join()")

    original = 'tree, house, gamepad'

    split = original.split(', ')
    print(split)

    joined = ', '.join(split)
    print(joined)

    pass


# split(), join()
program_3()


# reverse, sorted
def program_4():
    print_section("program_4(): reverse, sorted")

    arr = [1, 2, 3]

    reversed = arr[:]
    reversed.reverse()

    print(arr)
    print(reversed)

    sorted = reversed[:]
    sorted.sort()
    print(sorted)

    pass


# reverse, sorted
program_4()


# Unpacking/rest
def program_5():
    print_section("program_5(): Unpacking/rest")

    a, b = [10, 20]
    print(a, b)

    a = [10, 10]
    b = [20, 20]

    a[0], b[0], *rest = [b[0], a[0], 15, 16]
    print(a, b, rest)

    pass


# Unpacking/rest
program_5()


# range
def program_6():
    print_section("program_6(): range")

    print(list(range(4, 2)))
    b = a = 10
    print(b)

    def foo(s: str):
        iter = reversed(s)
        return ''.join([char for char in iter])

    print(foo(s='asdbs'))
    print('asdasd'[::-1])
    pass


# range
program_6()

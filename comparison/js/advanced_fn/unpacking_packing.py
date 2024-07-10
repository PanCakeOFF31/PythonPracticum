from helpers import print_section


# Аргументов больше чем параметров
def program_0():
    print_section("program_0(): Аргументов больше чем параметров")

    def too_args(a, b):
        print(a, b)
        pass

    try:
        too_args(10, 20, 30)
    except:
        print("Передали больше чем доступно позиционных аргументов")

    pass


# Аргументов больше чем параметров
program_0()


# Rest parameters (Packing)
def program_1():
    print_section("program_1(): Rest parameters")

    def packaging(*args):
        print(args)
        pass

    packaging(10, '15', True, '❤️')
    pass


# Rest parameters
program_1()


# Unpacking collection
def program_2():
    print_section("program_2(): Unpacking/spreading collection")

    # Packing/rest collection
    def foo(*any_collection: list):
        print(any_collection)
        pass

    foo(*[10, 11])
    foo(*{10, 20})
    foo(*{'10': 10, '20': 20})

    # Развёртывание списка, чтобы передать 4 аргумента в функцию max(...)
    print(max(*[10, 20, 30, 40]))

    pass


# Unpacking collection
program_2()


# Merging - слияние списков
def program_3():
    print_section("program_3(): Merging - слияние списков")

    ls1 = [10, 3, 1]
    ls2 = [7, -3, 8]

    merged_list = [*ls1, *ls2]

    print('ls1:', ls1)
    print('ls2:', ls2)
    print('merged_list:', merged_list)

    pass


# Merging - слияние списков
program_3()


# Unpacking - spread operator
def program_4():
    print_section("program_4(): Unpacking - spread operator")

    print([{10, 20}, [15, 20]])
    print(*{10, 20, 30}, *[10, 20, 30])
    print({*[10, 20, 30], *{15, 17, 30}})

    pass


# Unpacking - spread operator
program_4()


# kwargs
def program_5():
    print_section("program_5(): kwargs")

    def foo(**kwargs):
        for entry in kwargs.items():
            print(entry[0], ':', entry[1])

        pass

    foo(name='Maxim', age=25)

    pass


# kwargs
program_5()

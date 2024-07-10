# Destructuring assignment
from helpers import print_section


def program_1():
    print_section("program_1(): Destructuring assignment")

    # Деструктуризация кортежа с пропуском и оператором rest
    a, b, _, *c = 10, 20, 30, 40, 50
    print(type(a), a)
    print(type(b), b)
    print(type(c), c)

    # def foo_1(*a):
    #     print(type(a), print(a))
    #     pass
    # 
    # foo_1(10, 20, 30)

    pass


# Destructuring assignment
program_1()


# Destructuring assignment
def program_2():
    print_section("program_2(): Destructuring assignment")

    a, b, c = 'asd'
    print(a, b, c)

    d1 = {1: 10, 2: 20, 3: 30}
    for key, value in d1.items():
        print(f'{key}: {value}')

    big_list = list(range(10))
    big_a, *big_b, big_c = big_list
    print(big_list)
    print(big_a, big_b, big_c)

    pass


# Destructuring assignment
program_2()


# Default value
def program_3():
    print_section("program_3(): Default value")

    def foo(a: int = 1, *ls):
        print(a, ls)
        pass

    foo(*[1, 2, 3])

    pass


# Default value
program_3()


# Destructuring assignment - default
def program_4():
    print_section("program_4(): Destructuring assignment - default ")

    def foo1(ls):
        a, b, *_ = list(ls) + [0, 0]  # default value
        print(a, b)
        pass

    foo1([])

    pass


# Destructuring assignment - default
program_4()

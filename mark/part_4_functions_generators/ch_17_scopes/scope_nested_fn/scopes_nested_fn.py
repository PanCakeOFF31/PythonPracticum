# Nested scopes
from helpers import print_section


def program_1():
    print_section("program_1(): Nested scopes")
    x = 100

    def fn_outer():
        y = 200
        print(x, y)

        def fn_inner():
            # x находится в самой дальней объемлющей области
            # y находится в самой ближайшей объемлющей области
            nonlocal x, y
            x = 150
            y = 250
            print(x, y)

        fn_inner()

    fn_outer()
    print(x)


# Nested scopes
program_1()

from helpers import print_section


# min wakeup function
def program_1():
    print_section("program_1(): min wakeup function")

    def min_1(*args):
        res = args[0]

        for arg in args[1:]:
            if arg < res:
                res = arg

        return res

    def min_2(first, *rest):
        for arg in rest:
            if arg < first:
                first = arg
        return first

    def min_3(*args):
        tmp = list(args)
        tmp.sort()
        return tmp[0]

    pass


# min wakeup function
program_1()

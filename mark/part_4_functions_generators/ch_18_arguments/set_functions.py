from helpers import print_section


# Set functions
def program_1():
    print_section("program_1(): Set functions")

    # Передаются последовательности
    def intersection(*args):
        if len(args) == 0:
            return []

        result = list()

        for item in args[0]:
            if item in result:
                continue
            for sequence in args[1:]:
                if item not in sequence:
                    break
            else:
                result.append(item)

        return result

    print(intersection([10, 20, 30], (10, 11, 12), {10, 15, 18}))
    print(intersection())

    pass


# Set functions
program_1()


# Union
def program_2():
    print_section("program_2(): Union")

    def union(*args):
        if len(args) == 0:
            return []

        result = []
        for sequence in args:
            for item in sequence:
                if item not in result:
                    result.append(item)

        return result

    print(union([1, 2, 3], [3, 2, 1]))
    print(union([1, 2, 3], [3, 2, 1], [4]))

    pass


# Union
program_2()


# free
def program_3():
    print_section("program_3(): free")

    print([1, 2, 3][:1])

    # get or default
    print({}.get('sep', 'max'))

    def keyword_only(*, a=False):
        print(a)

    # unexpected keyword argument
    # keyword_only(b=15)

    # Приведение коллекции: False - пустая, True - более 0 размер
    print(bool([]))
    print(bool([1]))
    print()
    print(sorted([10, 1, 2, 3], reverse=True))
    print(sorted([10, 1, 2, 3], reverse=False))

    pass


# free
program_3()

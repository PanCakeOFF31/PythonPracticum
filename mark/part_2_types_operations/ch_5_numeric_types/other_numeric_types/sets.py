# Создание словаря
from helpers import print_section


def program_1():
    s1 = set((1, 2, 3, 4, 5))
    s2 = {1, 2, 3, 4, 5, 6}
    s3 = set('clock')
    print(s1)
    print(s2)
    print(s3.add(7), s3)
    print(s3)
    pass


program_1()


# Immutable set - frozenset()
def program_2():
    s1 = frozenset([frozenset([5, 18]), frozenset([18, 5]), 3])
    print(s1)
    pass


print_section("Immutable set - frozenset()")
program_2()


# iterable conversion
def program_3():
    l1 = list(range(0, 10))
    s1 = set(l1)
    print(s1)
    pass


print_section("iterable conversion")
program_3()


# difference finding
def program_4():
    s1 = set('abcdefg')
    s2 = set('abcdehijklmn')
    print(s1 - s2)
    print(s1.difference(s2))
    pass


print_section("difference finding")
program_4()


# set equality
def program_5():
    l1 = list('abcd')
    l2 = list('dcab')
    print('l1:', l1, 'l2:', l2)
    print('l1 == l2:', l1 == l2)

    s1 = set('abcd')
    s2 = set('dcba')
    print('s1:', s1, 's2:', s2)
    print(s1 == s2)
    pass


print_section("set equality")
program_5()


# practice example
def program_6():
    engineers = {'John', 'Jane', 'Jack', 'Jill', 'Joe', 'Michael', 'Sarah', 'Alex', 'Vitaly', 'Dima'}
    managers = {'Kate', 'Alex', 'Vitaly', 'Dima', 'Tony', 'Carol'}
    print(engineers.intersection(managers))
    print(engineers & managers)
    print(engineers.union(managers))
    print(engineers.difference(managers))
    print(engineers.symmetric_difference(managers))
    print(engineers ^ managers)
    pass


print_section("practice example")
program_6()

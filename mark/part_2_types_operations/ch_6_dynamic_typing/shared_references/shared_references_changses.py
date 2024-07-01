import copy

from helpers import print_section


# Mutable object and shared reference
def program_1():
    original = ['😍', 3, 17, 55, -10, '🐍']
    print('original:', original)

    shallow_copy = original
    shallow_copy[3] = '😂'
    print('shallow_copy:', shallow_copy)

    deep0 = list(original)
    deep0[3] = '🐍🐍🐍🐍'
    print('deep0:', deep0)

    deep1 = original.copy()
    deep1[3] = '😎'
    print('deep1:', deep1)

    deep2 = original[:]
    deep1[3] = 'ἊἊἋ'
    print('deep2:', deep2)

    deep3 = copy.copy(original)
    deep1[3] = '😏😶‍🌫️'
    print('deep3:', deep3)

    deep4 = copy.deepcopy(original)
    deep1[3] = '😭'
    print('deep4:', deep4)

    print('original:', original)


print_section("Mutable object and shared reference")
program_1()

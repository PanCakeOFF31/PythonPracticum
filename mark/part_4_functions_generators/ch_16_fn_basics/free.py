from helpers import print_section


# Free set
def program_1():
    print_section("program_1(): Free set")

    # not hashable type - list
    # s = {10, '15', [15, 20]}

    # правый операнд 15 is not iterable
    # 10 in 15

    # Проверка на членство элемента в коллекции
    print([10, 20].__contains__(15))
    print(15 in [10, 20])

    pass


# Free set
program_1()

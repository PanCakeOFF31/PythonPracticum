# Loops
from helpers import print_section


#
def program_1():
    print_section("program_1(): Loops")

    while True:
        print('Всего 1 итерация')
        break

    pass


# Loops
program_1()


# for-in
def program_2():
    print_section("program_2(): for-in")

    ls = [10, 20, 30]
    for item in ls:
        print(item)

    records = {"name": "maxim", "10": 10, True: 123}
    for record in records:
        print(record)

    iterator = iter(records)
    for item in iterator:
        if item:
            break
        print(item)

    pass


# for-in
program_2()


# labels
def program_3():
    print_section("program_3(): labels")

    for i in range(0, 3):
        for j in range(0, 3):
            print(i, j)
            if i == 1 and j == 1:
                break

    pass


# labels
program_3()

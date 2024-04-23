print([10, 20] * 2)

initial = [116, 12, 13]
double = initial.__mul__(2)

print(initial)
print(double)


def task_1(origin: list):
    origin.pop(2)
    print(len(origin))
    origin.reverse()
    new_list = [1, 0]
    # origin.extend(new_list)
    origin = origin.__add__(new_list)
    print(origin)
    return origin


task_1(['New', 10, 10.5, True, [10, 20, 30]])


def task_2(or_1: list, or_2: list):
    total_1 = or_1 + or_2
    total_2 = or_1.__add__(or_2)
    print(total_1, total_2, or_1, or_2)


task_2([10, 20], [-10, -15])

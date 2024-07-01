import sys


def program_1():
    for pow in range(10, 20):
        big = 2 ** pow
        print('pow:', pow)
        print(big)
        print(sys.getsizeof(big))
    pass

    program_1()


# Unlimited-precision number (integer)
def program_2():
    print(round(1360 / 1024, 3), 'килобайт')
    a = 2 ** 100_000
    print(round(sys.getsizeof(a) / 1024, 3), 'килобайт')
    a = 2 ** 1_000_000
    print(round(sys.getsizeof(a) / 1024, 3), 'килобайт')
    a = 2 ** 1_000_000_000
    print(round(sys.getsizeof(a) / 1024 / 1024, 3), 'мегабайт')
    a = 2 ** 10_000_000_000
    print(round(sys.getsizeof(a) / 1024 / 1024, 3), 'мегабайт')

# Опасно запускать на слабом ПК
# program_2()

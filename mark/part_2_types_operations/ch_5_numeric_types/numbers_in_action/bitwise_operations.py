from helpers import print_section


def program_1():
    initial = 1
    print('initial:', initial, bin(initial))
    left_shift = initial << 2
    print(left_shift, bin(left_shift))
    inversion = left_shift ^ 0b1111
    print(inversion, bin(inversion))
    inversion ^= 0b1111
    print(inversion, bin(inversion))
    pass


program_1()


# Возвращает количество бит необходим для двоичного представления целого числа
def program_2():
    x = 144
    print('x:', x, bin(x))
    print('x', x.bit_length(), x.bit_count())
    pass


print_section("Битовые методы")
program_2()

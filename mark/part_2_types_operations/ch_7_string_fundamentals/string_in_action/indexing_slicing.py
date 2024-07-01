from helpers import print_section


# indexing and slicing
def program_1():
    print_section("program_1(): indexing and slicing")

    s = "spam"
    print('s:', s, 's[0]:', s[0], 's[-1]:', s[-1])
    print(s[1:3], s[1:], s[::-1], s[-1::-1])


# indexing and slicing
program_1()


# slice objects with index syntax
def program_2():
    print_section("program_2(): slice objects with index syntax")

    s = "reversing like this are"
    sl = slice(0, 5, 2)
    print(f'Исходная строка - {s}')
    print(f'Объект среза - {sl}')

    print('Реализация среза через литеральный синтаксис:', s[0:5:2])
    print('Реализация среза через объект slice:', s[sl])

    pass


# slice objects with index syntax
program_2()

# import sys
# print(sys.argv)

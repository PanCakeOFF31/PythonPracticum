def program_1(long_string):
    print(f'Исходная строка: \'{long_string}\'')
    print('Длина строки: ', len(long_string))

    if len(long_string) > 0:
        print('Первый элемент строки : ', long_string[0])
        print('Последний элемент строки : ', long_string[-1])
    else:
        print('Первый элемент строки : ', '')
        print('Последний элемент строки : ', '')


program_1('Maxim')
program_1('')


def program_2(string):
    print(string[1:3])
    print(type(string[1:3]))
    print(string[2:])


program_2('Maxim')

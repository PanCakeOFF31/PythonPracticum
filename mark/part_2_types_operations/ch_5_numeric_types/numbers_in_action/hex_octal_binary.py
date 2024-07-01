# Способ преобразования десятичного числа в строку определенной СС
def program_1():
    print(format(177, 'x'))
    print(hex(177))
    pass


program_1()


# Преобразование числа из произвольной СС в десятичную
def program_2():
    print(int('21', 3))
    pass


program_2()


# Форматирование десятичного числа за счет форматирования строки
# и подстановочных знаков
def program_3():
    formatted = '%o, %x' % (47, 47)
    print(formatted)
    formatted = '{:o}, {:x}, {:b}'.format(47, 47, 47)
    print(formatted)
    pass


program_3()

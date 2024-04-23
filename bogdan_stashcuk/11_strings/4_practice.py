def program_1(origin: str):
    print('Исходная  строка: ', origin)
    print('Та же строка в верхнем регистре: ', origin.upper())
    print('Та же строка в нижнем регистре: ', origin.lower())
    print('Количество символов \'о\' в строке : ', origin.count('о'))
    print('Капитализация строки: ', origin.upper().capitalize())
    print('Индекс первой буквы \'р\': ', origin.index('р'))


program_1('Околопланетная орбита расположена на...')


def program_2(string: str):
    if string.isdigit():
        print("Строка представляет собой число")
    if string.isnumeric():
        print("Числовая строка")
    if str.isdigit(string):
        print("Строка представляет собой число")


program_2('10')


def replacing(string: str):
    print(string.replace('о', 'О'))


replacing('Около')

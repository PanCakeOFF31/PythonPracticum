# Проверка некоторых методов для строк: string methods
def program_1():
    value = 'какая-то строка с информацией'

    print(value.count('а'))
    print("54".isdigit())
    print("54".isnumeric())
    print("       \t".isspace())


program_1()


# Получение справки - getting help
def program_2():
    print(dir(str))
    print(type(str))
    # print(dir("asd"))
    print(type(""))


program_2()


def program_3():
    S = "maximum"
    S.find('x', 0, 7)
    S.find('x', )
    # Выведет один атрибут - S
    print(dir())


program_3()


# pattern matching
def program_4(value: int):
    match value:
        case 10:
            print('10')
        case 20:
            print(20)
        case _:
            print("no value")


program_4(10)
program_4(20)
program_4(30)

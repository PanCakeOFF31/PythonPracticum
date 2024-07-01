# ternary operator
from helpers import print_section


def program_1():
    result = '10 > 5' if 10 > 5 else '10 < 5'
    print(result)
    result = '10 < 5' if 10 < 5 else '10 < 5'
    print(result)

    user = {'name': 'Maxim',
            'job': 'developer'}

    # getOrDefault() - аналог Java
    value = user.get('hobby') if 'hobby' in user else 'unknown'
    print(value)


# Тернарный оператор
print_section("Демонстрация тернарного оператора при обращении к словарю")
program_1()


# Получение объекта slice и передача его в []
def program_2():
    collection = [10, 20, 30]
    s = slice(0, 2, 1)
    print(collection[s])


print_section("Альтернативное определение slice")
program_2()


#  string iteration
def program_3(string: str):
    for char in string:
        print(char.upper())


print_section("Итерация по строке")
program_3("wind")


# generator
def program_4():
    pass


# assert
def program_5():
    pass


print_section('generator')
program_4()

print_section('assert')
program_5()

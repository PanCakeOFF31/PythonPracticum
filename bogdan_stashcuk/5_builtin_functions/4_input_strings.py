def program_1():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    city = input("Enter your city: ")

    print("Hello", name, 'You are from', city, "and your age:", age, "is valid")


def program_2():
    name = 'maxim blinov aleksandroviCH'
    print(name.capitalize())


def program_3():
    name = 'some name'
    print(dir(name))


def program_4():
    name = 'error'
    print(name.count('e'))
    print(len(name))


# Ввод данных
# program_1()

# Капитализация строки - все переводятся в нижний регистр, а первая буква становится заглавной
# program_2()

# Вывод всех аттрибутов строкового объекта
program_3()

# Длина строки + количество букв в строке
program_4()

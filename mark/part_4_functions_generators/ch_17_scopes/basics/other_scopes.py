from helpers import print_section


# Loop variables
def program_1():
    print_section("program_1(): Loop variables")

    for i in range(5):
        print('Вызов из цикла, переменная цикла i:', i)

    print('Вызов из объемлющей цикл области i:', i)

    pass


# Loop variables
# program_1()


# Comprehension variables
def program_2():
    print_section("program_2(): Comprehension variables")

    item = 10

    # Переменная item существует в отдельной области видимости
    comp_list = [item for item in range(3)]
    print(item, comp_list)

    pass


# Comprehension variables
program_2()


# except scope
def program_3():
    print_section("program_3(): except scope")

    try:
        x = 10
        print('Вызов из try, x:', x)
        raise ZeroDivisionError()
    except ZeroDivisionError as x:
        # Переменная с именем x будет уничтожена после выхода из except
        print('Вызов из except, x:', x)

    print('Вызов из local, x:', x)


# except scope
program_3()

from helpers import print_section


# Simple example
def program_1():
    print_section('Простой пример производства новых скопированных список')

    total_list = [number for number in range(1, 6)]
    print(type(total_list), ':', total_list)

    total_set = {number for number in range(1, 6)}
    print(type(total_set), ':', total_list)

    total_dict = {key: value for key, value in [('a', 10), ('b', 20)]}
    print(type(total_dict), ':', total_dict)

    print([value for value in zip(total_set, total_list)])
    pass


# Simple example
program_1()


# List comprehension with changes
def program_2():
    print_section("program_2(): List comprehension with changes")

    initial_list = (1, 2, 5, 'zZ', 12, 15,)
    multiple_list = [value * 3 for value in initial_list]

    print('initial_list:', initial_list)
    print('multiple_list:', multiple_list)

    pass


# List comprehension with changes
program_2()


# List comprehension with if statement
def program_3():
    print_section("program_3(): List comprehension with if statement")

    initial_str = 'manufacturing'
    result = str([letter for letter in initial_str if ord(letter) % 2 == 0])

    print('initial_str:', initial_str)
    print('result:', result)

    pass


# List comprehension with if statement
program_3()


# List comprehension with nested for
def program_4():
    print_section("program_4(): List comprehension with nested for")

    # Порядок выполнения - слева на право
    matrix = [
        [x + y for x in range(1, 5)]
        for y in range(10, 12)
    ]
    print(matrix)

    three_dimension = [
        [
            [x for x in range(0, 4)]
            for y in range(0, 3)
        ]
        for z in range(0, 2)
    ]
    print(three_dimension)

    pass


# List comprehension with nested for
program_4()


# Real example
def program_5():
    print_section("program_5(): Real example")

    some_example = [
        x for x in [1, 2, 3]
        for y in [4, 5, 6]
    ]
    print(some_example)

    people = [
        {
            "first_name": "Василий",
            "last_name": "Марков",
            "birthday": "9/25/1984"
        }, {
            "first_name": "Регина",
            "last_name": "Павленко",
            "birthday": "8/21/1995"
        }]

    property_values = [
        person[key]
        for person in people
        for key in person
    ]
    print(property_values)

    birthday = [
        person[key]
        for person in people
        for key in person
        if key == 'birthday'
    ]
    print(birthday)

    pass


# Real example
program_5()


# Переписывание list comprehension as for statement
def program_6():
    print_section("program_6(): Переписывание list comprehension as for statement")

    total_list: list = [number for number in range(1, 6)][:3]
    print(type(total_list), ':', total_list)

    total_list: list = []
    for number in range(1, 6):
        total_list.append(number)
    total_list = total_list[:3]

    print(type(total_list), ':', total_list)

    pass


# Переписывание list comprehension as for statement
program_6()

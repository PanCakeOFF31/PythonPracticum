# Dictionary as object
from helpers import print_section


def program_1():
    print_section("program_1(): Dictionary as object")

    user = {
        "name": "Max",
        "age": 18,
    }

    user["size"] = 15211
    print(user["name"], user.get("age"), user.get("weight"), user["size"])

    del user["size"]
    print(user["name"], user.get("age"), user.get("weight"), user.get("size"))

    newUser = {
        *user
    }

    print(type(newUser), newUser)

    newUser = {
        **user
    }
    print(type(newUser), newUser)

    pass


# Dictionary as object
program_1()


# Delete
def program_2():
    print_section("program_2(): Delete")

    l1 = [10, 20, 30]
    print(l1)

    del l1[0]
    print(l1)

    d1 = {
        'name': 'max'
    }

    del d1['name']
    print(d1.get('kjnkvsaldj'))
    pass


# Delete
program_2()


# Проверка существования ключа
def program_3():
    print_section("program_3(): Проверка существования ключа")

    d1 = {10: 11, 11: 12, 12: 13}
    print(10 in d1)

    pass


# Проверка существования ключа
program_3()

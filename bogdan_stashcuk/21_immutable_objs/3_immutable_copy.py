import copy

from helpers import print_subsection, print_article


def program_1():
    print_subsection("Оригинальный словарь")
    info = {
        'name': 'Maxim',
        'is_instructor': True
    }

    print(info, type(info), id(info), sep=", ", end="\n")
    print(info.get('name') + ':', id(info.get('name')))

    print_subsection("Копирование адреса объекта в переменную")
    info_copy_address = info
    print(info_copy_address, type(info_copy_address), id(info_copy_address), sep=", ", end="\n")
    print(info.get('name') + ':', id(info.get('name')))

    print_subsection("Shallow coping")
    info_shallow_copy = info.copy()
    print(info_shallow_copy, type(info_shallow_copy), id(info_shallow_copy), sep=", ", end="\n")
    print(info.get('name') + ':', id(info.get('name')))

    print_subsection("Shallow coping with constructor")
    info_shallow_copy = list(info)
    print(info_shallow_copy, type(info_shallow_copy), id(info_shallow_copy), sep=", ", end="\n")
    print(info.get('name') + ':', id(info.get('name')))


def program_2():
    print_article("Копирование контейнера с вложенным контейнером")
    print_subsection("Оригинальный список с вложенным списком")

    inner_list = [10, 20, 30]
    original_list = [
        100,
        inner_list,
        200
    ]
    print(original_list, type(original_list), id(original_list), sep=", ", end="\n")
    print(original_list[1], id(original_list[1]), sep=", ", end="\n")

    print_subsection("Копированный список с вложенным списком")

    list_copy = list(original_list)
    print(list_copy, type(list_copy), id(list_copy), sep=", ", end="\n")
    print(list_copy[1], id(list_copy[1]), sep=", ", end="\n")

    print_subsection("Изменяем внутренний список через копию исходной списка")

    list_copy[1].append(99)
    print(original_list, type(original_list), id(original_list), sep=", ", end="\n")
    print(original_list[1], id(original_list[1]), sep=", ", end="\n")
    print(list_copy, type(list_copy), id(list_copy), sep=", ", end="\n")
    print(list_copy[1], id(list_copy[1]), sep=", ", end="\n")


def program_3():
    print_article("Демонстрация копирования изменяемых объектов")

    set_1 = {10, 20, 30}
    set_2 = set(set_1)

    print(set_1, id(set_1), sep=", ")
    print(set_2, id(set_2), sep=", ")


def program_4():
    print_article("Демонстрация копирования неизменяемых объектов")

    info = {'name': 'maxim'}
    print(info, id(info['name']))

    info_copy = dict.copy(info)
    print(info_copy, id(info_copy['name']))

    name = info['name']
    print(name, id(name))

    info['name'] = info['name'].upper()
    print(info, id(info['name']))
    print(info_copy, id(info_copy['name']))


def program_5():
    print_article("Глубокое копирование")

    print_subsection("Оригинальный список с вложенным списком")

    inner_list = [10, 20, 30]
    original_list = [
        100,
        inner_list,
        200
    ]

    print(original_list, type(original_list), id(original_list), sep=", ", end="\n")
    print(original_list[1], id(original_list[1]), sep=", ", end="\n")

    print_subsection("Копированный список через глубокое копирование")

    copy_list = copy.deepcopy(original_list)

    print(copy_list, type(copy_list), id(copy_list), sep=", ", end="\n")
    print(copy_list[1], id(copy_list[1]), sep=", ", end="\n")

    print_subsection("Стандартное Shallow Copy")

    copy_list = original_list.copy()

    print(copy_list, type(copy_list), id(copy_list), sep=", ", end="\n")
    print(copy_list[1], id(copy_list[1]), sep=", ", end="\n")


# program_1()
# program_2()
# program_3()
# program_4()
program_5()

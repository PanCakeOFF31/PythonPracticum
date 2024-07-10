import copy

from helpers import print_section


# Поверхностная копия объекта
def program_1():
    print_section("Поверхностная копия без вложения")

    a = str("Maxim")
    b = a
    print(f"a = {a}, id(a) = {id(a)}")
    print(f"b = {b}, id(b) = {id(b)}")

    c = copy.copy(a)
    print(f"a = {a}, id(a) = {id(a)}")
    print(f"b = {b}, id(b) = {id(b)}")
    # строковый литерал хранится в стеке
    print(f"c = {c}, id(c) = {id(c)}")

    pass


program_1()


def program_2():
    print_section("Глубокая копия")

    l_ref = ['🤞', '😉', True]
    l_origin = [10, 20, l_ref, 'maxim']
    l_shallow = l_origin
    l_copy = l_origin.copy()
    l_deep = copy.deepcopy(l_origin)

    print(f"l_ref = {l_ref}, id(l_ref) = {id(l_ref)}")
    print(f"l_origin = {l_origin}, id(l_origin) = {id(l_origin)}")
    print(f"l_shallow = {l_shallow}, id(l_shallow) = {id(l_shallow)}")
    print(f"l_copy = {l_copy}, id(l_copy) = {id(l_copy)},\n\t l_copy[2] = {l_copy[2]}, id(l_copy[2]) = {id(l_copy[2])}")
    print(f"l_deep = {l_deep}, id(l_deep) = {id(l_deep)},\n\t l_deep[2] = {l_deep[2]}, id(l_deep[2]) = {id(l_deep[2])}")
    pass


program_2()

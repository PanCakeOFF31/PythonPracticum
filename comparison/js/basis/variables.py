from helpers import print_section, print_section_ending

global_str = "global"


# Демонстрация работы затенения
def program_1():
    print_section("program_1(): Демонстрация работы затенения")
    global global_str
    str1 = "asd"
    print(str1)
    str1 = "asdasd"
    print(str1)
    print(global_str)
    global_str = "Asd"
    pass


# Демонстрация работы затенения + затенение глобальной переменной
program_1()
print(global_str)


# Null и undefined
def program_2():
    print_section("program_2(): Null и undefined")
    a = None
    print(a)
    pass


# Null и undefined
program_2()

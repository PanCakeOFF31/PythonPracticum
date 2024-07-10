from helpers import print_section


# Scopes
def program_1():
    print_section("program_1(): Scopes")
    a = 15;

    def modify():
        global a
        a = 30
        print('Вложенная/global переменная:', a, id(a))
        a = 40
        print('Вложенная переменная:', a, id(a))

    print('Внешняя переменная', a)
    modify()
    print('Внешняя переменная', a)
    pass


# Scopes
program_1()
print('Global переменная', a, id(a))

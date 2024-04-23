# объявление функции
def print_name_function(name):
    # тело функции - на основании отступа - 4 пробела
    print(name)


# Объявление функции, использование похожих имен
def my_name(name):
    print(name)


# recursion
def recursion():
    recursion()


name = 'Maxim'
my_name(name)
print('maxiM')

recursion()

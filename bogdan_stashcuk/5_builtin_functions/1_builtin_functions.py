def my_fn(a, b):
    return a + b


def my_fn_print(a, b):
    print(a + b)


print(my_fn(10, 20))
my_fn_print(10, 20)

# type()
# Вывожу типы данных у объектов
print(type(18), type(20.5), type('some'), type([]), type({}), type({1, 2, 3}), sep='\n')
print(print)

# input()
# name = input('Enter your name\n')
# print('Your name:', name)

# len()
print(len({10, 20, 30}))

# sum()
print(sum([1, 2, 3]))

# min()
# max()
# id()
# int()
print(int('15'))

# str()
# bool()

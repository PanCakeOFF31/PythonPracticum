# Простые примеры
simple_tuple = (10, 20, 30, '144')
print(simple_tuple, type(simple_tuple))

tuple_copy = tuple(simple_tuple)
print(tuple_copy, type(tuple_copy))

print(simple_tuple[0], simple_tuple[:3:])
print(simple_tuple + (10,))
print(simple_tuple.__add__((10,)))

# Картеж объектов, которые можно менять, но сам кортеж - нет
single_tuple = ({
                    'id': 100
                },)

print(single_tuple)
single_tuple[0]['id'] = 200
print(single_tuple)

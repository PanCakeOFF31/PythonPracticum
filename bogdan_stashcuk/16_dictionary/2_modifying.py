my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.259,
    'optionals': [],
}

print(my_motorbike.__dir__())

# Изъятие из словаря элементы по одному
print(len(my_motorbike))
print(my_motorbike.popitem())
print(my_motorbike.popitem())
print(my_motorbike.popitem())
print(my_motorbike.popitem())
print(len(my_motorbike))

my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.259,
    'optionals': [],
}

my_motorbike[10] = 20
print(my_motorbike)

my_motorbike.update({10: 25})
print(my_motorbike)

del my_motorbike[10]
print(my_motorbike)

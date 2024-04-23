# Сравнение словарей
my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.259,
    'optionals': [],
}

foreign_motorbike = {
    'price': 25000,
    'engine_vol': 1.259,
    'brand': 'Ducati',
    'optionals': [],
}

print(my_motorbike)
brand = dict.__getitem__(my_motorbike, 'brand')
print('Бренд мотоцикла -', brand)

print(foreign_motorbike)
print('Словарь содержит ключ \'brand\':', foreign_motorbike.__contains__('brand'))
brand = foreign_motorbike['brand']
print('Значение ключа \'brand\':', brand)

print(id(my_motorbike), id(foreign_motorbike))
print('Сравнение двух байков:', my_motorbike.__eq__(foreign_motorbike))

print(my_motorbike is None)

cars = {
    'brand': 'Toyota',
    'price': 10_000,
}

print('brand' in cars, cars.__contains__('brand'))
print('year' in cars, cars.__contains__('year'))
print('price' in cars, cars.__contains__('price'))

cars = ['Omoda', 'Hyndai', 'Lada']
print(cars)
print('Omoda' in cars, cars.__contains__('Omoda'))

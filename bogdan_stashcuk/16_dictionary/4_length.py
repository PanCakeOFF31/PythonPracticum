my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.259,
}

print(len(my_motorbike))

if 'brand' in my_motorbike:
    del my_motorbike['brand']

print(len(my_motorbike))

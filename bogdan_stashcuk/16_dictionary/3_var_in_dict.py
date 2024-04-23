my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.259,
}

key_name = 'brand'
my_motorbike[key_name] = 'BMW'
print(my_motorbike)

# Вложенный словарь
my_motorbike = {
    'brand': 'Ducati',
    'engine_vol': 1.259,
    'price_info': {
        'price': 250000,
        'is_available': True
    }
}

print(my_motorbike)
print('my_motorbike[\'price_info\'][\'is_available\'] =',
      my_motorbike['price_info']['is_available'])

#
bike_brand_key = 'brand'
bike_brand = 'OMODA'

bike_price_key = 'price'
bike_price = 25500

bike_weight_key = 'weight'
bike_weight = 11.5

my_motorbike = {
    bike_brand_key: bike_brand,
    bike_price_key: bike_price,
}

my_motorbike[bike_weight_key] = bike_weight
print(my_motorbike)

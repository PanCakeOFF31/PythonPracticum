# Основные методы словарей

disk = {}
print(disk, type(disk), id(disk))

disk['brand'] = 'Samsung'
disk['price'] = 800

print(disk)
print('Ключи словаря:', disk.keys(), '\nЗначения словаря:', disk.values())
print('Копия словаря:', disk.copy())
print('Элементы словаря', disk.items())

for item in disk.items():
    print('item:', item)
    list(item)
    print(item[0])

if disk.get('tuple') is None:
    disk['tuple'] = 'new element'

print(disk)

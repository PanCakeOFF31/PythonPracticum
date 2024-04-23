# Копирование словарей
disk = {}
disk['brand'] = 'Samsung'
disk['price'] = 800

new_disk = disk.copy()
new_disk['type'] = 'SSD'

print(disk)
print(new_disk)

disk['brand'] = 'Kingston'
new_disk['price'] = new_disk['price'] * 3

print(disk)
print(new_disk)

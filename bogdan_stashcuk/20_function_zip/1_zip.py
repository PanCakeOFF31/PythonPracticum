# Функция порождает итератор по кортежам
fruits = ['apple', 'banana', 'lime']
quantities = [100, 70, 50]

zipped = zip(fruits, quantities)
print(zipped)

print(list(zipped))
print(list(zipped))

# Превращают zip(): iterator of tuple в dict
new_dict = dict(zip(fruits, quantities))
print(new_dict)

# zipped = zip(fruits, quantities)
# for item in zipped:
#     imm_list = item;
#     print(imm_list, type(imm_list))
#
# zipped = zip(fruits, quantities)
# fruit_quantity = {}
# for item in zipped:
#     fruit_quantity[item[0]] = item[1]
#
# print(fruit_quantity)
#
# zipped = zip(fruits, quantities, [1, 2, 3, 4])
# print(list(zipped))
#
# zipped = zip(fruits, quantities)
# print(dict(zipped))
#
# zipped = zip(fruits, quantities, [1, 2, 3, 4])
# print(dict(zipped))

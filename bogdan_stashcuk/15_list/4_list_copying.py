origin_list = ['Igor', 'Pavel', 'Anton']

copy_list_1 = origin_list.copy()
copy_list_2 = list(origin_list)
copy_list_3 = origin_list[:]

print(id(origin_list), origin_list)
print(id(copy_list_1), copy_list_1)
print(id(copy_list_2), copy_list_2)
print(id(copy_list_3), copy_list_3)

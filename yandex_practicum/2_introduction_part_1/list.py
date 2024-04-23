simple_list = [10, 20, 'maxim']
print(simple_list)
print(simple_list[0])
print(simple_list[1])
print(simple_list[2])
print(simple_list[0])

new_list = simple_list + simple_list
print(new_list)

simple_list[2] = 'notmaxim'
print(simple_list)
print(new_list)

print(simple_list)
print('len(simple_list) = ' + str(len(simple_list)))

start_list = [10, 11, 12]
start_set = set(start_list)
start_list = list(start_set)

print(start_list)
print(start_set)

start_set.add(10)

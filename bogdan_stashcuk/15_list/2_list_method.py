def print_section(text: str):
    print('-------------------------------------------------------------')
    print('\t\t', text)


print_section('Исходный список:')
origin = ['часы', 'false', 'max', 'max', '000', 'Замок', 'замоК']
print(origin)

# Добавление элемента в конец списка
print_section('append:')
copy = origin.copy()
print('copy:', copy)
print('copy after appending:', copy.append('new element!!!'))

# Удаление последнего элемента/ элемента по индексу
print_section('pop:')
copy = origin.copy()
print('copy:', copy)

deleted_item = copy.pop()
print('Удаленный элемент: ', deleted_item)
print('copy, удаление последнего:', copy)

deleted_item = copy.pop(-2)
print('Удаленный элемент: ', deleted_item)
print('copy удаление предпоследнего:', copy)

# Удаление элемента по значению
print_section('remove:')
copy = origin.copy()
copy.remove('max')
print('copy:', copy)
print('copy после remove()', copy)

# Добавление элемента по индексу
print_section('insert:')
copy = origin.copy()

print('copy:', copy)

copy.insert(-1, 'last item')
print('copy после remove()', copy)

# Сортировка списка
print_section('sort:')
copy = list(origin)

copy.sort()
print('copy:', copy)

copy.sort(reverse=True)
print('copy:', copy)

# Нахождение индекса элемента
print_section('index:')
copy = origin.copy()
print('Индекс элемента \'max\'', copy.index('max'))

# Очистка списка
print_section('clear:')
copy = origin.copy()
copy.clear()
print(copy)

#
print_section('copy:')
copy = origin.copy()
del copy[-1]
print('copy:', copy)
print('origin:', origin)

#
print_section('extend:')
copy = origin.copy()
copy.extend(copy)
print(copy)

#
print_section('reverse:')
copy = origin.copy()
copy.reverse()
print(copy)

# Подсчет количества вхождений
print_section('count:')
copy = origin.copy()
print('количество вхождений \'max\':', copy.count('max'))

playlist_1 = {'Голубой вагон', 'Облака', 'Yesterday', 'Наше лето'}
playlist_2 = {'Наше лето', 'Голубой вагон', 'Облака'}

# Difference
playlist_difference = playlist_1.difference(playlist_2)
print(playlist_1)
print(playlist_2)
print(playlist_difference)

# Intersection
playlist_intersection = playlist_1.intersection(playlist_2)
print(playlist_1)
print(playlist_2)
print(playlist_intersection)

# Union
playlist_union = playlist_1.union(playlist_2).union({'Новое слово'})
print(playlist_1)
print(playlist_2)
print(playlist_union)

some_set = {12, 3}

# Add to set
print('Сложение множество с самим собой:')
print(playlist_1.union(playlist_1))
print(playlist_1.add('Новый элемент я!!!'))
print(playlist_1)

print(True, False, not True, not False)

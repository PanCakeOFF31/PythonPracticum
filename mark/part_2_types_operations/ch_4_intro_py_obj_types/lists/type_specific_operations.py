# print(dir(list))
# append(+), clear(), copy(), count(), extend(+), index(), insert(), pop(+), remove(), reverse(), sort()

collection = [123, 'spam', 1.23, True, '😁']
print(collection)

collection.append('conflict')
print(collection)

deleted = collection.pop(1)
deleted_by_index = collection[2]
del collection[2]
print(collection, 'deleted:', deleted, 'and', deleted_by_index)

collection.extend([77.77, '❤️'])
print(collection)

collection.reverse()
print(collection)

iterable = ['❤️', 'True', 15, '😁']


def mapping(value):
    return value * 2


print(map(mapping, iterable))
print(list(map(mapping, iterable)))

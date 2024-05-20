mapper = {
    'a': 1,
    'b': 2,
    'c': 3
}

print(mapper)

# проверка элементов посредствам in
if not ('d' and 'f') in mapper:
    print('missing')

# получения значения без исключения
print(mapper.get('d'))

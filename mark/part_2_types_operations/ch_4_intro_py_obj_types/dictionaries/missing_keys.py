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

if mapper.get('d') is None:
    mapper['d'] = 100
    print(mapper.get('d'))
    mapper.__delitem__('d')

# получение несуществующего значения вызовет исключение
try:
    print(mapper['d'])
except:
    print('Возникло исключение')


def program_1() -> None:
    pass

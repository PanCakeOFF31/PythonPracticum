# Список []
# difference, intersection, add, union,
# Множество {}
# Словарь

set_first = {
    10,
    20,
    20
}

print(set_first)
print('length = ', len(set_first))
# print(set_first[0])

list_first = [
    10,
    20,
    30
]

print(list_first)
print('length = ', len(list_first))

print(type(set_first), type(list_first))

list_repetition = [10, 20, 30, 30, 10]
print(list_repetition)

set_without_repetition = set(list_repetition)
print(set_without_repetition)

set_without_repetition.add('Новый элемент')
print(set_without_repetition)
print(set_without_repetition.union({11, 22, 33}))

set1 = {'Day', 'Week', 'Month'}
set2 = {'Day', 'Week', 'March'}

print(set1.difference(set2))
print(set1.pop())
print(set1)

dictionary1 = {
    'рука': 'hand',
    'нога': 'leg'
    # 'рука': 10
}

print(dictionary1)
print(dictionary1.keys())
print(dictionary1.values())
print(dictionary1['рука'])

dictionary1['рука'] = "Hand"
print(dictionary1['рука'])
dictionary1['ручище'] = 'mega hand'
print(dictionary1)

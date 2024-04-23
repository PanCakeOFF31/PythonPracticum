# dict

simple_dictionary = {
    'рука': 'hand',
    'нога': 'leg'
}

print('Словарь:', simple_dictionary)
print('Ключи:', simple_dictionary.keys())
print('Значения', simple_dictionary.values())

print(simple_dictionary['рука'])
print('Создаю список из словаря:', list(simple_dictionary))

# Добавление в словарь нескольких значений
english = {
    'рука': 'arm',
    'нога': 'leg',
    'хвост': 'tail',
    'питон': 'python',
    'бэкенд-разработчик': 'back-end developer',
    'голова': 'head'
}

new_words = {'мозг': 'brain', 'логика': 'logic'}

print('Изначальный словарь:', english)
print('Новые слова:', new_words)
print(type(new_words))

english.update(new_words)
print('Словарь после добавления новых слов:', english)

# loop

favorite_songs = {
    'Тополиный пух': 'Иванушки international',
    'Город золотой': 'Аквариум',
    'Звезда по имени Солнце': 'Кино',
    'Space Oddity': 'David Bowie',
    'Рыба': 'Аквариум',
    'Серенада Трубадура': 'Муслим Магомаев',
}

print('Перебор элементов словаря:')
print(favorite_songs)

for key in favorite_songs:
    print(key)

print('Перебор items():')
print(favorite_songs.items())

for key, value in favorite_songs.items():
    print(key, ": ", value)

print('Перебор элементов словаря по ключам:')
for key in favorite_songs:
    print(key)

for i in range(5):
    print(i)

simple_list = ['asd', 'asdasd', 'asdasd']
print(simple_list[0])
print(len(simple_list))

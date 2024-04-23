import json


def print_section(text: str):
    print('-------------------------------------------------------------')
    print('\t\t', text)


my_fruits = ['apple', 'banana', 'lime']
print(my_fruits, '-', type(my_fruits))

posts_ids = [151, 245, 762, 167]
print(posts_ids, '-', type(posts_ids))

print('Сравнение списков:', my_fruits.__eq__(posts_ids))
print('Длины первого и второго списков: ', len(my_fruits), len(posts_ids))

# Итерация по списку и конкатенация элементов
new_string = ''
for item in my_fruits:
    new_string += f'{item}'

print(new_string)


# Обращение к элементам списка по индексам
def list_info(container: list, title: str = 'no-title'):
    print('Список с названием: ', title)
    print('Исходный список: ', container)
    print('Первый элемент: ', container[0])
    print('Последний элемент: ', container[-1])


print_section('Обращение к элементам списка по индексам')
list_info(my_fruits, 'my_fruits')

# Изменение элементов списка
# Копирование списка
print_section('Копирование списка с последующим изменение элементов')
fruits_copy = list(my_fruits)
fruits_copy[0] = fruits_copy[0].upper()
fruits_copy.__setitem__(0, fruits_copy.__getitem__(0).upper())

print('Исходный список')
list_info(my_fruits, 'my_fruits')
print('Измененный скопированный список')
list_info(fruits_copy, 'fruits_copy')

print_section('Удаление элементов списка')
user_inputs = [True, 'hi!', '❤️❤️', 10.5]
print('Исходный список:', user_inputs)

del user_inputs[0]
del user_inputs[-1]

print('Список после удаления первого и последнего элемента:', user_inputs)

user_inputs.__delitem__(-1)
print('Еще раз удаляем последний элемент')
print(user_inputs)

print_section('Список словарей:')
users = [
    {
        'user_id': 134,
        'user_name': 'Alice'
    },
    {
        'user_id': 135,
        'user_name': 'Alien'
    }
]

print(users)
print(users.__getitem__(0).__getitem__('user_id'))
print(users[1]['user_id'])
print(json.dumps(users, indent=4))
users.append({'user_id': '136',
              'user_name': 'Maxim'})
print(users)

# Обращение к неизвестным элементам
print_section('Перебор и ошибка')
# print(fruits_copy[10])

###
# Standard destructuring assignments
###

# Unpacking - tuple
x, y = 20, '🤩'
print('x:', x, 'y:', y)

x, y = '🤩', '(❁´◡`❁)'
print('x:', x, 'y:', y)

# Синтаксис объявление картежа
x = 10, 20
print(type(x))

# Дестрктуризация списка
x, y = [10, 44]
print('x:', x, 'y:', y)
# Деструктуризацяи кортежа
x, y = 10, 44
print('x:', x, 'y:', y)
# Деструктуризацяи множества - порядок не гарантируется
x, y = {True, 'Поляна'}
print('x:', x, 'y:', y)

# Словари
user = {
    'name': 'maxim',
    'age': 25,
    'gender': 'normal',
    'sex': 'm',
}

user_keys = list(user.keys())
user_keys.sort()

# Деструктуризация словаря с присвоением по ключам
user_age, user_gender, *user_other = user_keys
print(user_age, user_gender, user_other)

# Деструктурзиация словаря с присвоением по значениям
x, y, *rest = user.values()
print(x, y, rest)
###
# Destructuring in for loops
###
# Деструктуризация в цикле for
letters = ['A', 'B', 'X', 'Z']
letters_enum = enumerate(letters)
# Деструктурируем прямо в инструкции for ... in ...
for index, letter in letters_enum:
    print(f'По индексу [{index}] находится буква "{letter}" ')

letters_enum = enumerate(letters)
# Деструктурируем в теле цикла row - tuple.class
for row in letters_enum:
    index, letter = row
    print(f'По индексу [{index}] находится буква "{letter}" ')

###
# Ignoring values in destructuring
###

person = ('Bob', 42, 'Engineer')
name, _, profession = person
print(name, profession)

###
# Collect values or Rest values in destructuring
###

digit_list = [1, 2, 3, 4, 5, 6]

head_item, *tail_items = digit_list
print(head_item, tail_items)

*head_items, tail_item = digit_list
print(head_items, tail_item)

head_item, *middle_items, tail_item = digit_list
print(head_item, middle_items, tail_item)

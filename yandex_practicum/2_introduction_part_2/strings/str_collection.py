# Конвертация строк в коллекции.
# Строки тоже коллекции
string = 'Какая-то строка'
str_list = list(string)
str_set = set(string)

print(string)
print(str_list)
print(str_set)

print('Четвертый элемент строки', string[4], 'Четвертый элемент списка', str_list[4])
print(string[-1])
print('Строка длиной:', len(string))

# Отрицательные индексы в строках

# Разделение строки
split = string.split(sep='а')
print(split)

init_string = 'Предложение из нескольких слов.'
print(init_string.split())

# Объединение строк
joinner = ' '
string_list = ['Белый', 'Сильный', 'Красивый']
print(joinner.join(string_list))

# Шаблонная строка или строка форматирования
one_message = 'Ветренный'
two_message = 'Водяной'
three_message = 100
print(f'Эта строка форматирования из {one_message},'
      f' еще {three_message}, а также {two_message}')

# Проверка
list = [109, 20]
print(list[0])
print('asd' == 'asd')

print('================\n\tSection:')
# Альтернативное split()
init_string = "Max Min        Turbo"
print(init_string.split())
print(init_string.split(' '))

print('ax' in init_string)
print(init_string.__contains__('ax'))

print(' '.join(init_string.split()))

# print(str.startswith('Maximum', 'Max'))
listing = [10, 20, 30]
print(listing[1:])

import math
import random

# импортирование всех функций из библиотеки
from helpers import *

print_article('Импортирование')
print_section('Библиотека math')

square_root = math.sqrt(16)
print(square_root, round(math.sqrt(15), 2))

print_section_ending()
print_section('Библиотека random')

# Вывожу случайное целое число в диапазоне включительно
print(random.randint(10, 15), random.randint(10, 20))
# Возвращает случайно число в диапазоне [0;1)
print(random.random(), random.random())
# Выбираем случайный элемент из списка
initial_list = [10, '❤️', 'car', True]
print(random.choice(initial_list),
      random.choice(initial_list),
      random.choice(initial_list))

print_section_ending()
print_article_ending()

from helpers import *

print_article()
print_section("Set overview")

fruit_set = {'apple', 'banana', 'lime'}
other_fruits = {'banana', 'lime', 'apple'}
ud_set = {151, 245, 672, 167}
input_set = {True, 'hi!', '💕', 10.5}

print(fruit_set.__eq__(other_fruits), fruit_set == other_fruits)
print('Сумма двух множеств:', fruit_set.union(other_fruits))

print_section_ending()
print_section("Встроенные функции по отношению к set")

boolean_set = {True, False, True}
print("Исходный элемент:", boolean_set)
print('Любой элемент с True:', any(boolean_set))
print('Все элементы с True:', all(boolean_set))

all_true_set = {True, True, True}
print(all(all_true_set))

print_section_ending()
print_article_ending()

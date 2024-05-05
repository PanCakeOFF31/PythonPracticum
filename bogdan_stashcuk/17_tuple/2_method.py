from helpers import *

print_article("Методы кортежей")
print_section("count()/index()")

simple_list = [10, 20, 30, 15, 10]
print('Количестве чисел 10 в списке:', simple_list.count(10))
print('Индекс первого вхождения для числа 10:', simple_list.index(10))

simple_tuple = tuple(simple_list)
print('Количестве чисел 10 в кортеже:', simple_tuple.count(10))
print('Индекс первого вхождения для числа 10:', simple_tuple.index(10))

print_section_ending()
print_section('Прочие методы')
print_subsection("Добавление элемента в кортеж")

converted_list = list(simple_tuple)
converted_list.append(99)
converted_tuple = tuple(converted_list)
print(converted_tuple)

print_subsection_ending()
print_section_ending()
print_section("Практика")

nums = (10, 5, 100, 0)

if 99 in nums:
    print("99 есть в кортеже")

print(nums.index(100, 1, -1))

simple_dict = {1: 100, 2: 200}
print(tuple(simple_dict))
print(tuple(simple_dict.keys()) + tuple(simple_dict.values()))

print_section_ending()
print_article_ending()

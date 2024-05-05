from helpers import print_article

print_article("Изменяемый объект")
# Все три списка одинаковы по содержимому, но находятся в разных местах памяти
# Изменение одного, не приведет к изменению других
number_1 = 10
number_2 = 30
number_3 = 50

print(id(number_1), id(number_2), id(number_3))

list_1 = [number_1, number_2, number_3]
list_2 = [number_1, number_2, number_3]
list_3 = [number_1, number_2, number_3]

print(id(list_1), id(list_2), id(list_3))
print(list_1, list_2, list_3)

list_1.append(99)

print(id(list_1), id(list_2), id(list_3))
print(list_1, list_2, list_3)

print_article("Изменение переменных, которые ссылаются на один и тот же\n\t\tизменяемый объект")

list_1 = [number_1, number_2, number_3]
list_2 = list_1
print(list_1, list_2)

list_1.append(99)
print(list_1, list_2)

# new_dict = {}
# dict.__setitem__(new_dict, 10, 20)
# print(new_dict)

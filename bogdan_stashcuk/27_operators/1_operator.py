# Арифметические:
# + - * /
# Сравнение:
#  == != < > <= >=
# Логические
# not and or
# Присвоение
# =
# Текстовые операторы
# not and or is 'is not' in 'not in'
from helpers import print_section, print_subsection

print_section("Проверка равенство ссылок на объект")
a = 10
b = 10

c = a is not b
print(c)

print_section("Проверка равенство ссылок на объект")
a = 11
b = 12

c = a is not b
print(c)
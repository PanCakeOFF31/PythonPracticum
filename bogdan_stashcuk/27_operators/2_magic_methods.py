from helpers import print_section, print_subsection

print_section("Проверка списка на равенства")
a = [10, 20, 13]
b = [10, 20, 13]

print_subsection("Сравнение через оператора ==")
print(a is b, a == b)
print_subsection("Сравнение через магический метод __eq__()")
print(a == b, a.__eq__(b))

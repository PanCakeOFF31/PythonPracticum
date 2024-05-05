from helpers import *
print_article("Неизменяемые объекты")
print_section("Адреса неизменяемых объектов")

number_one = 10
number_two = 10
# Копирование неизменяемого объекта
number_three = number_one
print(id(number_one), id(number_two), id(number_three))
print(number_one, bin(number_one), oct(number_one), hex(number_one))
print(0b1010, 0o77, 0xff)

#
number_one += 100
print(id(number_one), id(number_two), id(number_three))

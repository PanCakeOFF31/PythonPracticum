name = 'Maxima'

# Функция выведет список всех атрибутов объекта
print(dir(name))
# Метод вернет новую строку, исходное значение осталось тем же
print(name.upper())
print(name.upper().lower().replace('a', 'A', 1))

name = name.__add__(' Blinov')
print(name)
print(name.__sizeof__())

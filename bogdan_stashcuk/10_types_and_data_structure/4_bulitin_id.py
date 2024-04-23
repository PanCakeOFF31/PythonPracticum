# Встроенная функция id() позволяет по имени переменной
# получить адрес объекта в памяти

var_1 = 755
address = id(var_1)
print(address)

address = id('new string')
print(address)

print(id('new string'))

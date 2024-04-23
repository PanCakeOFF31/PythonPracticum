origin = [10, 20, 30, 40, 50, 15, 25, 35]

print(origin)
print(origin[::])
print(origin[:])
print(origin[0:])
print(origin[0:len(origin)])
# Элементы с четными индексами
print(origin[-1::-2])
# Элементы с нечетными индексами
print(origin[-2::-2])

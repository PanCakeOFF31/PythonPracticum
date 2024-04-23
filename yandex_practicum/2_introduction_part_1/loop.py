bremen_musicians = ['Кот', 'Пёс', 'Трубадур', 'Осёл', 'Петух']

for musician in bremen_musicians:
    print(musician)

small_range = range(1, 5)
print(small_range)
print(len(small_range))

for e in small_range:
    print(e)

for number in range(5, 1):
    print(number)

print('Указание в качестве диапазона одного числа')
for i in range(10):
    print(i)

print('12 чисел в обратной последовательности:')
for i in reversed(range(1, 13)):
    print(i)

for i in {10, 20, 30}:
    print(i)

print(range(1, 10))
print(range(1, 10).__sizeof__())
print(range(1, 10).__hash__())
print(type(range(1, 2)))

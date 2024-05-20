#
iterator = iter([10, 20, 30])
print(iterator)
print(next(iterator))
print(iterator.__next__())
# iterable dict
mapper = {'d': 3, 'e': 3, 'f': 3}
print(sorted(mapper))
# manually coded a list comprehension expression
squares = [x ** 2 for x in range(1, 6)]
print(squares)
squares = []

for x in range(1, 6):
    squares.append(x ** 2)
print(squares)

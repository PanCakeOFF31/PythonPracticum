#
from helpers import print_section

iterator = iter([10, 20, 30])
print(iterator)
print(next(iterator))
print(iterator.__next__())
# iterable dict
mapper = {'e': 3, 'd': 3, 'f': 3}
print(sorted(mapper))
# manually coded a list comprehension expression
squares = [x ** 2 for x in range(1, 6)]
print(squares)
squares = []

for x in range(1, 6):
    squares.append(x ** 2)

print(squares)


# iter() exception
def program_3():
    collection = ['❤️', 'True', 15, '😁']
    iterator = iter(collection)

    for _ in range(len(collection)):
        next(iterator)

    try:
        next(iterator)
    except StopIteration:
        print("Исключение: за пределами итератора")


print_section("Выбрасывание исключения от итератора")
program_3()

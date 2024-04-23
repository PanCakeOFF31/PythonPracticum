is_authorized = True
is_new = False

print(is_authorized, is_new, type(is_new))

print(100 > 24, -5 > 0)

# Сравнение строк по значению в алфавитном порядке
print("Long String" > "Long tring")

# Сравнение строк по значению
print("Long" == 'long')

# Сравнение объектов - списков по значению
print([1, 2, 3] == [1, 2, 3])


def booling():
    print(bool(10), bool(-10), bool(0), bool(1))
    print(bool('asdasd'), bool('   '), bool('a'), bool(''))
    print(bool(10.5), bool(), bool(), bool())


booling()

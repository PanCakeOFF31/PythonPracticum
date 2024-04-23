int_value = 10

print(int_value.__eq__(15))
print(int_value.__ge__(10))
print(int_value.__gt__(10))
print(int_value.__ne__(11))

print(int.__and__(4, 25))
print(0b0011 & 0b1100)

print(dir(bool))
print(bool.__doc__)  # Обращаюсь к полю класса
print(bool(False), bool(True))

print(str.__doc__, str())

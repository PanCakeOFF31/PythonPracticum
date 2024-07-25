a = 10

try:
    raise ValueError
except ValueError as e:
    b = 11
    print(e)
    print(a, b)

print(a, b)

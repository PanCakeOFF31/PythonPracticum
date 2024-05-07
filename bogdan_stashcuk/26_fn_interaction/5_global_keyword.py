a = '😂'
print('a:', a, id(a))


def fn():
    c = 44
    global a
    a = '😁'
    print(dir())


fn()
print('a:', a, id(a))

print(dir())
print()

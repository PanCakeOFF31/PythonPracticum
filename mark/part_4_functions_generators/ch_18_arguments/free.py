[a, [b, [c]]] = [10, [10, [20]]]
print(a, b, c)

a, b = {20, 10}
print(a, b)


def unpack(value):
    # unpacking value argument
    a, (b, c) = value
    print(a, b, c)


unpack((10, (15, 30)))

a, *_, c = 1, 2, 3
print(a, _, c)

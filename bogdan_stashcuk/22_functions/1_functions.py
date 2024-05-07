def summing_void(a, b):
    c = a + b
    print(c)


def summing_result(a, b):
    c = a + b
    return c


summing_void(10, 20)
summing_result(10, 20)

print(summing_void, type(summing_void))
print(summing_void(10, 20))

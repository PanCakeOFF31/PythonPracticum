a = 10


def my_fn():
    a = True
    b = 15
    print('a:', id(a), a, 'b:', id(b), b)

    def my_fn2():
        a = 144.5
        b = 'hello'
        print('a:', id(a), a, 'b:', id(b), b)

    my_fn2()


print('a:', id(a), a)
my_fn()
# Здесь переменные a/b перестают существовать локально, остаются только глобальные
print('a:', id(a), a)

weight = 44
print(id(weight), weight)

# Здесь нет функции и блока кода, поэтому weight = ... новая глобальная переменная
if 10 > 5:
    weight = 55
    print(id(weight), weight)

print(id(weight), weight)

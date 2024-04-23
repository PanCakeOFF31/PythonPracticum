# Вызов dir() без аргументов - возвращает имена в текущей области видимости
print(dir())
print(print)
print(input)
print(dir(print))


def foo():
    print('Вызов функции foo()')


foo.__call__()
print(dir(__builtins__))
print(__builtins__)

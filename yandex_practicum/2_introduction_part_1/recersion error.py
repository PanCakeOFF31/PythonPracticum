count = 0


def foo1(count):
    count += 1
    print('foo1')
    print(count)
    foo2(count)


def foo2(count):
    count += 1
    print('foo2')
    print(count)
    foo1(count)


foo1(count)

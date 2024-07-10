from helpers import print_section

x = 'old'
print(x)


def changer():
    global x
    x = 'new'
    print(x)


changer()
print(x)

lambdas = [lambda x: x ** 2, lambda x: x ** 3]

for lm in lambdas:
    print(lm(10))
    z = 10

print(z)


def squares(x):
    for i in range(1, x):
        return i ** 2


print(squares(10))


def squares(x):
    for i in range(1, x):
        yield i ** 2


generator = squares(10)
print(next(generator), next(generator), next(generator))
print(list(squares(10)))

x = 'global old'
print(x, id(x))


# Local scope
def program_1():
    print_section("program_1(): Local scope")

    # global x
    global x
    print(x, id(x))

    # global x
    x = 'local old'
    print(x, id(x))

    def fn():
        # local x
        x = 'inner new'
        print(x, id(x))

    return fn


# Local scope
fn = program_1()
fn()

print(x, id(x))


# Nonlocal scope
def program_2():
    print_section("program_2(): Nonlocal scope")

    # local y
    y = 'outer local y'
    print(y, id(y))

    def inner():
        nonlocal y
        print(y, id(y))

    return inner


# Nonlocal scope
inner = program_2()
inner()


# Generator
def program_3():
    print_section("program_3(): Generator")

    x = 0

    def generator():
        nonlocal x
        x += 1
        return x

    def fn1():
        nonlocal x

        def fn2():
            nonlocal x
            x += 1
            return x

        x += 1
        return fn2

    return generator


# Generator
generator1 = program_3()
generator2 = program_3()

print('generator1:', generator1(), generator1())
print('generator2:', generator2(), generator2(), generator2())


# print(generator1()(), generator1()())

# Yield
def program_4():
    print_section("program_4(): Yield")

    def squares(x):
        for i in range(1, x):
            yield i ** 2

    print(squares(5))


# Yield
program_4()

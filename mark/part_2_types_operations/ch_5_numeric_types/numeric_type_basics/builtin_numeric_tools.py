import fractions


# is_integer()
def program_1():
    number = 10.4
    print(number)
    print(number.is_integer())

    number = 10.0000
    print(number.is_integer())


program_1()


# as_integer_ratio()
def program_2():
    frac = fractions.Fraction(7, 19)
    print(frac, '->', float(frac))
    ratio = frac.as_integer_ratio()
    print('numerator:', ratio[0])
    print('denominator:', ratio[1])


program_2()

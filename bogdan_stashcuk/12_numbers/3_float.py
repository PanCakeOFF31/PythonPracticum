var = 10.5
print(var, type(var))


def conversion(string: str):
    var = float(string)
    print(var, type(var))


conversion('10.5')


def checking(string: str):
    #   все символы строки являются цифрами
    if string.isdigit():
        print(string, "digit")
    #   все символы строки являются числовыми
    if string.isnumeric():
        print(string, "numeric")
    #   все символы строки - десятичные символы
    if string.isdecimal():
        print(string, "decimal")


checking('10')
checking('10f')
checking('11')

average_price = 144.7
print('average price: ', float(average_price))
print('average price: ', int(average_price))


def rounding(number: float):
    print(number, '->', round(number), type(round(number)))
    print(number, '->', round(number, 2), type(round(number, 2)))


rounding(100)
rounding(100.355)
rounding(100.50001)

sum_value = int.__add__(10, 20)
print(sum_value)


# Конвертация строки в число
def inputting():
    value = input("Введите число: ")
    if value.isdigit():
        int_value = int(value)
        print('Ваше число: ', int_value)
    else:
        print("Вы ввели не число")


# inputting()


# Возведение в степень
def powering(base, exp):
    print(f'{base} в степени {exp} будет: ', pow(base, exp))

# powering(10, 2)
# powering(2, 10)

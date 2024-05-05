try:
    # 10 / 0
    len()
except ZeroDivisionError:
    print("Возникло исключение с делением числа на ноль")
except TypeError:
    print("Какое-то не обработанное исключение:")

# print(list.__class__)

print()

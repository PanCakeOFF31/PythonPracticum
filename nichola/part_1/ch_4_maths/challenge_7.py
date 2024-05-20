def challenge_7():
    dividend = int(input("Enter a dividend: "))
    divider = int(input("Enter a divider: "))

    result = dividend // divider

    remainder = dividend % divider
    message = f"Если разделить {dividend} на {divider}, получится {result}"
    if remainder > 0:
        print(message + f" с остатком {remainder}")
    else:
        print(message + " без остатка")


# for i in range(2):
#     challenge_7()

print(10.5 / 2, 10 // 2, 10 // 2.4)

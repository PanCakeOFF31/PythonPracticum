for i in range(2):
    print(f'Итерация № {i + 1}')
    num = int(input('Enter int number between 10 and 20 inclusive: '))

    # variant 1
    if num >= 10 and num <= 20:
        print("Thank you")
    else:
        print("Incorrect answer")

    # variant 2 - chaining comparison operator
    if 10 <= num <= 20:
        print("Thank you")
    else:
        print("Incorrect answer")

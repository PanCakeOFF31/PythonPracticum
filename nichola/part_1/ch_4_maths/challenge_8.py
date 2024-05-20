def challenge_8():
    print("1) Square")
    print("2) Triangle")

    number = int(input("Enter a number: "))

    if number == 1:
        side = float(input("Enter a side size: "))
        print("Square of square is", side ** 2)
        return

    if number == 2:
        side = float(input("Enter a side size: "))
        height = float(input("Enter a height: "))
        print("Square of square is", side / 2 * height)
        return

    print("Недопустимое значения, только 1 или 2")


for _ in range(2):
    challenge_8()

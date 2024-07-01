def main():
    print("Угадай число!")
    try:
        guess = int(input("Введите свое число.\n"))
        print(f"Вы загадали {guess}")
    except ValueError:
        print("Не получилось прочитать строку...")


main()

a: str = "PanCakeOFF"
print(a)

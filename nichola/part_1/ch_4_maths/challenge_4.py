import math

number = float(input("Enter a float point number greater than 500: "))

if number <= 500:
    print("Invalid number")
else:
    print(round(math.sqrt(number), 2))

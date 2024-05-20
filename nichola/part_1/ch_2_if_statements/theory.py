from helpers import print_article

print_article('if statements')

num = 11

if num > 10:
    print('This is over 10')
elif num == 10:
    print('This is equals to 10')
else:
    print('This is under 10')

num = int(input("Enter "))

# вложенные if инструкции
if num >= 10:
    if num <= 20:
        print("This is between 10 and 20")
    else:
        print("This is over 20")
else:
    print("This is under 10")

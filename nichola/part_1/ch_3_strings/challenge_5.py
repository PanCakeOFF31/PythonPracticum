first_name = input("Enter your name: ")
name = input("Enter your name: ")

if len(name) < 5:
    surname = input("Enter your surname: ")
    total = (name + surname).upper()
    print(total)
else:
    total = name.lower()
    print(total)

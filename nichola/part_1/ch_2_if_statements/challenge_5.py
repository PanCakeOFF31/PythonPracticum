is_rainy = input("it is raining: ").lower()

if is_rainy == 'yes':
    is_windy = input("it is windy: ").lower()

    if is_windy == 'yes':
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")

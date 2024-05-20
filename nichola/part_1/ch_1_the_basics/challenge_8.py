check = int(input('Enter your check: '))
participants = int(input('Enter a participant count: '))
fraction = check / participants
print('Each person must pay: ', format(fraction, '.2f'))
print(f'Each person must pay: {fraction.__format__('.2f')}')

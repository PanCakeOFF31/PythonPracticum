new_mail = 0


def check_mail():
    if new_mail > 0:
        print('Пришло письмо, не пропусти!')
    else:
        print('Никто не пишет.')


check_mail()

new_mail = 10
check_mail()


def hello():
    print('Hello, developer')


hello()


def hello_name(name):
    print('Hello,', name)


hello_name('Максим')
hello_name('Макс')
hello_name('Максимум силы')


def default_value(name='unknown', surname='unknown'):
    print(name, surname)


default_value()
default_value('maxim')
default_value('maxim', 'blinov')
default_value(surname='blinov', name='maxim')

print(10, 20, 30, sep='!!!')


def count(a, b):
    print(a + b)


count(10, 20)
count(b=20, a=10)

x = count

x(10, 20)


def decompose_string(string):
    for character in string:
        print('\t', character)


decompose_string('maxim')
decompose_string('MaX')

print(10 < 15 < 20)

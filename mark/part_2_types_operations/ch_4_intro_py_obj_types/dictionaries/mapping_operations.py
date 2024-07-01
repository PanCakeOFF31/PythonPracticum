# dictionary - definition
from helpers import print_section

d = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print(d)
# fetching value by key 'quantity'
print(d['quantity'], d.__getitem__('quantity'))
# modifying value by key
d['quantity'] += 10
print(d)
# bob
bob1 = dict(name='Bob', job='developer', age=40)
print(bob1)
bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'developer', 40]))
print(bob2)


def program_3():
    bob1 = dict(name='Bob', job='Dev', age=40)
    print(bob1)

    keys = ['name', 'job', 'age']
    values = ['Bob', 'Dev', 40]
    bob2 = dict(zip(keys, values))
    print(bob2)


print_section("Сборка словаря из нескольких список")
program_3()


def program_4():
    marti = dict(name='Bob', age=40)
    print(marti)

    if 'job' in marti:
        print('job:', marti['job'])
    else:
        marti['job'] = 'Dev'

    print(marti)


print_section("Обращение по несуществующему ключу")
program_4()

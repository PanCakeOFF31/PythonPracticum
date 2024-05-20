print(bool(1), bool(0), bool(-1))
print(bool(1.5), bool(0.0), bool(-0.001))
print(bool(1 + 0j), bool(0 + 0j), bool(-1 - 100j))
print(bool(set()), bool(list()), bool(range(0)), bool(''))

my_list = [10, 2]

if my_list:
    print('Список не пустой')

l = list('abc')
print(type(l))

if isinstance(l, list):
    print('Это тип list')

if type(l) is list:
    print('Это тип list')

if type(l) == list:
    print('Это тип list')

if type(l) is type([]):
    print('Это тип list')

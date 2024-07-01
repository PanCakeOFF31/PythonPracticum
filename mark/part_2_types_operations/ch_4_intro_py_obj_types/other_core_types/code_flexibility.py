l = list('abc')
print(type(l))
print(type([]))
print(type(list))

if isinstance(l, list):
    print('Это тип list')

if type(l) is list:
    print('Это тип list')

# Допустимо, но не следует сравнивать согласно PEP
if type(l) == list:
    print('Это тип list')

if type(l) is type([]):
    print('Это тип list')

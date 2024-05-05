print(set('maxim'))
print(set().symmetric_difference('asasd'))

names = {'max', 'viktor', 'dima'}
print(names)

names.discard('max')
print(names)

a = {'a', 'b', 'c', 'f'}
b = {'a', 'b', 'c', 'l'}

# symmetric_difference
print((a | b) - (a & b))

# s = 'spam'
# s[0] = 10

s = 'shubbery'
l = list(s)
print(l)

joined = ''.join(l)
print(joined)

b = bytearray(b'asd')
print(b)
print(b.decode())

tup = 10, 20
print(id(tup), tup)
added = tup + (30,)
print(id(added), added)

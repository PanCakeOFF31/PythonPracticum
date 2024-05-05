r = range(1, 10, 3)
print(r, list(r))

r = range(1, 10, 1)
print(r, list(r)[1::2])

r = range(1, 10, 4)
print(r, r[1])

for item in range(10, 20, 3):
    print('item:', item)

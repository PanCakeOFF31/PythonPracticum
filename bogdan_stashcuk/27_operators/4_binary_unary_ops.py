a = +10
a = int.__pos__(10)
print(a)

a = -a
a = int.__neg__(10)
print(a)

print(True, not True, not not True)
print(1, not -1, not not 1)
print(0, not 0, not not 0)

print(0 and 0, 0 or 1)

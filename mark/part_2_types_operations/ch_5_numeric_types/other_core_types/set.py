x = set('spam')
y = set('ham')

print(x, y)

intersection = x & y
print(intersection)

union = x | y
print(union)

difference = x - y
print(difference)

print(x > {'p', 'm'})
print(y < {'h', 'a', 'm'})

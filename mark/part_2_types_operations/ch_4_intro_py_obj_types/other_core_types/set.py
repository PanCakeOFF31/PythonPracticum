x = set('spam')
y = set('ham')

print(x, y)

intersection = x & y
method_intersection = x.intersection(y)
print(intersection)

union = x | y
method_union = x.union(y)
print(union)

difference = x - y
method_difference = x.difference(y)
print(difference)

print(x > {'p', 'm'})
print(y < {'h', 'a', 'm'})

print(x.symmetric_difference(y))
print(x ^ y)

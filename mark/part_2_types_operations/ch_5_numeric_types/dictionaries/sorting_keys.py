mapper = {'a': 1, 'b': 2, 'c': 3, 'd': 3, 'e': 3, 'f': 3}

sorted_keys = list(mapper.keys())
sorted_keys.sort()

for key in sorted_keys:
    print(key, '=>', mapper[key])
# sorted() -> built-in function
print('sorted() ->', sorted(mapper.keys()))
#
word = 'collab'
for char in word:
    print('character:', char.upper())
    if char == 'l':
        break
else:
    print(word)

#
x = 4
while x > 0:
    print(x)
    x -= 1

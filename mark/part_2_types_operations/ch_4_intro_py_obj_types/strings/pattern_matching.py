import re

value = 'Hello, Python world!'
match = re.match('Hello,(.*)world!', value)

print(match)
print(match.group(1))
print(match.group())
print(match.start(), match.end())
print(value[match.start():match.end()])
# print(match.)

print(re.split('[/:]', '/user:item/booking'''))

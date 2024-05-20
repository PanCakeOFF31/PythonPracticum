import re

match = re.match('Hello,(.*)world!', 'Hello, Python world!')
print(match)
print(match.group(1))
print(match.start(), match.end())

print(ord('я'))
# print('\')

multi_str = """1 line
2 line
    3 line
        4 line"""

print(multi_str)

# raw string - для windows
path = r'C:\user\user'
print(path)
# formatted string
# template string - expression language
user_name = "maxim"
path = f'C:\\user\\{user_name}'
print(path)
# byte string
print(b'asd\12A1c'.decode())
print('\u00A3')

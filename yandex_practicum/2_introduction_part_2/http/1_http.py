import urllib.parse as up

strings = [
    'Что такое backend',
    'Привет!',
    ' ',  # Просто пробел.
    'letiště',  # Аэропорт по-чешски.
    'München',  # Крупнейший город Баварии.
    'Champs-Élysées',  # Елисейские поля.
    '東京',  # А это Токио.
]

for item in strings:
    encoded = up.quote(item)
    decoded = up.unquote(encoded)
    print(f'decode: \"{decoded}\" -> encoded: \"{encoded}\"')

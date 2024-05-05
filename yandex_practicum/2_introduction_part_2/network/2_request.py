import requests

search_params = {
    'text': 'что такое backend',
    'lr': 213
}

url = 'https://yandex.ru/search/'

response = requests.get(url=url,
                        params=search_params)

print(response.url)
print(response.status_code)
print(response.ok)
print()

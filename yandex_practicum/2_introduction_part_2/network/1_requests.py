import requests

url = 'http://wttr.in'
response = requests.get(url=url,
                        params=[('0', ''), ('T', '')])

print(response.status_code)
# print(response.headers)
print(response.text)
# print(response.content)

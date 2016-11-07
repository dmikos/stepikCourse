import requests

"""
https://yandex.ru/search/?text=Stepic
https://yandex.ru/search/?text=Python
https://yandex.ru/search/?text=Stepic&test=test1&name=Name+With+Spaces&list=test1&list=test2

res = requests.get("https://yandex.ru/search/", params={"text": "Stepic"})
print(res.status_code)
print(res.headers['Content-Type'])
print(res.url)
print(res.text)
"""

res = requests.get("https://yandex.ru/search/",
                   params={
                       "text": "Stepic",
                       "test": "test1",
                       "name": "Name With Spaces",
                       "list": ["test1", "test2"]
                   })
print(res.status_code)
print(res.headers['Content-Type'])
print(res.url)
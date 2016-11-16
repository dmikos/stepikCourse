import requests

"""
https://openweathermap.org/api
Ключ: 11c0d3dc6093f7442898ee49d2430d20
"""
api_url = "http://api.openweathermap.org/data/2.5/weather"
city = input("City? ")
params = {
    #'q': 'Kiev',
    'q': city,
    'appid': '11c0d3dc6093f7442898ee49d2430d20',
    'lang': 'ru',
    'units': 'metric'
}

res = requests.get(api_url, params=params)
# print(res.status_code)
# print(res.headers["Content-Type"])
# print(res.text)
#print(res.json()) # returns json.loads(res.text)
data = res.json()
# print(data["main"]["temp"])
template = 'Current temperature in {} is {}'
print(template.format(city, data["main"]["temp"]))
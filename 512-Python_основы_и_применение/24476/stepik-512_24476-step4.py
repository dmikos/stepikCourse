import requests
import json

# https://developers.artsy.net
# Name:           dmitriy
# Client Id:      059f40a63e79ec0c00e7
# Client Secret:  cbdfc978649d645a85cac63b2c2ec6b8


client_id = '059f40a63e79ec0c00e7'
client_secret = 'cbdfc978649d645a85cac63b2c2ec6b8'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

template = 'https://api.artsy.net/api/artists/{}'
# id = "4d8b92b34eb68a1b2c0003f4"
res = dict()
with open("dataset_24476_4.txt", "r") as f:
    for line in f.readlines():
        id = line.split()[0]

        # инициируем запрос с заголовком
        r = requests.get(template.format(id), headers=headers)

        # разбираем ответ сервера
        j = json.loads(r.text)

        # res[j["birthday"]] = [j["sortable_name"]]
        try:
            res[j["birthday"]].append(j["sortable_name"])
        except KeyError:
            res[j["birthday"]] = [j["sortable_name"]]

for i in sorted(res):
    #print(i, res[i])
    res[i].sort()
    for j in res[i]:
        print(j)

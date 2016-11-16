import requests

template = 'http://numbersapi.com/{}/math?json'
with open("dataset_24476_3.txt", "r") as f:
    for line in f.readlines():
        num = line.split()[0]
        res_url = template.format(num)
        # print(res_url)
        # num = '31'
        # res_url = template.format(num)
        res = requests.get(res_url)
        data = res.json()
        print("Interesting") if data["found"] else print("Boring")

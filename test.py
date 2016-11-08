import requests

res = requests.get("http://hosting.ukrtelecom.ua/stepik-512_24471-step7.html")
print(res.headers)

res = requests.get("http://hosting.ukrtelecom.ua/info.php")
print(res.headers)
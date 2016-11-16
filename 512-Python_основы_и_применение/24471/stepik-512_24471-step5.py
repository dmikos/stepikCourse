import requests

"""
res = requests.get("https://docs.python.org/3.5/")
print(res)
print(res.status_code)
print(res.headers['Content-Type'])

print(res.content)
print(res.text)
"""

res = requests.get("https://space.ukrtelecom.net/favicon.ico")
print(res.status_code)
print(res.headers['Content-Type'])
print(res.content)

fname = str(res.url).split('/')
# print(fname[-1])
with open(fname[-1], 'wb') as f:
    f.write(res.content)
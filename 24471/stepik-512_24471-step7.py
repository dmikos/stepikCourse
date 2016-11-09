import requests
import re

# link = input()
link = "http://hosting.ukrtelecom.ua/stepik-512_24471-step7.html"
#test3
# link = "http://pastebin.com/raw/7543p0ns"
# link = "http://hosting.ukrtelecom.ua/stepik-512_24471-step7-test3.html"
res = requests.get(link)
# print(res.text)
# print("- - -")
pattern = re.compile(r"href=.+[',\"]")
res1 = pattern.findall(res.text)
# print(res1)
for line in res1:
    line = re.split(r"[',\"]", str(line))[1]
    if line.startswith(".."):
        continue
    elif "//" in line:
        result = re.search(r"//.+\b", line)
        print(result)
    else:
        print(line)


"""
Output
    mail.ru
    neerc.ifmo.ru
    stepic.org
    www.ya.ru
    ya.ru
"""
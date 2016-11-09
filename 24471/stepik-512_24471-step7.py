import requests
import re
from urllib.parse import urlparse

# link = input()
link = "http://hosting.ukrtelecom.ua/stepik-512_24471-step7.html"
# link = "http://pastebin.com/raw/2mie4QYa"
#test3
# link = "http://pastebin.com/raw/7543p0ns"
# link = "http://hosting.ukrtelecom.ua/stepik-512_24471-step7-test3.html"

pattern = re.compile(r"href *=.+[',\"]")
res = pattern.findall(requests.get(link).text)
finset = set()

for line in res:
    line = re.split(r"[',\"]", str(line))[1]
    if line.startswith("../"):
        continue
    elif urlparse(line).scheme == '':
        # finset.add((urlparse(line).path).split(':')[0]) if urlparse(line).port else finset.add(urlparse(line).path)
        finset.add(urlparse(line).path)
    elif urlparse(line).scheme:
        finset.add((urlparse(line).netloc).split(':')[0]) if urlparse(line).port else finset.add(urlparse(line).netloc)

# print(sorted(finset))

for stroke in sorted(finset):
    print(stroke)


"""
Output
    mail.ru
    neerc.ifmo.ru
    stepic.org
    www.ya.ru
    ya.ru
"""
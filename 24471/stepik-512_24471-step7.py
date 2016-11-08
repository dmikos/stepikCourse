import requests
import re

# link = input()
link = "http://hosting.ukrtelecom.ua/stepik-512_24471-step7.html"
res = requests.get(link)
print(res.text)
print("- - -")
print()
"""
Output
    mail.ru
    neerc.ifmo.ru
    stepic.org
    www.ya.ru
    ya.ru
"""
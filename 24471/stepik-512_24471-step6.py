import requests
import re

A=input()
B=input()
TwoStep = 'No'

resA = requests.get(A)
listA = re.findall(r"href=\".+\"", resA.text)
for line in listA:
    url = line.split('"')[1]
    res = requests.get(url)
    if B in res.text:
        TwoStep = 'Yes'
print(TwoStep)


"""
# A=str(input()).split()
# B=str(input()).split()
# A = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
# B = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'
A = 'http://hosting.ukrtelecom.ua/sample0.html'
B = 'http://hosting.ukrtelecom.ua/sample2.html'
TwoStep = 'No'

resA = requests.get(A)
#resB = requests.get(B)
# print(resA.text)
# print(resA.text)
# print(re.findall(r"href=\".+\"", resA.text))
listA = re.findall(r"href=\".+\"", resA.text)
# print(listA[0].split('"')[1])
for line in listA:
    url = line.split('"')[1]
    res = requests.get(url)
    if B in res.text:
        print('Yes')

"""

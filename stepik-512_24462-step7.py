#!/usr/bin/env python3

# https://stepik.org/lesson/%D0%9D%D0%B0%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%BE%D0%B2-24462/step/7?course=Python-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D1%8B-%D0%B8-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5&unit=6768
version__ = "$Revision: 201610181516 $"
# $Source$


def add(c1, c2=[None]):
    #print("add C1 =", c1, "add C2 =", c2)
    Struct[c1] = c2
    for s in c2:
        if s not in Struct.keys():
            Struct[s] = [None]
            # print(Struct)


def recurs(c1, parent):
    if parent[0] is not None:
        for temp in parent:
            if c1 in Struct[temp]:
                return "Yes"
            else:
                recurs(c1, Struct[temp])


def get(c1, c2):
    #print("get C1 =", c1, "get C2 =", c2)
    if c1 == c2:
        print("Yes")
    elif c1 in Struct[c2]:
        print("Yes")
    else:
        print('Yes') if str(recurs(c1, Struct[c2])) == 'Yes' else print('No')

Struct = {}
# print(Struct)

# Input sequence
# i_num = int(input("Enter number: "))
i_num = int(input())
for i in range(i_num):
    string = str(input())
    if len(string) == 1:
        C1 = string
        add(C1)
    else:
        C1 = string.split()[0]
        C2 = string.split()[2:]
        add(C1, C2)
# print(Struct)

# Output sequence
# i_num = int(input("Enter number: "))
i_num = int(input())
for i in range(i_num):
    string = str(input())
    C1 = string.split()[0]
    C2 = string.split()[1]
    get(C1, C2)


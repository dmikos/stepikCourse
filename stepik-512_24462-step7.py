#!/usr/bin/env python3

# https://stepik.org/lesson/%D0%9D%D0%B0%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%BE%D0%B2-24462/step/7?course=Python-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D1%8B-%D0%B8-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5&unit=6768
version__ = "$Revision: 201610161442 $"
# $Source$


def add(c1, c2=[None]):
    print("C1 =", c1, "C2 =", c2)
    #templist = list(Struct.get(ns))
    #templist.append(var)
    Struct[c1] = c2
    # print(Struct)


def get(C1, C2):
    # print("request = get,", "namespace =", ns, ", var =", var)
    while not(var in Struct[ns]):
        ns = list(Struct.get(ns))[0]
        if not ns:
            break
    return ns

i_num = int(input("Enter number: "))
# i_num = int(input())
Struct = {}
# print(Struct)

for i in range(i_num):
    string = str(input())
    if len(string) == 1:
        C1 = string
        add(C1)
    else:
        C1 = string.split()[0]
        C2 = string.split()[2:]
        add(C1, C2)


print(Struct)

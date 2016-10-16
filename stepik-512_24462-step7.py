#!/usr/bin/env python3

# https://stepik.org/lesson/%D0%9D%D0%B0%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%BE%D0%B2-24462/step/7?course=Python-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D1%8B-%D0%B8-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5&unit=6768

def create(ns, parent):
    # print("request = create", "namespace =", ns, ", parent =", parent)
    templist = list()
    templist.append(parent)
    Struct[ns] = templist
    # print(Struct)


def add(ns, var):
    # print("request = add", "namespace =", ns, ", var =", var)
    templist = list(Struct.get(ns))
    templist.append(var)
    Struct[ns] = templist
    # print(Struct)


def get(ns, var):
    # print("request = get,", "namespace =", ns, ", var =", var)
    while not(var in Struct[ns]):
        ns = list(Struct.get(ns))[0]
        if not ns:
            break
    return ns

# num = int(input("Enter number: "))
num = int(input())
Struct = {'global': [None]}
# print(Struct)

for i in range(num):
    v1, v2, v3 = str(input()).split()
    if v1 == "create":
        create(v2, v3)
    elif v1 == "add":
        add(v2, v3)
    elif v1 == "get":
        # get(v2, v3)
        print(get(v2, v3))

# print(Struct)

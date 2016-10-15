#!/usr/bin/env python3

# https://stepik.org/lesson/%D0%9F%D1%80%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%BD%D1%81%D1%82%D0%B2%D0%B0-%D0%B8%D0%BC%D1%91%D0%BD-%D0%B8-%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D0%B8-%D0%B2%D0%B8%D0%B4%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D0%B8-24460/step/9?course=Python-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D1%8B-%D0%B8-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5&unit=6766

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


def get(parent, var):
    print("request = get,", "namespace =", parent, ", var =", var)
    ns = None
    return ns

num = int(input("Enter number: "))
Struct = {'global': [None]}
print(Struct)

for i in range(num):
    v1, v2, v3 = str(input()).split()
    if v1 == "create":
        create(v2, v3)
    elif v1 == "add":
        add(v2, v3)
    elif v1 == "get":
        get(v2, v3)

print(Struct)

# if __name__ == "__main__":
#    pass
#    func("add", "global", "a")
#    func("create", "foo", "global")
#    func("get", "foo", "a")

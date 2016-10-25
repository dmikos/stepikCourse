
Struct = dict()

num = int(input())
for i in range(num):
    exeption = str(input()).split()
    var1 = exeption[0]
    var2 = ([None] if len(exeption) == 1 else exeption[2:])
    Struct[var1] = var2
# print(Struct)

usedlist = list()
flag = 0


def recurs(exept, parent):
    for tempo in parent:
        if tempo is not None and tempo in usedlist:
            global flag
            flag = 1
        elif tempo is not None and tempo not in usedlist:
            recurs(exept, Struct[tempo])

num = int(input())
for i in range(num):
    exeption = str(input())
    if Struct[exeption][0] is not None:
        recurs(exeption, Struct[exeption])
    if flag:
        print(exeption)
    flag = 0
    usedlist.append(exeption)


# if __name__ == "__main__":
#    pass

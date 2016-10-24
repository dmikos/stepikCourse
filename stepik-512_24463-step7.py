
Struct = dict()

num = int(input())
for i in range(num):
    exeption = str(input()).split()
    var1 = exeption[0]
    var2 = ([None] if len(exeption) == 1 else exeption[2:])
    Struct[var1] = var2
print(Struct)

usedlist = list()


def recurs(exept):
    for tempo in Struct[exept]:
        if tempo is not None and tempo in usedlist:
            return 1
        elif tempo is not None and tempo not in usedlist:
            recurs(tempo)

num = int(input())
for i in range(num):
    exeption = str(input())
    if Struct[exeption][0] is not None:
            if recurs(exeption):
                print(exeption)

# if __name__ == "__main__":
#    pass
"""
def recurs(c1, parent):
    # if parent[0] is not None:
    if len(parent) and parent[0] is not None:
        for temp in parent:
            if c1 in Struct[temp]:
                return "Yes"
            else:
                recurs(c1, Struct[temp])


def get(c1, c2=[None]):
    if c2 not in Struct.keys():
        print('No')
    elif c1 == c2:
        print("Yes")
    elif c1 in Struct[c2]:
        print("Yes")
    else:
        print('Yes') if str(recurs(c1, Struct[c2])) == 'Yes' else print('No')

"""
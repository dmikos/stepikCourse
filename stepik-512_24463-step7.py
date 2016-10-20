
Struct = dict()

num = int(input())
for i in range(num):
    tempo = str(input()).split()
    var1 = tempo[0]
    var2 = ([None] if len(tempo) == 1 else tempo[2:])
    # print(var1, var2)
    Struct[var1] = var2

# print(Struct)

num = int(input())
for i in range(num):
    tempo = str(input())
    for st in Struct[tempo]:
        # print(i)
        # print(st)
        if st in Struct.keys():
            print(tempo)

# if __name__ == "__main__":
#    pass

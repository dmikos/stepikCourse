
Struct = dict()

num = int(input())
for i in range(num):
    exeption = str(input()).split()
    var1 = exeption[0]
    var2 = ([None] if len(exeption) == 1 else exeption[2:])
    Struct[var1] = var2
print(Struct)

num = int(input())
usedlist=list()
for i in range(num):
    exeption = str(input())
    for parent in Struct[exeption]:
        if parent in Struct.keys() and parent in usedlist:
            print(exeption)
    usedlist.append(exeption)

# if __name__ == "__main__":
#    pass
"""
 Sample Input:

4
ArithmeticError
ZeroDivisionError : ArithmeticError
OSError
FileNotFoundError : OSError
4
ZeroDivisionError
OSError
ArithmeticError
FileNotFoundError

Sample Output:

FileNotFoundError
"""
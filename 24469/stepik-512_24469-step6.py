s = str(input())
a = str(input())
b = str(input())


if a in b and s.count(a):
    print("Impossible")
elif a == b and not s.count(a):
    print("0")
else:
    count = 0
    while s.count(a):
        s = s.replace(a, b)
        count += 1
    print(count)

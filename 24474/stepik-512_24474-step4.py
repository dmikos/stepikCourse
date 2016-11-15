from xml.etree import ElementTree

# root = ElementTree.fromstring('<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>')
root = ElementTree.fromstring(input())

res = {"red": 0, "green": 0, "blue": 0}
val = 0


def recurs(funcroot, funcval):
    funcval += 1
    if funcroot.tag == "cube":
        res[funcroot.attrib['color']] += funcval
    for child in funcroot:
        recurs(child, funcval)

recurs(root, val)

for i in ['red', 'green', 'blue']:
    print(res[i], end=" ")

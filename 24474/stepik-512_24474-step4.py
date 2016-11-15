from xml.etree import ElementTree

root = ElementTree.fromstring('<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>')
# root = ElementTree.fromstring(input())

res = {"red":0, "green":0, "blue":0}
val = 1

# print(root)
#print(root.tag, root.attrib)

if root.tag == "cube":
    res[root.attrib['color']] += val

def recurs(root, val):
    val += 1
    for child in root:
        recurs(child, val)
    if root.tag == "cube":
        res[root.attrib['color']] += val
        # print(child.tag, child.attrib)

recurs(root, val)

print("- - -")
print(res)

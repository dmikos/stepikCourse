from xml.etree import ElementTree

tree = ElementTree.parse("example.xml")
root = tree.getroot()
# use root = ElementTree.fromstring(string_xml_data) to parse from str
"""
print(root)
print(root.tag, root.attrib)

for child in root:
    print(child.tag, child.attrib)

print(root[0][0].text)
"""

for element in root.iter("scores"):
    # print(element)
    score_sum = 0
    for child in element:
        score_sum += float(child.text)
    print(score_sum)

for element in root.iter("scores"):
    print(element)

for element in root.findall("scores"):  # .findall - перебрать только среди детей
    print(element)
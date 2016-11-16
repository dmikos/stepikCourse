from xml.etree import ElementTree

tree = ElementTree.parse("example.xml")
root = tree.getroot()

# запись в xml формате
tree.write("example_copy.xml")

# изменение xml файла
greg =root[0]
module1 = next(greg.iter("module1"))
print(module1, module1.text)

module1.text = str(float(module1.text) + 30)
print(module1, module1.text)
tree.write("example_modified.xml")

certificate = greg[2]
certificate.set("type", "with distinction")
tree.write("example_modified.xml")

# добавить новый элемент
description = ElementTree.Element("description")
description.text = "Showed excellent skills during the course"
greg.append(description)
tree.write("example_modified.xml")

# удалить элемент
description = greg.find("description")
greg.remove(description)
tree.write("example_modified.xml")

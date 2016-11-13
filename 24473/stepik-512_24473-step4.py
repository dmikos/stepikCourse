import json

result = dict()
data_json = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]'
# data_json = input()
# print(data_json)
data = json.loads(data_json)
# print(data)
for elem in data:
    # print(elem["name"])
    # print(elem["parents"])
    if elem["name"] not in result.keys():
        result[elem["name"]] = 1
    if elem["parents"]:
        for parent in elem["parents"]:
            try:
                result[parent] += 1
            except KeyError:
                result[parent] = 1


print(result)
print(sorted(result))

import json

result = dict()
data_json = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]'
# data_json = input()
data = json.loads(data_json)
for elem in data:
    print(result)
    try:
        result[elem["name"]] = +1
    except KeyError:
        result[elem["name"]] = 1
    print(result)
    if elem["parents"]:
        for parent in elem["parents"]:
            try:
                result[parent] += 1
            except KeyError:
                result[parent] = 1
    print(result)
    print("- - -")

for i in sorted(result):
    print(i, " : ", result[i])


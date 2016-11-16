import json

student1 = {
    'first name': 'Greg',
    'last name': 'Dean',
    'scores': [70, 80, 90],
    'description': "Good job, Greag",
    'sertificate': True
}

student2 = {
    'first name': 'Wirt',
    'last name': 'Wood',
    'scores': [80, 80.2, 80],
    'description': 'Nicely done',
    'sertificate': True
}

data = [student1, student2]

# print(json.dumps(data, indent=4, sort_keys=True))

# with open("students.json", "w") as f:
#     json.dump(data, f, indent=4, sort_keys=True)

data_json = json.dumps(data, indent=4, sort_keys=True)
data_again = json.loads(data_json)
# print(data_again)
# print(data_again[0])
# print(data_again[0]["scores"])
print(sum(data_again[0]["scores"]))

with open("students.json", "r") as f:
    data_again = json.load(f)
    print(sum(data_again[1]["scores"]))

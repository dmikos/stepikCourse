import csv

with open("example.csv") as f:
    reader = csv.reader(f)
    for row in reader  :
        print(row)
print("- - -")
with open("example.tsv") as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader  :
        print(row)
print("- - -")
students = [
    ["Greg", "Dean", 70, 80, 90, "Good job, Greag"],
    ["Wirt", "Wood", 80, 80.2, 80, "Nicely done"]
]

with open("example-rows-1.csv", "w") as f:
    writer = csv.writer(f)
    for student in students:
        writer.writerow(student)
print("- - -")
students = [
    ["Greg", "Dean", 70, 80, 90, "Good job, Greag"],
    ["Wirt", "Wood", 80, 80.2, 80, "Nicely done"]
]

with open("example-rows-2.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(students)
print("- - -")
students = [
    ["Greg", "Dean", 70, 80, 90, "Good job, Greag"],
    ["Wirt", "Wood", 80, 80.2, 80, "Nicely done"]
]

with open("example-rows-3.csv", "w") as f:
    # writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerows(students)

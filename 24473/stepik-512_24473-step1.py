import csv

with open("example.csv") as f:
    reader = csv.reader(f)
    for row in reader  :
        print(row)

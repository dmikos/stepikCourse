import csv

crimdict = dict()

with open("Crimes.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if "/2015 " in row['Date']:
            try:
                crimdict[row['Primary Type']] += 1
            except KeyError:
                crimdict[row['Primary Type']] = 0


# val = sorted(crimdict.values())[-1]
inv_crimdict = dict(zip(crimdict.values(), crimdict.keys()))
#print(inv_crimdict)
#print(sorted(inv_crimdict)[-1])
print(inv_crimdict[sorted(inv_crimdict)[-1]])
# Output "THEFT"

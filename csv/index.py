import csv

primaryType = {}
with open('Crimes.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['Primary Type'] not in primaryType:
            primaryType.update({row['Primary Type']: 1})
        else:
            count = primaryType.get(row['Primary Type'])
            count += 1
            primaryType.update({row['Primary Type']: count})

print(primaryType)

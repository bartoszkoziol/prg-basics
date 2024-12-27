import csv

province_dict={}

with open('province.csv', 'r') as csvfile:
    reader=csv.DictReader(csvfile)

    for row in reader:
        province_dict[row["Letter"]] = row["Province"]

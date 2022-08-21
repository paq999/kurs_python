import csv

with open("export.csv", newline="", encoding="UTF-8") as coordinate:
    csv_reader = csv.reader(coordinate)
    for index, row in enumerate(csv_reader):
        for index, row in enumerate(csv_reader):
            if index == 0:
                continue
            print(row[7][12:-2])

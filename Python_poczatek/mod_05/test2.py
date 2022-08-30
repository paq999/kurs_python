import csv

with open("export.csv", newline="", encoding="UTF-8") as coordinate:
    csv_reader = csv.reader(coordinate)
    header = next(csv_reader)
    tmp = [row for row in csv_reader]

print(header)

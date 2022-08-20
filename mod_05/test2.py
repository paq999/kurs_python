import csv

with open("export.csv", newline="", encoding="UTF-8") as coordinate:
    points = []
    csv_reader = csv.reader(coordinate)
    for index, row in enumerate(csv_reader):
        if index == 0:
            continue
        points.append((row[2], row[3]))

print(points)
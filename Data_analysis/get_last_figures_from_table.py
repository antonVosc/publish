import csv
delete = True

with open('series-220921.csv') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        pass
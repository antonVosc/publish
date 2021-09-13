import csv

date = []
close_values = []
new_dates = []

with open('sample.csv') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        if 'Date' in row or 'ERR' in row:
                pass
        else:
                for i in row:
                        if '/' in i:
                                date.append(row[0])
                                close_values.append(float(row[4]))



for i in date:
        d = i.split('/')
        if len(d[2])>2:
                d[2] = d[2][2:]
                new_dates.append('/'.join(d))
        else:
            new_dates.append(i)
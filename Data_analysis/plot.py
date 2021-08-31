import matplotlib.pyplot as plt
import numpy as np
import csv

date = []
close_values = []
with open('SPY.csv') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        if 'Date' in row:
            pass
        else:
            date.append(row[0])
            close_values.append(float(row[4]))


x = np.array(date)
y = np.array(close_values)

plt.title('Close values')
plt.plot(x,y)

plt.xlabel(date)
plt.ylabel(close_values)

plt.grid()
plt.show()
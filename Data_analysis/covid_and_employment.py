import matplotlib.pyplot as plt
import csv
from datetime import datetime
date = []
cases = []

months=[]
unemployed_perc = []

with open('uk-daily-covid-admissions.csv') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        if 'Day' in row or 'null' in row:
            pass
        else:
            date.append(row[2])
            cases.append(float(str(row[3])))

with open('unemployment_data.csv') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        months.append(row[0])
        unemployed_perc.append(float(row[1]))

x_values = [datetime.strptime(d,'%d/%m/%Y').strftime('%m/%d/%Y') for d in date]
y_values = cases


second_x_values = months
second_y_values = unemployed_perc

fig = plt.figure()
ax=fig.add_subplot(111, label="1")
ax2=fig.add_subplot(111, label="2", frame_on=False)

ax.plot(x_values, y_values, color="black")
ax.set_xlabel("Date", color="black")
ax.set_ylabel("New cases", color="black")
ax.tick_params(axis='x', colors="black")
ax.tick_params(axis='y', colors="black")

ax2.plot(second_x_values, second_y_values, color="red")
ax2.xaxis.tick_top()
ax2.yaxis.tick_right()
ax2.set_xlabel('Months', color="red")
ax2.set_ylabel('Unemployed percentage', color="red")
ax2.xaxis.set_label_position('top')
ax2.yaxis.set_label_position('right')
ax2.tick_params(axis='x', colors="red")
ax2.tick_params(axis='y', colors="red")

plt.show()

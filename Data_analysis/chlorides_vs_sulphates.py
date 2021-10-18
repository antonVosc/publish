import csv
import matplotlib.pyplot as plt

chlor = []
sulph = []
x_values = []
y_values = []
x1_values = []
y1_values = []
counter = 0

with open('winequality_white.csv') as csv_file:
    reader = csv.reader(csv_file,delimiter=',')
    for row in reader:
        if 'chlorides' in row:
            pass
        else:
            chlor.append(float(row[4]))
            sulph.append(float(row[6]))

for i in range(len(chlor)-1):
    if (i % 50) == 0:
        x_values.append(counter)
        y_values.append(chlor[i])
    counter += i

counter = 0
for i in range(len(sulph)-1):
    if (i % 50) == 0:
        x1_values.append(counter)
        y1_values.append(sulph[i])
    counter += i


data = {'x':x_values,
        'y':y_values}
data2 = {'x':x1_values,
         'y':y1_values}


fig = plt.figure()
ax=fig.add_subplot(111, label="1")
ax2=fig.add_subplot(111, label="2", frame_on=False)

ax.plot(x_values, y_values, color="black")
ax.tick_params(axis='x', colors="black")
ax.tick_params(axis='y', colors="black")
ax.xaxis.tick_top()


ax2.plot(x1_values, y1_values, color="red")
ax2.tick_params(axis='x', colors="red")
ax2.tick_params(axis='y', colors="red")
ax2.yaxis.tick_right()

plt.show()

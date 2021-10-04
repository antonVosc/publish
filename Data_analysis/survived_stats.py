import matplotlib.pyplot as plt
import csv

survived_women = []
survived_men = []
graph = []
labels_list=['Survived Men','Survived Women']

with open('Titanic_R.csv') as csv_file:
    reader = csv.reader(csv_file,delimiter=';')
    for row in reader:
        if row[14]=='1' and row[1]=='1':
            survived_women.append(row[3])
            graph.append(int(row[14]))
        if row[14]=='0' and row[1]=='1':
            survived_men.append(row[3])
            graph.append(int(row[14]))


plt.gca().set_ylim([0,500])

plt.hist(graph,bins=3)
plt.xticks([0.16,0.83],labels_list)
plt.show()
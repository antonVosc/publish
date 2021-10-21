import matplotlib.pyplot as plt
import csv

africa = 0
asia = 0
america = 0
europe = 0
oceania = 0

graph = []
labels = ['Africa', 'Asia', 'America', 'Europe', 'Oceania']

with open('1900_2021_DISASTERS.csv') as csv_file:
    reader = csv.reader(csv_file,delimiter=';')
    for row in reader:
        if 'Continent' in row or 'data' in row[0]:
            pass
        else:
            if row[12]=='Africa':
                africa += 1
            if row[12]=='Asia':
                asia += 1
            if row[12]=='Americas':
                america += 1
            if row[12]=='Europe':
                europe += 1
            if row[12]=="Oceania":
                oceania += 1

graph.append(africa)
graph.append(asia)
graph.append(america)
graph.append(europe)
graph.append(oceania)

plt.gca().set_ylim([0,7000])
plt.bar(labels,graph)

plt.show()
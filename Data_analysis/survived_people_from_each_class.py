import matplotlib.pyplot as plt
import csv

first_class_total = 0
second_class_total = 0
third_class_total = 0
first_class_survived = 0
second_class_survived = 0
third_class_survived = 0
final = 0

graph = []
labels_list=['1st class','2nd class','3rd class']

with open('Titanic_R.csv') as csv_file:
    reader = csv.reader(csv_file,delimiter=';')
    for row in reader:
        if row[0]=='1':
            first_class_total += 1
            if row[1]=='1':
                first_class_survived += 1

        if row[0]=='2':
            second_class_total += 1
            if row[1]=='1':
                second_class_survived += 1

        if row[0]=='3':
            third_class_total += 1
            if row[1]=='1':
                third_class_survived += 1

final1 = first_class_survived/(first_class_total/100)
final2 = second_class_survived/(second_class_total/100)
final3 = third_class_survived/(third_class_total/100)


graph.append(final1)
graph.append(final2)
graph.append(final3)

plt.gca().set_ylim([0,100])
plt.bar(labels_list,graph)

plt.show()
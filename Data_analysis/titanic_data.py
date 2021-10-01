import matplotlib.pyplot as plt
import csv

age = []

with open('Titanic_R.csv') as csv_file:
    reader = csv.reader(csv_file,delimiter=';')
    for row in reader:
        if 'Residence' in row or ' ' in row[4]:
            pass
        else:
            if '.' in row[4] or row[4]=='':
                full_age='0'+row[4][:2]
                age.append(int(float(full_age)))
            elif '√' in row[4]:
                age.append(int(row[:2]))
            else:
                age.append(int(row[4]))

plt.hist(age)
plt.show()
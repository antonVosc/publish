import csv
import pandas as pd
import matplotlib.pyplot as plt

quality = []
alco = []
graph = []


with open('winequality_white.csv') as csv_file:
    reader = csv.reader(csv_file,delimiter=',')
    for row in reader:
        if 'chlorides' in row:
            pass
        else:
            alco.append(int(float(row[9])))
            quality.append(int(float(row[10])))

data = {'x':alco,
        'y':quality}

df = pd.DataFrame({'x_value':alco,'y_value':quality})
plt.plot('x_value','y_value',data=df,marker='',color='red',linewidth=2)

plt.show()

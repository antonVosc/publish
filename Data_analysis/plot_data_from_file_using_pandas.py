import matplotlib.pyplot as plt
import pandas as pd
import csv
from datetime import datetime

date = []
close_values = []
average_of_last_100_days = []
start = 0
end = 101
av = 0
second_x_values = []

with open('BTC-USD.csv') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        if 'Date' in row or 'null' in row:
            pass
        else:
            date.append(row[0])
            close_values.append(float(row[4]))


while end != len(close_values)-1:
    av = 0
    for i in range(start,end):
        av += close_values[i]
    average_of_last_100_days.append(av/100)
    start += 1
    end += 1


x_values = [datetime.strptime(d,'%d/%m/%Y').strftime('%m/%d/%Y') for d in date]
y_values = close_values

del date[:102]
second_x_values=[datetime.strptime(d,'%d/%m/%Y').strftime('%m/%d/%Y') for d in date]
second_y_values=average_of_last_100_days


data = {'x':x_values,
        'y':y_values
        }

second_line = {'x':second_x_values,
               'y':second_y_values}


df = pd.DataFrame({'x_value':x_values,'y_value':y_values})
plt.plot('x_value','y_value',data=df,marker='',color='black',linewidth=2)

df = pd.DataFrame({'x_value':second_x_values,'y_value':second_y_values})
plt.plot('x_value','y_value',data=df,marker='',color='red',linewidth=2)

plt.show()

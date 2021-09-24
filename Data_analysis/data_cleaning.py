import csv
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

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

for i in range(len(close_values)-2):
    if close_values[i+1] > (close_values[i]+(close_values[i]/100*20)):
        close_values[i+1] = (close_values[i]+close_values[i+2])/2

print(new_dates)
print(close_values)
print(len(new_dates),len(close_values))
x_values = [datetime.strptime(d,"%m/%d/%y").date() for d in new_dates]
ax = plt.gca()
formatter = mdates.DateFormatter("%m-%d-%y")
locator = mdates.MonthLocator()
ax.xaxis.set_major_locator(locator)
y_values = close_values

data = {'x':x_values,
        'y':y_values
        }

df = pd.DataFrame({'x_value':x_values,'y_value':y_values})
plt.plot('x_value','y_value',data=df,marker='',color='black',linewidth=2)
plt.show()

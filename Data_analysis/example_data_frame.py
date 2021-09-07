import pandas as pd
import matplotlib.pyplot as plt

data = {'x': [6.1,5.8,5.7,5.7,5.8,5.6,5.5,5.3,5.2,5.2],
        'y': [1500,1520,1525,1523,1515,1540,1545,1560,1555,1565]
        }
df = pd.DataFrame(data,columns=['x','y'])
df.plot(x='x',y='y',kind='scatter')

plt.show()
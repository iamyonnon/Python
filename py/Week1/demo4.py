import numpy as np
import pandas as pd

t = np.arange(0, 10, 0.1)
x = np.sin(t);
y = np.cos(t);

df = pd.DataFrame({'Time' : t, 'x' : x, 'y' : y})
# print(df)
#Select all table

# print(df['y'])
#Just Select y column

# print(df['Time', 'y'])
#Select Time and y 

data = df[['Time', 'y']]
#get 5 value first when you use data.head() and get 5 value detail when you use data.tail()
#data[4:10] get data start 5 and end 10

# print(df[['Time', 'y']] [4:10])
#get value 5-10 of Time and y columns

print(df.iloc[4 : 10, [0, 2]])
#Start 5-10 and select 0, 2 Columns (Time, y)
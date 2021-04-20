import pandas as pd
import numpy as np

data = pd.read_csv('../DataSet/babies.txt', sep = '\t+')
print(data)

#Select smoke = 1
df_cohuthuoc = pd.DataFrame(data, columns = ['bwt', 'smoke']).query('smoke' == 1)
print(df_cohuthuoc)
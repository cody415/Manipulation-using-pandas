import numpy as np
import pandas as pd

d1 = {'Name': ['Pankaj', 'Meghna', 'David', 'Lisa'], 'ID': [1, 2, 3, 4], 'Salary': [100, 200, np.nan, pd.NaT],
      'Role': ['CEO', None, pd.NaT, pd.NaT]}

df = pd.DataFrame(d1)

print(df)

df.head(2)

df.tail(2)

df.isnull().sum()

df.info()

df1 = df.dropna()
print(df1)

df1 = df.dropna(axis=1)
print(df1)

import pandas as pd
import numpy as np

df = pd.DataFrame ({
    'Age': [25, 30, np.nan, 40, 35],
    'Department': ['HR', 'Finance', 'Finance', np.nan, 'IT']
})
print(df)
print("\n")

df_dropped = df.dropna(axis=0) #Rows
print(df_dropped)
print("\n")

df_dropped = df.dropna(axis=1) #Columns
print(df_dropped)
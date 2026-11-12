import pandas as pd

df = pd.DataFrame ({
    'ID': [1, 2, 2, 3, 4, 4],
    'Name': ['Alice', 'Bob', 'Bob', 'Charlie', 'David', 'David'],
    'Age': [25, 30, 30, 35, 40, 40]
})
print(df)
print("\n")

df_ori = df.drop_duplicates()
print(df_ori)
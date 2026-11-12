import pandas as pd

"""data = {'apples':[3, 2, 0, 1], 'oranges':[0, 3, 7, 2]}
df = pd.DataFrame(data)
print(df)

df = pd.DataFrame(data, index=['Cat', 'Bat', 'Ball', 'Doll'])
print(df)
print(df.loc['Ball'])"""

df = pd.read_csv('Iris.csv')
print(df)
print(df.head) #Prints first 5 rows
print(df.tail(4))
print(df.head(2))
print(df.info())
print(df.shape)

#df = pd.read_json('sample1.json')
#print(df)

temp_df = pd.concat([df, df])
print(temp_df.shape)

temp_df.drop_duplicates(inplace = True)
print(temp_df.shape)

print(df.describe())


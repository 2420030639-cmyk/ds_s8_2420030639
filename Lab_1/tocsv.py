import pandas as pd

"""data = [1, 2, 3, 10, 20, 15]
df = pd.DataFrame(data)
print(df)

df.to_csv('output.csv', index=True)"""

data = {'col_1':[3, 2, 1, 0], 'col_2':['a', 'b', 'c', 'd']}
print(pd.DataFrame.from_dict(data))
print(pd.DataFrame.from_dict(data, orient = 'index'))
print(pd.DataFrame.from_dict(data, orient = 'index', columns = ['A', 'B', 'C', 'D']))

#roll, name, age, section, 3 diff subject marks (DS, QC, TOC) dataframe -> csv
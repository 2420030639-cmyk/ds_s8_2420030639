#roll, name, age, section, 3 diff subject marks (DS, QC, TOC) dataframe -> csv

import pandas as pd

data = {
    "Roll Number": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Name": ["Kundana", "Mani", "Veda", "Kridhay", "Kumar", "Sai", "Laya", "Varshini", "Sri", "Priya"],
    "Age": [20, 21, 20, 22, 21, 20, 22, 21, 20, 21],
    "Section": ["A", "A", "B", "B", "A", "C", "C", "B", "A", "C"],
    "DS": [85, 78, 92, 88, 75, 81, 90, 84, 79, 87],
    "QC": [80, 76, 89, 91, 73, 85, 88, 82, 77, 90],
    "TOC": [82, 79, 94, 86, 74, 83, 91, 80, 78, 88]
}

df = pd.DataFrame(data)
print(df.describe())
print("\n")
print(df.shape)
print("\n")
print(df.head(4))
print("\n")

print(df)
print("\n")

df.to_csv("students.csv", index=False)

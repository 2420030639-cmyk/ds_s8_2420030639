import pandas as pd

df = pd.DataFrame({
    'TOC': [79, 89, 89, 90, 98, 86],
    'DS': [77, 98, 80, 96, 90, 82],
    'QC': [84, 89, 97, 92, 79, 88]
})

corr_matrix = df.corr(method='pearson')
print("Students Pearson Correlation Matrix:\n", corr_matrix)
print("\n")

data = pd.read_csv('Iris.csv')

corr_iris = data.corr(method='pearson', numeric_only=float)

print("Iris Pearson Correlation Matrix:\n", corr_iris)
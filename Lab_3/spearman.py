import pandas as pd
from scipy.stats import spearmanr

df = pd.DataFrame({
    'X': [10, 20, 30, 40, 50],
    'Y': [12, 24, 33, 45, 60]
})

corr_value, p_value = spearmanr(df['X'], df['Y'])
print("Spearman Correlation Coeff: ", corr_value)
print("P-Value: ", p_value)
print("\n")

df = pd.DataFrame({
    'TOC': [79, 89, 89, 90, 98, 86],
    'DS': [77, 98, 80, 96, 90, 82],
    'QC': [84, 89, 97, 92, 79, 88]
})

corr_matrix = df.corr(method='spearman')
print("Students Spearman Correlation Matrix:\n", corr_matrix)
print("\n")

data = pd.read_csv('Iris.csv')

corr_iris = data.corr(method='spearman', numeric_only=True)
print("Iris Spearman Correlation Matrix:\n", corr_iris)
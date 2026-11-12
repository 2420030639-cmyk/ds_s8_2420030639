import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
df= pd.DataFrame(iris.data, columns=iris.feature_names)

print("First 5 rows of dataset")
print(df.head())

range_val = df.max() - df.min()
print("\nRange Values:")
print(range_val)

variance_val = df.var()
print("\nVariance Values:")
print(variance_val)

std_val = df.std()
print("\nStandard Deviation Values:")
print(std_val)

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1   
print("\nInterquartile Range (IQR) Values:")
print(IQR)
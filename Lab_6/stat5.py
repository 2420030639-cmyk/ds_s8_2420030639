import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
print("First 5 rows of dataset")
print(df.head())

skewness_val = df.skew()
print("\nSkewness Values:")
print(skewness_val)

kurtosis_val = df.kurtosis()
print("\nKurtosis Values:") 
print(kurtosis_val)